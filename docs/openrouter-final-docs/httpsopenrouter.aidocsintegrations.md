# https://openrouter.ai/docs/integrations

<!--
URL: https://openrouter.ai/docs/integrations
title: Integrations | OpenRouter
url: https://openrouter.ai
hostname: openrouter.ai
description: Bring your own provider keys with OpenRouter
sitename: OpenRouter
date: 2023-01-01
categories: []
tags: []
image: https://openrouter.ai/dynamic-og?pathname=docs%2Fintegrations&title=Integrations&description=Bring+your+own+provider+keys+with+OpenRouter
filedate: 2024-12-14
-->

## Integrations

### Bring your own provider API Keys

OpenRouter supports both OpenRouter credits and the option to bring your own provider keys.

When you use OpenRouter credits, your rate limits for each provider are managed by OpenRouter.

Using provider keys enables direct control over rate limits and costs via your provider account.

Your provider keys are securely encrypted and used for all requests routed through the specified provider.

Manage keys in your [account settings](/settings/integrations).

The cost of using custom provider keys on OpenRouter is **5% of the upstream provider's cost**.

#### Automatic Fallback

You can configure individual keys to act as fallbacks.When "Use this key as a fallback" is enabled for a key, OpenRouter will prioritize using your credits. If it hits a rate limit or encounters a failure, it will then retry with your key.

Conversely, if "Use this key as a fallback" is disabled for a key, OpenRouter will prioritize using your key. If it hits a rate limit or encounters a failure, it will then retry with your credits.

#### Embeddings

OpenRouter does not currently provide an embeddings API.

---