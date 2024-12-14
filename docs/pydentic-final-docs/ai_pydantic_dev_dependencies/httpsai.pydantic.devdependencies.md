# https://ai.pydantic.dev/dependencies

<!--
URL: https://ai.pydantic.dev/dependencies
title: Dependencies - PydanticAI
url: https://ai.pydantic.dev/dependencies/
hostname: pydantic.dev
description: Agent Framework / shim to use Pydantic with LLMs
sitename: ai.pydantic.dev
date: 2024-01-01
categories: []
tags: []
image: https://ai.pydantic.dev/assets/images/social/dependencies.png
pagetype: website
filedate: 2024-12-14
-->

## Dependencies

PydanticAI uses a dependency injection system to provide data and services to your agent's [system prompts](../agents/#system-prompts), [tools](../tools/) and [result validators](../results/#result-validators-functions).

Matching PydanticAI's design philosophy, our dependency system tries to use existing best practice in Python development rather than inventing esoteric "magic", this should make dependencies type-safe, understandable easier to test and ultimately easier to deploy in production.

### Defining Dependencies

Dependencies can be any python type. While in simple cases you might be able to pass a single object as a dependency (e.g. an HTTP connection), [dataclasses](https://docs.python.org/3/library/dataclasses.html#module-dataclasses) are generally a convenient container when your dependencies included multiple objects.

Here's an example of defining an agent that requires dependencies.

(**Note:** dependencies aren't actually used in this example, see [Accessing Dependencies](#accessing-dependencies) below)

```
from dataclasses import dataclass
import httpx
from pydantic_ai import Agent
@dataclass
class MyDeps: # (1)!
api_key: str
http_client: httpx.AsyncClient
agent = Agent(
'openai:gpt-4o',
deps_type=MyDeps, # (2)!
)
async def main():
async with httpx.AsyncClient() as client:
deps = MyDeps('foobar', client)
result = await agent.run(
'Tell me a joke.',
deps=deps, # (3)!
)
print(result.data)

### Did you hear about the toothpaste scandal? They called it Colgate.

```
- Define a dataclass to hold dependencies.
- Pass the dataclass type to the
`deps_type`
argument of the.`Agent`
constructor**Note**: we're passing the type here, NOT an instance, this parameter is not actually used at runtime, it's here so we can get full type checking of the agent. - When running the agent, pass an instance of the dataclass to the
`deps`
parameter.
*(This example is complete, it can be run "as is")*

### Accessing Dependencies

Dependencies are accessed through the [ RunContext](../api/tools/#pydantic_ai.tools.RunContext) type, this should be the first parameter of system prompt functions etc.

```
from dataclasses import dataclass
import httpx
from pydantic_ai import Agent, RunContext
@dataclass
class MyDeps:
api_key: str
http_client: httpx.AsyncClient
agent = Agent(
'openai:gpt-4o',
deps_type=MyDeps,
)
@agent.system_prompt # (1)!
async def get_system_prompt(ctx: RunContext[MyDeps]) -> str: # (2)!
response = await ctx.deps.http_client.get( # (3)!
'https://example.com',
headers={'Authorization': f'Bearer {ctx.deps.api_key}'}, # (4)!
)
response.raise_for_status()
return f'Prompt: {response.text}'
async def main():
async with httpx.AsyncClient() as client:
deps = MyDeps('foobar', client)
result = await agent.run('Tell me a joke.', deps=deps)
print(result.data)

### Did you hear about the toothpaste scandal? They called it Colgate.

```
may optionally be passed to a`RunContext`
function as the only argument.`system_prompt`
is parameterized with the type of the dependencies, if this type is incorrect, static type checkers will raise an error.`RunContext`
- Access dependencies through the
attribute.`.deps`
- Access dependencies through the
attribute.`.deps`
*(This example is complete, it can be run "as is")*

#### Asynchronous vs. Synchronous dependencies

[System prompt functions](../agents/#system-prompts), [function tools](../tools/) and [result validators](../results/#result-validators-functions) are all run in the async context of an agent run.
If these functions are not coroutines (e.g. `async def`
) they are called with
[ run_in_executor](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor) in a thread pool, it's therefore marginally preferable
to use

`async`
methods where dependencies perform IO, although synchronous dependencies should work fine too.`run`
vs. `run_sync`
and Asynchronous vs. Synchronous dependencies
Whether you use synchronous or asynchronous dependencies, is completely independent of whether you use `run`
or `run_sync`
— `run_sync`
is just a wrapper around `run`
and agents are always run in an async context.

Here's the same example as above, but with a synchronous dependency:

```
from dataclasses import dataclass
import httpx
from pydantic_ai import Agent, RunContext
@dataclass
class MyDeps:
api_key: str
http_client: httpx.Client # (1)!
agent = Agent(
'openai:gpt-4o',
deps_type=MyDeps,
)
@agent.system_prompt
def get_system_prompt(ctx: RunContext[MyDeps]) -> str: # (2)!
response = ctx.deps.http_client.get(
'https://example.com', headers={'Authorization': f'Bearer {ctx.deps.api_key}'}
)
response.raise_for_status()
return f'Prompt: {response.text}'
async def main():
deps = MyDeps('foobar', httpx.Client())
result = await agent.run(
'Tell me a joke.',
deps=deps,
)
print(result.data)

### Did you hear about the toothpaste scandal? They called it Colgate.

```
- Here we use a synchronous
`httpx.Client`
instead of an asynchronous`httpx.AsyncClient`
. - To match the synchronous dependency, the system prompt function is now a plain function, not a coroutine.
*(This example is complete, it can be run "as is")*

### Full Example

As well as system prompts, dependencies can be used in [tools](../tools/) and [result validators](../results/#result-validators-functions).

```
from dataclasses import dataclass
import httpx
from pydantic_ai import Agent, ModelRetry, RunContext
@dataclass
class MyDeps:
api_key: str
http_client: httpx.AsyncClient
agent = Agent(
'openai:gpt-4o',
deps_type=MyDeps,
)
@agent.system_prompt
async def get_system_prompt(ctx: RunContext[MyDeps]) -> str:
response = await ctx.deps.http_client.get('https://example.com')
response.raise_for_status()
return f'Prompt: {response.text}'
@agent.tool # (1)!
async def get_joke_material(ctx: RunContext[MyDeps], subject: str) -> str:
response = await ctx.deps.http_client.get(
'https://example.com#jokes',
params={'subject': subject},
headers={'Authorization': f'Bearer {ctx.deps.api_key}'},
)
response.raise_for_status()
return response.text
@agent.result_validator # (2)!
async def validate_result(ctx: RunContext[MyDeps], final_response: str) -> str:
response = await ctx.deps.http_client.post(
'https://example.com#validate',
headers={'Authorization': f'Bearer {ctx.deps.api_key}'},
params={'query': final_response},
)
if response.status_code == 400:
raise ModelRetry(f'invalid response: {response.text}')
response.raise_for_status()
return final_response
async def main():
async with httpx.AsyncClient() as client:
deps = MyDeps('foobar', client)
result = await agent.run('Tell me a joke.', deps=deps)
print(result.data)

### Did you hear about the toothpaste scandal? They called it Colgate.

```
- To pass
`RunContext`
to a tool, use thedecorator.`tool`
`RunContext`
may optionally be passed to afunction as the first argument.`result_validator`
*(This example is complete, it can be run "as is")*

### Overriding Dependencies

When testing agents, it's useful to be able to customise dependencies.

While this can sometimes be done by calling the agent directly within unit tests, we can also override dependencies while calling application code which in turn calls the agent.

This is done via the [ override](../api/agent/#pydantic_ai.Agent.override) method on the agent.

```
from dataclasses import dataclass
import httpx
from pydantic_ai import Agent, RunContext
@dataclass
class MyDeps:
api_key: str
http_client: httpx.AsyncClient
async def system_prompt_factory(self) -> str: # (1)!
response = await self.http_client.get('https://example.com')
response.raise_for_status()
return f'Prompt: {response.text}'
joke_agent = Agent('openai:gpt-4o', deps_type=MyDeps)
@joke_agent.system_prompt
async def get_system_prompt(ctx: RunContext[MyDeps]) -> str:
return await ctx.deps.system_prompt_factory() # (2)!
async def application_code(prompt: str) -> str: # (3)!
...
...

## now deep within application code we call our agent

async with httpx.AsyncClient() as client:
app_deps = MyDeps('foobar', client)
result = await joke_agent.run(prompt, deps=app_deps) # (4)!
return result.data
```
- Define a method on the dependency to make the system prompt easier to customise.
- Call the system prompt factory from within the system prompt function.
- Application code that calls the agent, in a real application this might be an API endpoint.
- Call the agent from within the application code, in a real application this call might be deep within a call stack. Note
`app_deps`
here will NOT be used when deps are overridden.
```
from joke_app import MyDeps, application_code, joke_agent
class TestMyDeps(MyDeps): # (1)!
async def system_prompt_factory(self) -> str:
return 'test prompt'
async def test_application_code():
test_deps = TestMyDeps('test_key', None) # (2)!
with joke_agent.override(deps=test_deps): # (3)!
joke = await application_code('Tell me a joke.') # (4)!
assert joke.startswith('Did you hear about the toothpaste scandal?')
```
- Define a subclass of
`MyDeps`
in tests to customise the system prompt factory. - Create an instance of the test dependency, we don't need to pass an
`http_client`
here as it's not used. - Override the dependencies of the agent for the duration of the
`with`
block,`test_deps`
will be used when the agent is run. - Now we can safely call our application code, the agent will use the overridden dependencies.

### Agents as dependencies of other Agents

Since dependencies can be any python type, and agents are just python objects, agents can be dependencies of other agents.

```
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext
@dataclass
class MyDeps:
factory_agent: Agent[None, list[str]]
joke_agent = Agent(
'openai:gpt-4o',
deps_type=MyDeps,
system_prompt=(
'Use the "joke_factory" to generate some jokes, then choose the best. '
'You must return just a single joke.'
),
)
factory_agent = Agent('gemini-1.5-pro', result_type=list[str])
@joke_agent.tool
async def joke_factory(ctx: RunContext[MyDeps], count: int) -> str:
r = await ctx.deps.factory_agent.run(f'Please generate {count} jokes.')
return '\n'.join(r.data)
result = joke_agent.run_sync('Tell me a joke.', deps=MyDeps(factory_agent))
print(result.data)

### Did you hear about the toothpaste scandal? They called it Colgate.

```

### Examples

The following examples demonstrate how to use dependencies in PydanticAI:

---