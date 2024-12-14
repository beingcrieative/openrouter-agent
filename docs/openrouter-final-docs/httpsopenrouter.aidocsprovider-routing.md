# https://openrouter.ai/docs/provider-routing

<!--
URL: https://openrouter.ai/docs/provider-routing
title: Provider Routing | OpenRouter
url: https://openrouter.ai
hostname: openrouter.ai
description: Route requests across multiple providers
sitename: OpenRouter
date: 2023-01-01
categories: []
tags: []
image: https://openrouter.ai/dynamic-og?pathname=docs%2Fprovider-routing&title=Provider+Routing&description=Route+requests+across+multiple+providers
filedate: 2024-12-14
-->

## Provider Routing

OpenRouter routes requests to the best available providers for your model, given your preferences, including prompt size and output length. By default, requests are load balanced across the top providers to maximize uptime, but you can customize how this works using the `provider`
object in the request body.

### Load Balancing

For each model in your request, OpenRouter's default behavior is to load balance requests across providers with the following strategy:

- Prioritize providers that have not seen significant outages in the last 10 seconds.
- For the stable providers, look at the lowest-cost candidates and select one weighted by inverse square of the price (example below).
- Use the remaining providers as fallbacks.
Here's an example. Let's say Provider A is $1/million tokens, Provider B is $2/million, and Provider C is $3/million. Provider B recently saw a few outages.

- Your request is 9x more likely to be first routed to Provider A than Provider C.
- If Provider A is tried first and fails, then Provider C will be tried next.
- If both providers fail, Provider B will be tried last.

### Custom Routing

You can set the providers that OpenRouter will prioritize for your request using the `order`
field. The router will prioritize providers in this list, and in this order, for the model you're using. If you don't set this field, the router will [load balance](#load-balancing) across the top providers to maximize uptime.

OpenRouter will try try them one at a time and proceed to other providers if none are operational. If you don't want to allow any other providers, you should [disable fallbacks](#disabling-fallbacks) as well.

Here's an example, which will end up skipping over OpenAI (which doesn't host Mixtral), try Together, and then fall back to the normal list of providers on OpenRouter:

```
fetch("https://openrouter.ai/api/v1/chat/completions", {
method: "POST",
headers: {
"Authorization": `Bearer ${OPENROUTER_API_KEY}`,
"HTTP-Referer": `${YOUR_SITE_URL}`, // Optional, for including your app on openrouter.ai rankings.
"X-Title": `${YOUR_SITE_NAME}`, // Optional. Shows in rankings on openrouter.ai.
"Content-Type": "application/json"
},
body: JSON.stringify({
"model": "mistralai/mixtral-8x7b-instruct",
"messages": [
{"role": "user", "content": "Hello"},
],
"provider": {
"order": [
"OpenAI",
"Together"
]
},
})
});
```
Here's an example that will end up skipping over OpenAI, try Together, and then fail if Together fails:

```
fetch("https://openrouter.ai/api/v1/chat/completions", {
method: "POST",
headers: {
"Authorization": `Bearer ${OPENROUTER_API_KEY}`,
"HTTP-Referer": `${YOUR_SITE_URL}`, // Optional, for including your app on openrouter.ai rankings.
"X-Title": `${YOUR_SITE_NAME}`, // Optional. Shows in rankings on openrouter.ai.
"Content-Type": "application/json"
},
body: JSON.stringify({
"model": "mistralai/mixtral-8x7b-instruct",
"messages": [
{"role": "user", "content": "Hello"},
],
"provider": {
"order": [
"OpenAI",
"Together"
],
"allow_fallbacks": false
},
})
});
```

### Required Parameters (beta)

By default, providers that don't support a given [LLM parameter](/docs/parameters) will ignore them. But you can change this and only filter for providers that support the parameters in your request.

For example, to only use providers that support JSON formatting:

```
fetch("https://openrouter.ai/api/v1/chat/completions", {
method: "POST",
headers: {
"Authorization": `Bearer ${OPENROUTER_API_KEY}`,
"HTTP-Referer": `${YOUR_SITE_URL}`, // Optional, for including your app on openrouter.ai rankings.
"X-Title": `${YOUR_SITE_NAME}`, // Optional. Shows in rankings on openrouter.ai.
"Content-Type": "application/json"
},
body: JSON.stringify({
"model": "mistralai/mixtral-8x7b-instruct",
"messages": [
{"role": "user", "content": "Hello"},
],
"provider": {
"require_parameters": true
},
"response_format": {
"type": "json_object"
},
})
});
```

