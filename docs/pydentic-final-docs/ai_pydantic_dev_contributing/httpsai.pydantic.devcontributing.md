# https://ai.pydantic.dev/contributing

<!--
URL: https://ai.pydantic.dev/contributing
title: Contributing - PydanticAI
url: https://ai.pydantic.dev/contributing/
hostname: pydantic.dev
description: Agent Framework / shim to use Pydantic with LLMs
sitename: ai.pydantic.dev
date: 2024-01-01
categories: []
tags: []
image: https://ai.pydantic.dev/assets/images/social/contributing.png
pagetype: website
filedate: 2024-12-14
-->

## Contributing

We'd love you to contribute to PydanticAI!

### Installation and Setup

- Clone your fork and cd into the repo directory
`git clone `[[email protected]](/cdn-cgi/l/email-protection):<your username>/pydantic.git
cd pydantic-ai
- Install
`uv`
(version 0.4.30 or later) and`pre-commit`
We use pipx here, for other options see:

To get `pipx`
itself, see [these docs](https://pypa.github.io/pipx/)

```
pipx install uv pre-commit
```
- Install
`pydantic-ai`
, deps, test deps, and docs deps
```
make install
```

---