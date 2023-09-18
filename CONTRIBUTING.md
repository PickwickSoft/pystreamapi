# Contributing to pystreamapi

We are thrilled to have you here! You, the open source contributors, are what makes this project so great. We appreciate
all of your input and contributions to help make pystreamapi the best it can be.

## Ways to contribute

There are many ways to contribute to pystreamapi. Here is how you can help:

- [Report bugs and make feature requests by opening issues](#reporting-bugs-and-feature-requests)
- [Write code and fix/close existing issues](#contributing-code)
- [Improve documentation](#contributing-documentation)

## Important Resources

- [Issue Tracker](https://github.com/PickwickSoft/pystreamapi/issues): Report bugs and make feature requests
- [Documentation](https://pystreamapi.pickwicksoft.org/): Read the documentation
- [Project Board](https://github.com/orgs/PickwickSoft/projects/11): See the current development status
- [GitHub Discussions](https://github.com/PickwickSoft/pystreamapi/discussions): Ask questions and discuss ideas

## Reporting Bugs and Feature Requests

We use GitHub issues to track bugs and feature requests. Please ensure your bug description is clear and has sufficient
instructions to be able to reproduce the issue. If you are requesting a new feature, please explain why you think it is
needed and describe how it should work.

We already created prefilled templates for you to use when creating issues in order to improve the quality of the
information you provide.

Please do not use the issue tracker for personal support requests. Instead,
use [GitHub Discussions](https://github.com/PickwickSoft/pystreamapi/discussions/categories/q-a).

## Branches

The `main` branch is the stable branch. All development work should be done in a separate branch. When you are ready to
submit a pull request, please submit it against the `main` branch.

The `docs` branch is the branch used to build the documentation. It automatically updates the GitBook documentation when
a pull request is merged into it.

## Contributing Code

If you are interested in contributing code to pystreamapi, please follow these steps:

1. [Fork the repository and clone it](#fork-the-repository)
2. [Create a new branch for each feature or improvement](#create-a-new-branch)
3. [Install the development dependencies](#install-development-dependencies)
4. [Make your changes](#make-your-changes)
5. [Test and lint your code](#test-and-lint-your-code)
6. [Commit your changes](#commit-your-changes)
7. [Submit a pull request against the `main` branch]()
8. Wait for your pull request to be reviewed and merged

:tada: Congratulations! You have successfully contributed to pystreamapi!

### Fork the repository

You can fork the repository by clicking on the "Fork" button in the top right corner of the repository page or
by [clicking here](https://github.com/PickwickSoft/pystreamapi/fork). This will create a copy of the repository in your
own GitHub account.

If you need help with forking a repository, please refer to
the [GitHub documentation](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).

After you have forked the repository, you can [clone](https://help.github.com/articles/cloning-a-repository/) it to your
local machine.

### Create a new branch

Create a new branch for each feature or improvement you are working on. Please follow
our [branch naming conventions](https://github.com/PickwickSoft/conventions/blob/main/BRANCH_NAMING.md).

Create the branch from the `main` branch by running the following command:

```bash
git checkout -b BRANCH_NAME main
```

### Install development dependencies

Install Poetry if you haven't already by following the
instructions [here](https://python-poetry.org/docs/#installation).

Install the development dependencies by running the following command:

```bash
poetry install
```

Set poetry as the default interpreter for your project in your IDE. This will ensure that the correct dependencies are
used when running the project.

Alternatively, you can use the following command to activate the virtual environment:

```bash
poetry shell
```

### Make your changes

Make your changes to the code. Please follow the best practices and conventions for python development. You can find
them on the official style guide for python code: [PEP 8](https://www.python.org/dev/peps/pep-0008/).

### Test and lint your code

#### Testing

Before submitting a pull request, please make sure to write tests and lint the code.

All tests are located in the `tests` directory. Our tests can be executed
using [Coverage.py](https://coverage.readthedocs.io/).

To run the tests, execute the following command in the root directory of the project:

```bash
coverage run --source "pystreamapi/" -m unittest discover -s tests -t tests --pattern 'test_*.py'
```

To generate a coverage report, execute the following command and afterwards click on the link to open the report in your
browser:

```bash
coverage html && cd htmlcov/ && python3 -m http.server
```

Please make sure that all tests pass and the coverage of your code is 100% before submitting a pull request.

#### Linting

We use [pylint](https://www.pylint.org/) to lint our code. You can run pylint by executing the following command in the
root directory of the project after staging your changes:

```bash
pylint $(git ls-files '*.py')
```

Please make sure that your code passes the pylint checks before submitting a pull request.

### Commit your changes

We use gitmoji to add emojis to our commit messages. This helps us to quickly identify the purpose of a commit. You can
find the list of available emojis and their meaning [here](https://gitmoji.dev/).

Please follow this convention when writing commit messages:

```
:emoji: Short description of the change (less than 50 characters)

Longer (optional) description of the change (wrap at 72 characters)
```

Please describe your changes in detail in the commit message. This will help us to understand what you have changed and
why.

Also, always use the imperative, present tense: "change" not "changed" nor "changes".

Example:

```
:sparkles: Add data loader for CSV files
```

### Submit a pull request

Push your changes to your forked repository and submit a pull request against the `main` branch of the original
repository.

To push your changes to your forked repository, run the following command:

```bash
git push origin BRANCH_NAME
```

Afterward you can submit a pull request from the GitHub interface.

## Contributing Documentation

If you are interested in contributing to the documentation, please follow these steps:

1. [Fork the repository and clone it](#fork-the-repository)
2. Create a new branch from the `docs` branch by running the following command: `git checkout -b BRANCH_NAME docs`
3. [Add new documentation or update existing documentation](#add-new-documentation-or-update-existing-documentation)
4. [Commit your changes](#commit-your-changes)
5. [Submit a pull request against the `docs` branch](#submit-a-pull-request)

:tada: Congratulations! You have successfully contributed to the documentation of pystreamapi!

### Add new documentation or update existing documentation

The documentation is written in [Markdown](https://www.markdownguide.org/). You can find the documentation in the root
of the branch.

You can access the existing documentation [here](https://pystreamapi.pickwicksoft.org/).