### Tool Use (beta)

When you send a request with `tools`
or `tool_choice`
, OpenRouter will only route to providers that natively support tool use.

### Data Privacy

Some model providers may log prompts, so we display them with a **Data Policy** tag on model pages. This is not a definitive source of third party data policies, but represents our best knowledge.

OpenRouter's data policy is managed in your [privacy settings](/settings/privacy). You can disable third party model providers that store inputs for training. Alternatively, you can skip or allow them on a per-request basis:

```
fetch("https://openrouter.ai/api/v1/chat/completions", {
method: "POST",
headers: {
"Authorization": `Bearer ${OPENROUTER_API_KEY}`,
"HTTP-Referer": `${YOUR_SITE_URL}`, // Optional, for including your app on openrouter.ai rankings.
"X-Title": `${YOUR_SITE_NAME}`, // Optional. Shows in rankings on openrouter.ai.
"Content-Type": "application/json"
},
body: JSON.stringify({
"model": "mistralai/mixtral-8x7b-instruct",
"messages": [
{"role": "user", "content": "Hello"},
],
"provider": {
"data_collection": "deny"
},
})
});
```
Disabling a provider causes the router to skip over it and proceed to the next best one.

### Disabling Fallbacks

To guarantee that your request is only served by the top (lowest-cost) provider, you can disable fallbacks.

