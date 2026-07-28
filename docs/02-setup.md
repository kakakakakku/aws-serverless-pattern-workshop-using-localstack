# Chapter 2: Set Up Your Workshop Environment

## GitHub Codespaces

To keep the setup effort as low as possible and give everyone an identical environment, this workshop uses [GitHub Codespaces](https://github.com/features/codespaces). GitHub Codespaces is an online **VS Code (Visual Studio Code)** environment tied to a GitHub repository.

Open this GitHub repository and press the `.` (dot) keyboard shortcut. GitHub Codespaces should launch automatically.

## LocalStack

The [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/), which you use to operate LocalStack, is already set up in GitHub Codespaces.

> [!WARNING]
> LocalStack changed its license in March 2026 and now requires account registration and an auth token. There is a Hobby plan for personal use, but commercial use requires a paid plan (Base or higher). This workshop uses **LocalStack v4.14.0** — the last version published as open source — so that you can use LocalStack without registering an account. You will see a warning when starting LocalStack, which is safe to ignore. For details about the license change, see the official blog post:
> https://blog.localstack.cloud/the-road-ahead-for-localstack/

To start LocalStack, first select `Terminal` → `New Terminal` from the menu (the three-line icon) on the left side of GitHub Codespaces. Then choose `Continue Working in GitHub Codespaces` → `2 cores, 8 GB RAM, 32 GB storage`. GitHub Codespaces is available on the GitHub Free plan.

See [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces) for details.

> [!NOTE]
> You can check your GitHub Codespaces usage on the [Billing summary](https://github.com/settings/billing/summary) page.

> [!NOTE]
> Right after startup, you will see a terminal showing a `👋 Welcome to Codespaces!` message. Wait a moment, and it will automatically switch to a new terminal without that message.

Then run the following commands. If `localstack status` finally shows **✔ running**, the LocalStack startup is complete. It is fine if the other fields, such as `id` and the date, differ.

```sh
$ localstack --version
LocalStack CLI 4.14.0

$ localstack start -d
$ localstack status
┌─────────────────┬───────────────────────────────────────────────────────┐
│ Runtime version │ 4.14.0                                                │
│ Docker image    │ tag: 4.14.0, id: 3ebc37595918, 📆 2026-02-26T10:27:36 │
│ Runtime status  │ ✔ running (name: "localstack-main", IP: 172.17.0.2)   │
└─────────────────┴───────────────────────────────────────────────────────┘
```

> [!NOTE]
> Wait a moment for LocalStack to start up.

## AWS CLI

The AWS CLI is also preinstalled in GitHub Codespaces. Run `aws configure` to set up access keys for LocalStack. As the `DUMMY` values suggest, placeholder values are perfectly fine.

```sh
$ aws configure
AWS Access Key ID [None]: DUMMY
AWS Secret Access Key [None]: DUMMY
Default region name [None]: us-east-1
Default output format [None]: json
```

> [!NOTE]
> The LocalStack AWS CLI (`awslocal`) and the LocalStack AWS SAM CLI (`samlocal`) are also preinstalled.

## LocalStack Resource Browser

LocalStack has a feature called the [Resource Browser](https://docs.localstack.cloud/aws/capabilities/web-app/resource-browser/). Although its functionality and design differ from the AWS Management Console, it lets you inspect and operate the resources deployed to LocalStack.

> [!WARNING]
> Due to the license change, the Resource Browser is no longer available with LocalStack v4.14.0. This workshop therefore uses the AWS CLI for all resource verification.

## Resuming the Workshop Later

You can go through this workshop in one sitting, or a little bit every day. Here is how to resume the workshop on a different day after setting up the environment in Chapter 2.

To resume your existing GitHub Codespaces environment, open this GitHub repository and press the `,` (comma) keyboard shortcut, then select `Resume this codespace`.

The environment you set up is still there, but the LocalStack process itself will have stopped. So the only step you need to run again is starting LocalStack:

```sh
$ localstack start -d
```

That's it for Chapter 2! ✋

**Next: [Chapter 3: Process Images](03-image-processing.md)**
