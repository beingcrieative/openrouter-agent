# https://ai.pydantic.dev/agents

<!--
URL: https://ai.pydantic.dev/agents
title: Agents - PydanticAI
url: https://ai.pydantic.dev/agents/
hostname: pydantic.dev
description: Agent Framework / shim to use Pydantic with LLMs
sitename: ai.pydantic.dev
date: 2024-01-01
categories: []
tags: []
image: https://ai.pydantic.dev/assets/images/social/agents.png
pagetype: website
filedate: 2024-12-14
-->

## Agents

### Introduction

Agents are PydanticAI's primary interface for interacting with LLMs.

In some use cases a single Agent will control an entire application or component, but multiple agents can also interact to embody more complex workflows.

The [ Agent](../api/agent/#pydantic_ai.Agent) class has full API documentation, but conceptually you can think of an agent as a container for:

- A
[system prompt](#system-prompts)— a set of instructions for the LLM written by the developer - One or more
[function tool](../tools/)— functions that the LLM may call to get information while generating a response - An optional structured
[result type](../results/)— the structured datatype the LLM must return at the end of a run - A
[dependency](../dependencies/)type constraint — system prompt functions, tools and result validators may all use dependencies when they're run - Agents may optionally also have a default
[LLM model](../api/models/base/)associated with them; the model to use can also be specified when running the agent
In typing terms, agents are generic in their dependency and result types, e.g., an agent which required dependencies of type `Foobar`
and returned results of type `list[str]`
would have type `cAgent[Foobar, list[str]]`
. In practice, you shouldn't need to care about this, it should just mean your IDE can tell you when you have the right type, and if you choose to use [static type checking](#static-type-checking) it should work well with PydanticAI.

Here's a toy example of an agent that simulates a roulette wheel:

```
from pydantic_ai import Agent, RunContext
roulette_agent = Agent( # (1)!
'openai:gpt-4o',
deps_type=int,
result_type=bool,
system_prompt=(
'Use the `roulette_wheel` function to see if the '
'customer has won based on the number they provide.'
),
)
@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str: # (2)!
"""check if the square is a winner"""
return 'winner' if square == ctx.deps else 'loser'

## Run the agent

success_number = 18 # (3)!
result = roulette_agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.data) # (4)!

### True

result = roulette_agent.run_sync('I bet five is the winner', deps=success_number)
print(result.data)

### False

```
- Create an agent, which expects an integer dependency and returns a boolean result. This agent will have type
`Agent[int, bool]`
. - Define a tool that checks if the square is a winner. Here
is parameterized with the dependency type`RunContext`
`int`
; if you got the dependency type wrong you'd get a typing error. - In reality, you might want to use a random number here e.g.
`random.randint(0, 36)`
. `result.data`
will be a boolean indicating if the square is a winner. Pydantic performs the result validation, it'll be typed as a`bool`
since its type is derived from the`result_type`
generic parameter of the agent.
Agents are designed for reuse, like FastAPI Apps

Agents are intended to be instantiated once (frequently as module globals) and reused throughout your application, similar to a small [FastAPI](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI) app or an [APIRouter](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter).

### Running Agents

There are three ways to run an agent:

— a coroutine which returns a`agent.run()`
containing a completed response`RunResult`
— a plain, synchronous function which returns a`agent.run_sync()`
containing a completed response (internally, this just calls`RunResult`
`loop.run_until_complete(self.run())`
)— a coroutine which returns a`agent.run_stream()`
, which contains methods to stream a response as an async iterable`StreamedRunResult`
Here's a simple example demonstrating all three:

```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o')
result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.data)

### Rome

async def main():
result = await agent.run('What is the capital of France?')
print(result.data)

### Paris

async with agent.run_stream('What is the capital of the UK?') as response:
print(await response.get_data())

### London

```
*(This example is complete, it can be run "as is")*
You can also pass messages from previous runs to continue a conversation or provide context, as described in [Messages and Chat History](../message-history/).

jupyter notebooks

If you're running `pydantic-ai`
in a jupyter notebook, you might consider using [ nest-asyncio](https://pypi.org/project/nest-asyncio/)
to manage conflicts between event loops that occur between jupyter's event loops and

`pydantic-ai`
's.Before you execute any agent runs, do the following:

```
import nest_asyncio
nest_asyncio.apply()
```

#### Additional Configuration

PydanticAI offers a [ settings.ModelSettings](../api/settings/#pydantic_ai.settings.ModelSettings) structure to help you fine tune your requests.
This structure allows you to configure common parameters that influence the model's behavior, such as

`temperature`
, `max_tokens`
,
`timeout`
, and more.There are two ways to apply these settings:
1. Passing to `run{_sync,_stream}`
functions via the `model_settings`
argument. This allows for fine-tuning on a per-request basis.
2. Setting during [ Agent](../api/agent/#pydantic_ai.Agent) initialization via the

`model_settings`
argument. These settings will be applied by default to all subsequent run calls using said agent. However, `model_settings`
provided during a specific run call will override the agent's default settings.For example, if you'd like to set the `temperature`
setting to `0.0`
to ensure less random behavior,
you can do the following:

```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o')
result_sync = agent.run_sync(
'What is the capital of Italy?', model_settings={'temperature': 0.0}
)
print(result_sync.data)

### Rome

```

### Runs vs. Conversations

An agent **run** might represent an entire conversation — there's no limit to how many messages can be exchanged in a single run. However, a **conversation** might also be composed of multiple runs, especially if you need to maintain state between separate interactions or API calls.

Here's an example of a conversation comprised of multiple runs:

```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o')

## First run

result1 = agent.run_sync('Who was Albert Einstein?')
print(result1.data)

### Albert Einstein was a German-born theoretical physicist.

## Second run, passing previous messages

result2 = agent.run_sync(
'What was his most famous equation?',
message_history=result1.new_messages(), # (1)!
)
print(result2.data)

### Albert Einstein's most famous equation is (E = mc^2).

```
- Continue the conversation; without
`message_history`
the model would not know who "his" was referring to.
*(This example is complete, it can be run "as is")*

### Type safe by design

PydanticAI is designed to work well with static type checkers, like mypy and pyright.

Typing is (somewhat) optional

PydanticAI is designed to make type checking as useful as possible for you if you choose to use it, but you don't have to use types everywhere all the time.

That said, because PydanticAI uses Pydantic, and Pydantic uses type hints as the definition for schema and validation, some types (specifically type hints on parameters to tools, and the `result_type`
arguments to [ Agent](../api/agent/#pydantic_ai.Agent)) are used at runtime.

We (the library developers) have messed up if type hints are confusing you more than they're help you, if you find this, please create an [issue](https://github.com/pydantic/pydantic-ai/issues) explaining what's annoying you!

In particular, agents are generic in both the type of their dependencies and the type of results they return, so you can use the type hints to ensure you're using the right types.

Consider the following script with type mistakes:

```
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext
@dataclass
class User:
name: str
agent = Agent(
'test',
deps_type=User, # (1)!
result_type=bool,
)
@agent.system_prompt
def add_user_name(ctx: RunContext[str]) -> str: # (2)!
return f"The user's name is {ctx.deps}."
def foobar(x: bytes) -> None:
pass
result = agent.run_sync('Does their name start with "A"?', deps=User('Anne'))
foobar(result.data) # (3)!
```
- The agent is defined as expecting an instance of
`User`
as`deps`
. - But here
`add_user_name`
is defined as taking a`str`
as the dependency, not a`User`
. - Since the agent is defined as returning a
`bool`
, this will raise a type error since`foobar`
expects`bytes`
.
Running `mypy`
on this will give the following output:

```
➤ uv run mypy type_mistakes.py
type_mistakes.py:18: error: Argument 1 to "system_prompt" of "Agent" has incompatible type "Callable[[RunContext[str]], str]"; expected "Callable[[RunContext[User]], str]" [arg-type]
type_mistakes.py:28: error: Argument 1 to "foobar" has incompatible type "bool"; expected "bytes" [arg-type]
Found 2 errors in 1 file (checked 1 source file)
```
Running `pyright`
would identify the same issues.

### System Prompts

System prompts might seem simple at first glance since they're just strings (or sequences of strings that are concatenated), but crafting the right system prompt is key to getting the model to behave as you want.

Generally, system prompts fall into two categories:

**Static system prompts**: These are known when writing the code and can be defined via the`system_prompt`
parameter of the.`Agent`
constructor**Dynamic system prompts**: These depend in some way on context that isn't known until runtime, and should be defined via functions decorated with.`@agent.system_prompt`
You can add both to a single agent; they're appended in the order they're defined at runtime.

Here's an example using both types of system prompts:

```
from datetime import date
from pydantic_ai import Agent, RunContext
agent = Agent(
'openai:gpt-4o',
deps_type=str, # (1)!
system_prompt="Use the customer's name while replying to them.", # (2)!
)
@agent.system_prompt # (3)!
def add_the_users_name(ctx: RunContext[str]) -> str:
return f"The user's named is {ctx.deps}."
@agent.system_prompt
def add_the_date() -> str: # (4)!
return f'The date is {date.today()}.'
result = agent.run_sync('What is the date?', deps='Frank')
print(result.data)

### Hello Frank, the date today is 2032-01-02.

```
- The agent expects a string dependency.
- Static system prompt defined at agent creation time.
- Dynamic system prompt defined via a decorator with
, this is called just after`RunContext`
`run_sync`
, not when the agent is created, so can benefit from runtime information like the dependencies used on that run. - Another dynamic system prompt, system prompts don't have to have the
`RunContext`
parameter.
*(This example is complete, it can be run "as is")*

### Reflection and self-correction

Validation errors from both function tool parameter validation and [structured result validation](../results/#structured-result-validation) can be passed back to the model with a request to retry.

You can also raise [ ModelRetry](../api/exceptions/#pydantic_ai.exceptions.ModelRetry) from within a

[tool](../tools/)or
[result validator function](../results/#result-validators-functions)to tell the model it should retry generating a response.
- The default retry count is
**1**but can be altered for the[entire agent](../api/agent/#pydantic_ai.Agent.__init__), a[specific tool](../api/agent/#pydantic_ai.Agent.tool), or a[result validator](../api/agent/#pydantic_ai.Agent.__init__). - You can access the current retry count from within a tool or result validator via
.`ctx.retry`
Here's an example:

```
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext, ModelRetry
from fake_database import DatabaseConn
class ChatResult(BaseModel):
user_id: int
message: str
agent = Agent(
'openai:gpt-4o',
deps_type=DatabaseConn,
result_type=ChatResult,
)
@agent.tool(retries=2)
def get_user_by_name(ctx: RunContext[DatabaseConn], name: str) -> int:
"""Get a user's ID from their full name."""
print(name)

### John

### John Doe

user_id = ctx.deps.users.get(name=name)
if user_id is None:
raise ModelRetry(
f'No user found with name {name!r}, remember to provide their full name'
)
return user_id
result = agent.run_sync(
'Send a message to John Doe asking for coffee next week', deps=DatabaseConn()
)
print(result.data)
"""
user_id=123 message='Hello John, would you be free for coffee sometime next week? Let me know what works for you!'
"""
```

### Model errors

If models behave unexpectedly (e.g., the retry limit is exceeded, or their API returns `503`
), agent runs will raise [ UnexpectedModelBehavior](../api/exceptions/#pydantic_ai.exceptions.UnexpectedModelBehavior).

In these cases, [ agent.last_run_messages](../api/agent/#pydantic_ai.Agent.last_run_messages) can be used to access the messages exchanged during the run to help diagnose the issue.

```
from pydantic_ai import Agent, ModelRetry, UnexpectedModelBehavior
agent = Agent('openai:gpt-4o')
@agent.tool_plain
def calc_volume(size: int) -> int: # (1)!
if size == 42:
return size**3
else:
raise ModelRetry('Please try again.')
try:
result = agent.run_sync('Please get me the volume of a box with size 6.')
except UnexpectedModelBehavior as e:
print('An error occurred:', e)

### An error occurred: Tool exceeded max retries count of 1

print('cause:', repr(e.__cause__))

### cause: ModelRetry('Please try again.')

print('messages:', agent.last_run_messages)
"""
messages:
[
UserPrompt(
content='Please get me the volume of a box with size 6.',
timestamp=datetime.datetime(...),
role='user',
),
ModelResponse(
parts=[
ToolCallPart(
tool_name='calc_volume',
args=ArgsDict(args_dict={'size': 6}),
tool_call_id=None,
kind='tool-call',
)
],
role='model-response',
timestamp=datetime.datetime(...),
),
RetryPrompt(
content='Please try again.',
tool_name='calc_volume',
tool_call_id=None,
timestamp=datetime.datetime(...),
role='retry-prompt',
),
ModelResponse(
parts=[
ToolCallPart(
tool_name='calc_volume',
args=ArgsDict(args_dict={'size': 6}),
tool_call_id=None,
kind='tool-call',
)
],
role='model-response',
timestamp=datetime.datetime(...),
),
]
"""
else:
print(result.data)
```
`ModelRetry`
repeatedly in this case.
*(This example is complete, it can be run "as is")*

---