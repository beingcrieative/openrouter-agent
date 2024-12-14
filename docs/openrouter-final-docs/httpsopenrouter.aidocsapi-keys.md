# https://openrouter.ai/docs/api-keys

<!--
URL: https://openrouter.ai/docs/api-keys
title: API Keys | OpenRouter
url: https://openrouter.ai
hostname: openrouter.ai
description: Manage API keys for secure access
sitename: OpenRouter
date: 2023-01-01
categories: []
tags: []
image: https://openrouter.ai/dynamic-og?pathname=docs%2Fapi-keys&title=API+Keys&description=Manage+API+keys+for+secure+access
filedate: 2024-12-14
-->

## API Keys

Users or developers can cover model costs with normal API keys. This allows you to use `curl`
or the [OpenAI SDK](https://platform.openai.com/docs/frameworks) directly with OpenRouter. Just [create an API key](/keys), set the `api_base`
, and optionally set a [referrer header](/docs/format) to make your app discoverable to others on OpenRouter.

**Note:** API keys on OpenRouter are more powerful than keys used directly for model APIs. They allow users to set credit limits for apps, and they can be used in [OAuth](/docs/oauth) flows.
Example code:

```
import openai
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = $OPENROUTER_API_KEY
response = openai.ChatCompletion.create(
model="openai/gpt-3.5-turbo",
messages=[...],
headers={
"HTTP-Referer": $YOUR_SITE_URL, # Optional, for including your app on openrouter.ai rankings.
"X-Title": $YOUR_APP_NAME, # Optional. Shows in rankings on openrouter.ai.
},
)
reply = response.choices[0].message
```
To stream with Python, [see this example from OpenAI](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_stream_completions.ipynb).

---