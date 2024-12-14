# https://docs.convex.dev/functions

<!--
URL: https://docs.convex.dev/functions
title: Functions | Convex Developer Hub
url: https://docs.convex.dev/functions
hostname: convex.dev
description: Write functions to define your server behavior.
sitename: docs.convex.dev
date: 2024-01-01
categories: []
tags: []
image: https://docs.convex.dev/img/social.png
filedate: 2024-12-01
-->

## Functions

Functions run on the backend and are written in JavaScript (or TypeScript). They
are automatically available as APIs accessed through
[client libraries](/client/react). Everything you do in the Convex
backend starts from functions.

There are three types of functions:

[Queries](/functions/query-functions)read data from your Convex database and are automatically cached and subscribable (realtime, reactive).[Mutations](/functions/mutation-functions)write data to the database and run as a transaction.[Actions](/functions/actions)can call Open AI, Stripe, Twilio, or any other service or API you need to make your app work.
You can also build [HTTP actions](/functions/http-actions) when you
want to call your functions from a webhook or a custom client.

---