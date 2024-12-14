# https://openrouter.ai/docs/frameworks

<!--
URL: https://openrouter.ai/docs/frameworks
title: Frameworks | OpenRouter
url: https://openrouter.ai
hostname: openrouter.ai
description: Frameworks supporting model integration
sitename: OpenRouter
date: 2023-01-01
categories: []
tags: []
image: https://openrouter.ai/dynamic-og?pathname=docs%2Fframeworks&title=Frameworks&description=Frameworks+supporting+model+integration
filedate: 2024-12-14
-->

## Frameworks

You can find a few examples of using OpenRouter with other frameworks in [this Github repository](https://github.com/OpenRouterTeam/openrouter-examples). Here are some examples:

### Using OpenAI SDK

-
Using

`npm i openai`
:[github](https://github.com/OpenRouterTeam/openrouter-examples/blob/main/examples/openai/index.ts).**Tip:**You can also use[Grit](https://app.grit.io/studio?key=RKC0n7ikOiTGTNVkI8uRS)to automatically migrate your code. Simply run`npx @getgrit/launcher openrouter`
.
-
Using

`pip install openai`
:[github](https://github.com/OpenRouterTeam/openrouter-examples-python/blob/main/src/openai_test.py).
```
import OpenAI from "openai"
const openai = new OpenAI({
baseURL: "https://openrouter.ai/api/v1",
apiKey: $OPENROUTER_API_KEY,
defaultHeaders: {
"HTTP-Referer": $YOUR_SITE_URL, // Optional, for including your app on openrouter.ai rankings.
"X-Title": $YOUR_SITE_NAME, // Optional. Shows in rankings on openrouter.ai.
},
})
async function main() {
const completion = await openai.chat.completions.create({
model: "openai/gpt-4o",
messages: [
{ role: "user", content: "Say this is a test" }
],
})
console.log(completion.choices[0].message)
}
main()
```

### Using LangChain

-
Using

[LangChain for Python](https://github.com/langchain-ai/langchain):[github](https://github.com/alexanderatallah/openrouter-streamlit/blob/main/pages/2_Langchain_Quickstart.py) -
Using

[LangChain.js](https://github.com/langchain-ai/langchainjs):[github](https://github.com/OpenRouterTeam/openrouter-examples/blob/main/examples/langchain/index.ts)
```
const chat = new ChatOpenAI({
modelName: "anthropic/claude-3.5-sonnet",
temperature: 0.8,
streaming: true,
openAIApiKey: $OPENROUTER_API_KEY,
}, {
basePath: $OPENROUTER_BASE_URL + "/api/v1",
baseOptions: {
headers: {
"HTTP-Referer": "https://yourapp.com/", // Optional, for including your app on openrouter.ai rankings.
"X-Title": "Langchain.js Testing", // Optional. Shows in rankings on openrouter.ai.
},
},
});
```

### Vercel AI SDK

You can use the [Vercel AI SDK](https://www.npmjs.com/package/ai) to integrate OpenRouter with your Next.js app.
To get started, install [@openrouter/ai-sdk-provider](https://github.com/OpenRouterTeam/ai-sdk-provider):

`npm install @openrouter/ai-sdk-provider`
And then you can use [streamText()](https://sdk.vercel.ai/docs/reference/ai-sdk-core/stream-text) API to stream text from OpenRouter.

`import { createOpenRouter } from '@openrouter/ai-sdk-provider'; import { streamText } from 'ai'; import { z } from 'zod'; export const getLasagnaRecipe = async (modelName: string) => { const openrouter = createOpenRouter({ apiKey: process.env.OPENROUTER_API_KEY, }); const result = await streamText({ model: openrouter(modelName), prompt: 'Write a vegetarian lasagna recipe for 4 people.', }); return result.toAIStreamResponse(); }; export const getWeather = async (modelName: string) => { const openrouter = createOpenRouter({ apiKey: process.env.OPENROUTER_API_KEY, }); const result = await streamText({ model: openrouter(modelName), prompt: 'What is the weather in San Francisco, CA in Fahrenheit?', tools: { getCurrentWeather: { description: 'Get the current weather in a given location', parameters: z.object({ location: z .string() .describe('The city and state, e.g. San Francisco, CA'), unit: z.enum(['celsius', 'fahrenheit']).optional(), }), execute: async ({ location, unit = 'celsius' }) => { // Mock response for the weather const weatherData = { 'Boston, MA': { celsius: '15°C', fahrenheit: '59°F', }, 'San Francisco, CA': { celsius: '18°C', fahrenheit: '64°F', }, }; const weather = weatherData[location]; if (!weather) { return `Weather data for ${location} is not available.`; } return `The current weather in ${location} is ${weather[unit]}.`; }, }, }, }); return result.toAIStreamResponse(); };`

---