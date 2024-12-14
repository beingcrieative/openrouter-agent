# https://docs.convex.dev/production

<!--
URL: https://docs.convex.dev/production
title: Deploying Your App to Production | Convex Developer Hub
url: https://docs.convex.dev/production
hostname: convex.dev
description: Convex is built to serve live, production app traffic. Here we cover how to
sitename: docs.convex.dev
date: 2024-01-01
categories: []
tags: []
image: https://docs.convex.dev/img/social.png
filedate: 2024-12-01
-->

## Deploying Your App to Production

Convex is built to serve live, production app traffic. Here we cover how to deploy and maintain a production version of your app.

### Project management[](#project-management)

When you sign up for Convex, a Convex team is created for you. You can
[create more teams from the dashboard](/dashboard/teams) and add other
people to them as members. You can upgrade your team to the
[Pro plan](https://www.convex.dev/plans) for additional features, higher limits
and usage-based pricing.

Each team can have multiple projects. When you run `npx convex dev`
for the
first time, a project is created for you automatically. You can also create a
project from the dashboard.

Every project has one shared production deployment and one development deployment per team member. This allows each team member to make and test changes independently before they are deployed to the production deployment.

Usually all deployments belonging to a single project run the same code base (or
a version of it), but Convex doesn't enforce this. You can also run the same
code base on multiple different prod deployments belonging to different
projects, see [staging](#staging-environment) below.

### Deploying to production[](#deploying-to-production)

Your Convex deployments run your backend logic and in most cases you will also
develop a client that uses the backend. If your client is a web app, follow the
[Hosting and Deployment](/production/hosting/) guide, to learn
how to deploy your client and your Convex backend together.

You can also deploy your backend on its own. Check out the
[Project Configuration](/production/project-configuration) page to
learn more.

### Staging environment[](#staging-environment)

With Convex
[preview deployments](/production/hosting/preview-deployments) your
team can test out changes before deploying them to production. If you need a
more permanent staging environment, you can use a separate Convex project, and
deploy to it by setting the `CONVEX_DEPLOY_KEY`
environment variable when
running
[ npx convex deploy](/cli#deploy-convex-functions-to-production).

### Typical team development workflow[](#typical-team-development-workflow)

Teams developing on Convex usually follow this workflow:

- If this is the team's first project, one team member creates a team on the dashboard.
- One team member creates a project by running
`npx convex dev`
, perhaps starting with a[quickstart](/quickstarts)or a[template](https://www.convex.dev/templates). - The team member creates a Git repository from the initial code and shares it with their team (via GitHub, GitLab etc.).
- Other team members pull the codebase, and get their own dev deployments by
running
`npx convex dev`
. - All team members can make backend changes and test them out with their
individual dev deployments. When a change is ready the team member opens a
pull-request (or commits to a shared branch).
[Backup / Restore](//database/backup-restore)can be used to populate a dev deployment with data from a prod deployment.[Data import](/database/import-export/import)can be used to populate a dev deployment with synthetic seed data.- Members of a team with the
[Pro plan](https://www.convex.dev/plans)can get separate[preview deployments](/production/hosting/preview-deployments)to test each other's pull-requests.
- Deployment to production can happen
[automatically](/production/hosting/)when changes get merged to the designated branch (say`main`
).- Alternatively one of the team members can deploy to production manually by
running
`npx convex deploy`
.
- Alternatively one of the team members can deploy to production manually by
running

#### Making safe changes[](#making-safe-changes)

Especially if your app is live you want to make sure that changes you make to your Convex codebase do not break it.

Some unsafe changes are handled and caught by Convex, but others you need handle yourself.

**Schema must always match existing data.**Convex enforces this constraint. You cannot push a schema to a deployment with existing data that doesn't match it, unless you turn off schema enforcement. In general it safe to:- Add new tables to the schema.
- Add an
`optional`
field to an existing table's schema, set the field on all documents in the table, and then make the field required. - Mark an existing field as
`optional`
, remove the field from all documents, and then remove the field. - Mark an existing field as a
`union`
of the existing type and a new type, modify the field on all documents to match the new type, and then change the type to the new type.
**Functions should be backwards compatible.**Even if your only client is a website, and you deploy it together with your backend, your users might still be running the old version of your website when your backend changes. Therefore you should make your functions backwards compatible until you are OK to break old clients. In general it is safe to:- Add new functions.
- Add an
`optional`
named argument to an existing function. - Mark an existing named argument as
`optional`
. - Mark an existing named argument as a
`union`
of the existing type and a new type. - Change the behavior of the function in such a way that given the arguments from an old client its behavior will still be acceptable to the old client.
**Scheduled functions should be backwards compatible.**When you schedule a function to run in the future, you provide the argument values it will receive. Whenever a function runs, it always runs its currently deployed version. If you change the function between the time it was scheduled and the time it runs, you must ensure the new version will behave acceptably given the old arguments.

---