You can also combine this with the `order`
field from [Custom Routing](#custom-routing) to restrict the providers that OpenRouter will prioritize to just your chosen list.

```
fetch("https://openrouter.ai/api/v1/chat/completions", {
method: "POST",
headers: {
"Authorization": `Bearer ${OPENROUTER_API_KEY}`,
"HTTP-Referer": `${YOUR_SITE_URL}`, // Optional, for including your app on openrouter.ai rankings.
"X-Title": `${YOUR_SITE_NAME}`, // Optional. Shows in rankings on openrouter.ai.
"Content-Type": "application/json"
},
body: JSON.stringify({
"model": "mistralai/mixtral-8x7b-instruct",
"messages": [
{"role": "user", "content": "Hello"},
],
"provider": {
"allow_fallbacks": false
},
})
});
```

### Ignoring Providers

#### Ignore Providers for a Request

You can ignore providers for a request by setting the `ignore`
field in the `provider`
object.

Here's an example that will ignore Azure for a request calling GPT-4 Omni:

```
fetch("https://openrouter.ai/api/v1/chat/completions", {
method: "POST",
headers: {
"Authorization": `Bearer ${OPENROUTER_API_KEY}`,
"HTTP-Referer": `${YOUR_SITE_URL}`, // Optional, for including your app on openrouter.ai rankings.
"X-Title": `${YOUR_SITE_NAME}`, // Optional. Shows in rankings on openrouter.ai.
"Content-Type": "application/json"
},
body: JSON.stringify({
"model": "openai/gpt-4o",
"messages": [
{"role": "user", "content": "Hello"},
],
"provider": {
"ignore": [
"Azure"
]
},
})
});
```

#### Ignore Providers for Account-Wide Requests

You can ignore providers for all account requests by configuring your [preferences](/settings/preferences). This configuration applies to all API requests and chatroom messages.

Warning:Ignoring multiple providers may significantly reduce fallback options and limit request recovery.
When you ignore providers for a request, the list of ignored providers is merged with your account-wide ignored providers.

### Quantization

Quantization reduces model size and computational requirements while aiming to preserve performance. However, quantized models may exhibit degraded performance for certain prompts, depending on the method used.

Providers can support various quantization levels for open-weight models.

#### Quantization Levels

By default, requests are load-balanced across all available providers, ordered by price. To filter providers by quantization level, specify the `quantizations`
field in the `provider`
parameter with the following values:

`int4`
: Integer (4 bit)`int8`
: Integer (8 bit)`fp6`
: Floating point (6 bit)`fp8`
: Floating point (8 bit)`fp16`
: Floating point (16 bit)`bf16`
: Brain floating point (16 bit)`unknown`
: Unknown

#### Example Request with Quantization

```
fetch("https://openrouter.ai/api/v1/chat/completions", {
method: "POST",
headers: {
"Authorization": `Bearer ${OPENROUTER_API_KEY}`,
"HTTP-Referer": `${YOUR_SITE_URL}`, // Optional, for including your app on openrouter.ai rankings.
"X-Title": `${YOUR_SITE_NAME}`, // Optional. Shows in rankings on openrouter.ai.
"Content-Type": "application/json"
},
body: JSON.stringify({
"model": "meta-llama/llama-3.1-8b-instruct",
"messages": [
{"role": "user", "content": "Hello"},
],
"provider": {
"quantizations": [
"fp8"
]
},
})
});
```

### JSON Schema for Provider Preferences

For a complete list of options, see this JSON schema:

```
{
"$ref": "#/definitions/ProviderPreferences",
"definitions": {
"ProviderPreferences": {
"type": "object",
"properties": {
"allow_fallbacks": {
"type": [
"boolean",
"null"
],
"description": "Whether to allow backup providers to serve requests\n- true: (default) when the primary provider (or your custom providers in \"order\") is unavailable, use the next best provider.\n- false: use only the primary/custom provider, and return the upstream error if it's unavailable.\n"
},
"require_parameters": {
"type": [
"boolean",
"null"
],
"description": "Whether to filter providers to only those that support the parameters you've provided. If this setting is omitted or set to false, then providers will receive only the parameters they support, and ignore the rest."
},
"data_collection": {
"anyOf": [
{
"type": "string",
"enum": [
"deny",
"allow"
]
},
{
"type": "null"
}
],
"description": "Data collection setting. If no available model provider meets the requirement, your request will return an error.\n- allow: (default) allow providers which store user data non-transiently and may train on it\n- deny: use only providers which do not collect user data.\n"
},
"order": {
"anyOf": [
{
"type": "array",
"items": {
"type": "string",
"enum": [
"OpenAI",
"Anthropic",
"Google",
"Google AI Studio",
"Amazon Bedrock",
"Groq",
"SambaNova",
"Cohere",
"Mistral",
"Together",
"Together 2",
"Fireworks",
"DeepInfra",
"Lepton",
"Novita",
"Avian",
"Lambda",
"Azure",
"Modal",
"AnyScale",
"Replicate",
"Perplexity",
"Recursal",
"OctoAI",
"DeepSeek",
"Infermatic",
"AI21",
"Featherless",
"Inflection",
"xAI",
"Cloudflare",
"01.AI",
"HuggingFace",
"Mancer",
"Mancer 2",
"Hyperbolic",
"Hyperbolic 2",
"Lynn 2",
"Lynn",
"Reflection"
]
}
},
{
"type": "null"
}
],
"description": "An ordered list of provider names. The router will attempt to use the first provider in the subset of this list that supports your requested model, and fall back to the next if it is unavailable. If no providers are available, the request will fail with an error message."
},
"ignore": {
"anyOf": [
{
"type": "array",
"items": {
"type": "string",
"enum": [
"OpenAI",
"Anthropic",
"Google",
"Google AI Studio",
"Amazon Bedrock",
"Groq",
"SambaNova",
"Cohere",
"Mistral",
"Together",
"Together 2",
"Fireworks",
"DeepInfra",
"Lepton",
"Novita",
"Avian",
"Lambda",
"Azure",
"Modal",
"AnyScale",
"Replicate",
"Perplexity",
"Recursal",
"OctoAI",
"DeepSeek",
"Infermatic",
"AI21",
"Featherless",
"Inflection",
"xAI",
"Cloudflare",
"01.AI",
"HuggingFace",
"Mancer",
"Mancer 2",
"Hyperbolic",
"Hyperbolic 2",
"Lynn 2",
"Lynn",
"Reflection"
]
}
},
{
"type": "null"
}
],
"description": "List of provider names to ignore. If provided, this list is merged with your account-wide ignored provider settings for this request."
},
"quantizations": {
"anyOf": [
{
"type": "array",
"items": {
"type": "string",
"enum": [
"int4",
"int8",
"fp6",
"fp8",
"fp16",
"bf16",
"unknown"
]
}
},
{
"type": "null"
}
],
"description": "A list of quantization levels to filter the provider by."
}
},
"additionalProperties": false
}
},
"$schema": "http://json-schema.org/draft-07/schema#"
}
```

---