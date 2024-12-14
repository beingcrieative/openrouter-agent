# https://docs.convex.dev/realtime

<!--
URL: https://docs.convex.dev/realtime
title: Realtime | Convex Developer Hub
url: https://docs.convex.dev/realtime
hostname: convex.dev
description: Building realtime apps with Convex
sitename: docs.convex.dev
date: 2024-01-01
categories: []
tags: ['Stack']
image: https://docs.convex.dev/img/social.png
filedate: 2024-12-01
-->

## Realtime

Turns out Convex is automatically realtime! You don’t have to do anything
special if you are already using [query functions](/functions/query-functions),
[database](/database), and [client libraries](/client/react/) in your app.
Convex tracks the dependencies to your query functions, including database
changes, and triggers the subscription in the client libraries.

Aside from building a highly interactive app with ease, there are other benefits to the realtime architecture of Convex:

### Automatic caching[](#automatic-caching)

Convex automatically caches the result of your query functions so that future calls just read from the cache. The cache is updated if the data ever changes. You don't get charged for database bandwidth for cached reads.

This requires no work or bookkeeping from you.

### Consistent data across your app[](#consistent-data-across-your-app)

Every client subscription gets updated simultaneously to the same snapshot of the database. Your app always displays the most consistent view of your data.

This avoids bugs like increasing the number of items in the shopping cart and not showing that an item is sold out.

### Learn more[](#learn-more)

Learn how to work with realtime and reactive queries in Convex on
[Stack](https://stack.convex.dev/tag/Reactivity).

---