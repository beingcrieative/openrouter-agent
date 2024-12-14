# https://ai.pydantic.dev/examples/stream-markdown

<!--
URL: https://ai.pydantic.dev/examples/stream-markdown
title: Stream markdown - PydanticAI
url: https://ai.pydantic.dev/examples/stream-markdown/
hostname: pydantic.dev
description: Agent Framework / shim to use Pydantic with LLMs
sitename: ai.pydantic.dev
date: 2024-01-01
categories: []
tags: []
image: https://ai.pydantic.dev/assets/images/social/examples/stream-markdown.png
pagetype: website
filedate: 2024-12-14
-->

## Stream markdown

This example shows how to stream markdown from an agent, using the [ rich](https://github.com/Textualize/rich) library to highlight the output in the terminal.

It'll run the example with both OpenAI and Google Gemini models if the required environment variables are set.

Demonstrates:

### Running the Example

With [dependencies installed and environment variables set](../#usage), run:

```
python -m pydantic_ai_examples.stream_markdown
```
```
uv run -m pydantic_ai_examples.stream_markdown
```

### Example Code

```
import asyncio
import os
import logfire
from rich.console import Console, ConsoleOptions, RenderResult
from rich.live import Live
from rich.markdown import CodeBlock, Markdown
from rich.syntax import Syntax
from rich.text import Text
from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName

## 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured

logfire.configure(send_to_logfire='if-token-present')
agent = Agent()

## models to try, and the appropriate env var

models: list[tuple[KnownModelName, str]] = [
('gemini-1.5-flash', 'GEMINI_API_KEY'),
('openai:gpt-4o-mini', 'OPENAI_API_KEY'),
('groq:llama-3.1-70b-versatile', 'GROQ_API_KEY'),
]
async def main():
prettier_code_blocks()
console = Console()
prompt = 'Show me a short example of using Pydantic.'
console.log(f'Asking: {prompt}...', style='cyan')
for model, env_var in models:
if env_var in os.environ:
console.log(f'Using model: {model}')
with Live('', console=console, vertical_overflow='visible') as live:
async with agent.run_stream(prompt, model=model) as result:
async for message in result.stream():
live.update(Markdown(message))
console.log(result.cost())
else:
console.log(f'{model} requires {env_var} to be set.')
def prettier_code_blocks():
"""Make rich code blocks prettier and easier to copy.
From https://github.com/samuelcolvin/aicli/blob/v0.8.0/samuelcolvin_aicli.py#L22
"""
class SimpleCodeBlock(CodeBlock):
def __rich_console__(
self, console: Console, options: ConsoleOptions
) -> RenderResult:
code = str(self.text).rstrip()
yield Text(self.lexer_name, style='dim')
yield Syntax(
code,
self.lexer_name,
theme=self.theme,
background_color='default',
word_wrap=True,
)
yield Text(f'/{self.lexer_name}', style='dim')
Markdown.elements['fence'] = SimpleCodeBlock
if __name__ == '__main__':
asyncio.run(main())
```

---