# https://docs.convex.dev/quickstart

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