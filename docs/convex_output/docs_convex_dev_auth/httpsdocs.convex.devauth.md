# https://docs.convex.dev/auth

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