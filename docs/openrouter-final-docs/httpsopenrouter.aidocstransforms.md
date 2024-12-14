# https://openrouter.ai/docs/transforms

<!--
URL: https://openrouter.ai/docs/transforms
title: Transforms | OpenRouter
url: https://openrouter.ai
hostname: openrouter.ai
description: Transform data for model consumption
sitename: OpenRouter
date: 2023-01-01
categories: []
tags: []
image: https://openrouter.ai/dynamic-og?pathname=docs%2Ftransforms&title=Transforms&description=Transform+data+for+model+consumption
filedate: 2024-12-14
-->

## Transforms

OpenRouter has a simple rule for choosing between sending a `prompt`
and sending a list of ChatML `messages`
:

- Choose
`messages`
if you want to have OpenRouter apply a recommended instruct template to your prompt, depending on which model serves your request. Available instruct modes include: - Choose
`prompt`
if you want to send a custom prompt to the model. This is useful if you want to use a custom instruct template or maintain full control over the prompt submitted to the model.
To help with prompts that exceed the maximum context size of a model, OpenRouter supports a custom parameter called `transforms`
:

`{ transforms: ["middle-out"], // Compress prompts > context size. This is the default for endpoints with context length <= 8k messages: [...], // "prompt" works as well model // Works with any model }`
The `transforms`
param is an array of strings that tell
OpenRouter to apply a series of transformations to the prompt before
sending it to the model. Transformations are applied in-order. Available
transforms are:

`middle-out`
: compress prompts and message chains to the context size. This helps users extend conversations in part because[LLMs pay significantly less attention](https://twitter.com/xanderatallah/status/1678511019834896386)to the middle of sequences anyway. Works by compressing or removing messages in the middle of the prompt. Additionally, it reduces the number of messages to adhere to the model's limit. For instance, Anthropic's Claude models enforce a maximum of 1000 messages. This transform will only be applied to prompts that is up to twice the context size of the model.
**Note:** [All OpenRouter endpoints](/models) with 8k or less context length will default to using `middle-out`
. To disable this, set `transforms: []`
in the request body.

---