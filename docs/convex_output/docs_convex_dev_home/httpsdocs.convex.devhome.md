# https://docs.convex.dev/home

<!--
URL: https://docs.convex.dev/home
title: Convex Docs | Convex Developer Hub
url: https://docs.convex.dev/home
hostname: convex.dev
description: Convex is an all-in-one backend platform with thoughtful, product-centric
sitename: docs.convex.dev
date: 2024-01-01
categories: []
tags: ['Convex Perspectives', 'Build AI Apps', 'Convex Patterns', 'Convex Walkthroughs']
image: https://docs.convex.dev/img/social.png
filedate: 2024-12-01
-->

## Convex Docs

Convex is an all-in-one backend platform with thoughtful, product-centric APIs.

Use [TypeScript](/production/best-practices/typescript) to write [queries as
code](/functions/query-functions) that are [automatically
cached](/realtime#automatic-caching) and [realtime](/realtime), with an acid
compliant [relational database](/database).

### Learn about Convex by creating a chat app

Convex is a novel, fun, and extremely productive way to make backends for your

### Quickstarts[](#quickstarts)

Quickly get up and running with your favorite frontend tooling or language:

### React

### Next.js

### Remix

### TanStack Start

### React Native

### Vue

### Svelte

### Node.js

### Bun

### Script tag

### Python

### iOS Swift

### Android Kotlin

### Rust

### Why Convex?[](#why-convex)

### Backends Should be Designed for Product Developers

### Intro to Convex

### Supercharging your app with a reactive backend

### Why I use Convex over Supabase as my BaaS

Read the team's Perspectives on [Stack](https://stack.convex.dev):

### Convex vs Relational Databases

### Convex vs Firebase

### It's not you, it's SQL

### How Convex Works

### The Software-Defined Database

### Convex Perspectives

### Learn Convex[](#learn-convex)

### A quick start guide for using Convex with Next.js

### Fullstack Notion Clone: Next.js 13, React, Convex, Tailwind

### Build and Deploy a Saas Podcast Platform in Next.js

### Building a Subscription Based SaaS with Stripe

See more walkthroughs and patterns on [Stack](https://stack.convex.dev)

---
<!--
URL: https://docs.convex.dev/quickstart
title: Welcome to Convex | Convex Developer Hub
url: https://docs.convex.dev/get-started
hostname: convex.dev
description: Convex is a novel, fun, and extremely productive way to make backends for your
sitename: docs.convex.dev
date: 2024-01-01
categories: []
tags: []
image: https://docs.convex.dev/img/social.png
filedate: 2024-12-01
-->

## Convex Tutorial

Convex is a novel, fun, and extremely productive way to make backends for your full-stack apps using 100% TypeScript. So first, let's explore the dashboard! Then, we'll get an example app up and running in a few minutes. We'll explore how it works, improve it together, and along the way learn the fundamentals of how to build your own projects in Convex.

### Explore the Convex dashboard[](#explore-the-convex-dashboard)

Before you get started we want to give you a quick tour of our dashboard. Click on the button below to connect your Github and create a Convex account.

### Get started with an in-dashboard tutorial

In this tutorial you will learn about how to interact with data in the dashboard and run functions. Once finished with the tutorial, you will be directed back here to continue on with a new project.

### Start developing with Convex[](#start-developing-with-convex)

### Before you begin: You'll need Node.js 16+ and Git

Ensure you have Node.js version 16 or greater installed on your computer. You
can check your version of Node.js by running `node --version`
in your terminal.
If you don't have the appropriate version of Node.js installed,
[install it from the Node.js website.](https://nodejs.org/en)

In addition, this walkthrough requires Git, so verify you have it installed by
running `git -v`
in your terminal. If not, head over to the
[Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for
installation instructions.

First, clone the example project repo from GitHub:

`git clone https://github.com/get-convex/convex-tour-chat.git`
cd convex-tour-chat
In the project root directory, install `convex`
and the other project
dependencies with `npm`
:

`npm install`
Finally, this app's `dev`
npm command sets up Convex and then runs the web app:

`npm run dev`
During setup, you'll see that Convex uses your GitHub account for authentication. Sign into Convex with GitHub and then accept the default project setup prompts.

**Make sure you keep this command ( npm run dev) running in the background
throughout this tutorial.** It's running both the dev web server for the
frontend as well as the
`convex`
command in the background to keep your backend
in sync with your local codebase.Once your app is up and running, open [localhost:5173](http://localhost:5173)
and check it out. You'll see a chat frontend running in Node.js on your
computer. This frontend connects to your new Convex backend hosted in the cloud,
which stores and retrieves the app's chat messages:

Since we just checked this codebase out, you may wonder how it knows to connect
to *your specific* Convex backend? Information about your project backend was
written to the `.env.local`
file when we set up the project. When the app starts
up, the Convex client library uses an environment variable to connect to your
backend.

For extra fun, pop up a couple of browser windows and watch Convex relay chat messages between them:

Throughout the rest of this tutorial, we're going to learn more about how this app works and learn about how to build apps in general using Convex. We'll make a few improvements to this app as we go, and finish by integrating some cool GPT AI.

### Dive into more projects first?

If instead you want to see other example projects, head on over to our
[Template Gallery](https://convex.dev/templates), or see our
[Quickstarts](/quickstarts).

We still recommend you make your way back here eventually to learn the basics about how Convex works and how to "think in Convex." Most developers find that once they master the concepts in this tutorial, they're extremely comfortable making new application architectures on the platform.

### Convex main ingredients[](#convex-main-ingredients)

In the next three parts, we'll use this chat app to walk through the following fundamental platform concepts:

-
**The Convex reactor**
First we'll explore the beating heart of Convex, a custom cloud-hosted reactive database called "the reactor." The reactor combines document-relational**tables**with deterministic TypeScript**query**and**mutation**functions. -
**Convex and your app**
Next, we'll dive into the app's frontend code, and explore how to use Convex**client libraries**to seamlessly connect your hosted backend to your app. -
**The platform in action**
Finally, we'll touch on the broader backend features outside the reactor that work together to create a comprehensive backend platform. In particular, we'll go deep on**actions**, Convex's way to create powerful jobs that integrate your app with third-party services & APIs.
Let's go!

---
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
<!--
URL: https://docs.convex.dev/functions/mutation-functions
title: Mutations | Convex Developer Hub
url: https://docs.convex.dev/functions/mutation-functions
hostname: convex.dev
description: Mutations insert, update and remove data from the database, check authentication
sitename: docs.convex.dev
date: 2024-01-01
categories: []
tags: []
image: https://docs.convex.dev/img/social.png
filedate: 2024-12-01
-->

## Mutations

Mutations insert, update and remove data from the database, check authentication or perform other business logic, and optionally return a response to the client application.

This is an example mutation, taking in named arguments, writing data to the database and returning a result:

`import { mutation } from "./_generated/server";`
import { v } from "convex/values";
// Create a new task with the given text
export const createTask = mutation({
args: { text: v.string() },
handler: async (ctx, args) => {
const newTaskId = await ctx.db.insert("tasks", { text: args.text });
return newTaskId;
},
});
Read on to understand how to build mutations yourself.

### Mutation names[](#mutation-names)

Mutations follow the same naming rules as queries, see
[Query names](/functions/query-functions#query-names).

Queries and mutations can be defined in the same file when using named exports.

### The `mutation`

constructor[](#the-mutation-constructor)
To declare a mutation in Convex use the `mutation`
constructor function. Pass it
an object with a `handler`
function, which performs the mutation:

`import { mutation } from "./_generated/server";`
export const mutateSomething = mutation({
handler: () => {
// implementation will be here
},
});
Unlike a query, a mutation can but does not have to return a value.

#### Mutation arguments[](#mutation-arguments)

Just like queries, mutations accept named arguments, and the argument values are
accessible as fields of the second parameter of the `handler`
function:

`import { mutation } from "./_generated/server";`
export const mutateSomething = mutation({
handler: (_, args: { a: number; b: number }) => {
// do something with `args.a` and `args.b`
// optionally return a value
return "success";
},
});
Arguments and responses are automatically serialized and deserialized, and you can pass and return most value-like JavaScript data to and from your mutation.

To both declare the types of arguments and to validate them, add an `args`
object using `v`
validators:

`import { mutation } from "./_generated/server";`
import { v } from "convex/values";
export const mutateSomething = mutation({
args: { a: v.number(), b: v.number() },
handler: (_, args) => {
// do something with `args.a` and `args.b`
},
});
See [argument validation](/functions/validation) for the full list of
supported types and validators.

The first parameter to the handler function is reserved for the mutation context.

#### Mutation responses[](#mutation-responses)

Queries can return values of any supported
[Convex type](/functions/validation) which will be automatically
serialized and deserialized.

Mutations can also return `undefined`
, which is not a valid Convex value. When a
mutation returns `undefined`
**it is translated to null** on the client.

#### Mutation context[](#mutation-context)

The `mutation`
constructor enables writing data to the database, and other
Convex features by passing a
[MutationCtx](/generated-api/server#mutationctx) object to the handler
function as the first parameter:

`import { mutation } from "./_generated/server";`
import { v } from "convex/values";
export const mutateSomething = mutation({
args: { a: v.number(), b: v.number() },
handler: (ctx, args) => {
// Do something with `ctx`
},
});
Which part of the mutation context is used depends on what your mutation needs to do:

-
To read from and write to the database use the

`db`
field. Note that we make the handler function an`async`
function so we can`await`
the promise returned by`db.insert()`
:convex/myFunctions.tsTS`import { mutation } from "./_generated/server";`
import { v } from "convex/values";
export const addItem = mutation({
args: { text: v.string() },
handler: async (ctx, args) => {
await ctx.db.insert("tasks", { text: args.text });
},
});Read on about

[Writing Data](/database/writing-data). -
To generate upload URLs for storing files use the

`storage`
field. Read on about[File Storage](/file-storage). -
To check user authentication use the

`auth`
field. Read on about[Authentication](/auth). -
To schedule functions to run in the future, use the

`scheduler`
field. Read on about[Scheduled Functions](/scheduling/scheduled-functions).

### Splitting up mutation code via helpers[](#splitting-up-mutation-code-via-helpers)

When you want to split up the code in your mutation or reuse logic across multiple Convex functions you can define and call helper

`import { v } from "convex/values";`
import { mutation, MutationCtx } from "./_generated/server";
export const addItem = mutation({
args: { text: v.string() },
handler: async (ctx, args) => {
await ctx.db.insert("tasks", { text: args.text });
await trackChange(ctx, "addItem");
},
});
async function trackChange(ctx: MutationCtx, type: "addItem" | "removeItem") {
await ctx.db.insert("changes", { type });
}
Mutations can call helpers that take a
[QueryCtx](/generated-api/server#queryctx) as argument, since the
mutation context can do everything query context can.

You can `export`
helpers to use them across multiple files. They will not be
callable from outside of your Convex functions.

See
[Type annotating server side helpers](/production/best-practices/typescript#type-annotating-server-side-helpers)
for more guidance on TypeScript types.

### Using NPM packages[](#using-npm-packages)

Mutations can import NPM packages installed in `node_modules`
. Not all NPM
packages are supported, see
[Runtimes](/functions/runtimes#default-convex-runtime) for more
details.

`npm install @faker-js/faker`
`import { faker } from "@faker-js/faker";`
import { mutation } from "./_generated/server";
export const randomName = mutation({
args: {},
handler: async (ctx) => {
faker.seed();
await ctx.db.insert("tasks", { text: "Greet " + faker.person.fullName() });
},
});

### Calling mutations from clients[](#calling-mutations-from-clients)

To call a mutation from [React](/client/react) use the generated
[ useMutation](/client/react#editing-data) hook:

To call a mutation from [React](/client/react) use the
[ useMutation](/api/modules/react#usemutation) hook along with the generated

[object.](/generated-api/api)
`api`
`import { useMutation } from "convex/react";`
import { api } from "../convex/_generated/api";
export function MyApp() {
const mutateSomething = useMutation(api.myFunctions.mutateSomething);
const handleClick = () => {
mutateSomething({ a: 1, b: 2 });
};
// pass `handleClick` to a button
// ...
}
See the [React](/client/react) client documentation for all the ways
queries can be called.

When mutations are called from the [React](/client/react) or
[Rust](/client/rust) clients, they are executed one at a time in a single,
ordered queue. You don't have to worry about mutations editing the database in a
different order than they were triggered.

### Transactions[](#transactions)

Mutations run **transactionally**. This means that:

- All database reads inside the transaction get a consistent view of the data in the database. You don't have to worry about a concurrent update changing the data in the middle of the execution.
- All database writes get committed together. If the mutation writes some data to the database, but later throws an error, no data is actually written to the database.
For this to work, similarly to queries, mutations must be deterministic, and
cannot call third party APIs. To call third party APIs, use
[actions](/functions/actions).

### Limits[](#limits)

Mutations have a limit to the amount of data they can read and write at once to
guarantee good performance. Check out these limits
[here](/functions/error-handling/#database-limitations).

For information on other limits, see [here](/production/state/limits).

---
<!--
URL: https://docs.convex.dev/auth
title: Authentication | Convex Developer Hub
url: https://docs.convex.dev/auth
hostname: convex.dev
description: Add authentication to your Convex app.
sitename: docs.convex.dev
date: 2024-01-01
categories: []
tags: []
image: https://docs.convex.dev/img/social.png
filedate: 2024-12-01
-->

## Authentication

Authentication allows you to identify users and restrict what data they can see and edit.

### Convex Auth[](#convex-auth)

For client-side React and React Native mobile apps you can implement auth
directly in Convex with the [Convex Auth](/auth/convex-auth) library.
This [npm package](https://github.com/get-convex/convex-auth) runs on your
Convex deployment and helps you build a custom sign-up/sign-in flow via social
identity providers, one-time email or SMS access codes, or via passwords.

Convex Auth is in beta (it isn't complete and may change in backward-incompatible ways) and doesn't provide as many features as third party auth integrations. Since it doesn't require signing up for another service it's the quickest way to get auth up and running.

Convex Auth is currently a [beta
feature](/production/state/#beta-features). If you have feedback or feature
requests, [let us know on Discord](https://convex.dev/community)!

Support for Next.js is under active development. If you'd like to help test this
experimental support please [give it a try](https://labs.convex.dev/auth)!

### Third-party authentication platforms[](#third-party-authentication-platforms)

Leveraging a Convex integration with a third-party auth provider provides the most comprehensive authentication solutions. Integrating another service provides a ton of functionality like passkeys, two-factor auth, spam protection, and more on top of the authentication basics.

[Clerk](/auth/clerk)is newer and has better Next.js and React Native support[Auth0](/auth/auth0)is more established with more bells and whistles[Custom Auth Integration](/auth/advanced/custom-auth)allow any OpenID Connect-compatible identity provider to be used for authentication
After you integrate one of these, learn more about accessing authentication
information in [Functions](/auth/functions-auth) and storing user
information in the [Database](/auth/database-auth).

### Debugging[](#debugging)

If you run into issues consult the [Debugging](/auth/debug) guide.

---