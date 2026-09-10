# AA Memberaudit Dashboard.<a name="aa-memberaudit-dashboard"></a>

![Release](https://img.shields.io/pypi/v/aa-memberaudit-dashboard?label=release)
![Licence](https://img.shields.io/github/license/geuthur/aa-memberaudit-dashboard)
![Python](https://img.shields.io/pypi/pyversions/aa-memberaudit-dashboard)
![Django](https://img.shields.io/pypi/frameworkversions/django/aa-memberaudit-dashboard.svg?label=django)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Geuthur/aa-memberaudit-dashboard/master.svg)](https://results.pre-commit.ci/latest/github/Geuthur/aa-memberaudit-dashboard/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checks](https://github.com/Geuthur/aa-memberaudit-dashboard/actions/workflows/autotester.yml/badge.svg)](https://github.com/Geuthur/aa-memberaudit-dashboard/actions/workflows/autotester.yml)
[![codecov](https://codecov.io/gh/Geuthur/aa-memberaudit-dashboard/graph/badge.svg?token=B3BSovXASa)](https://codecov.io/gh/Geuthur/aa-memberaudit-dashboard)
[![Translation status](https://weblate.geuthur.de/widget/allianceauth/aa-memberaudit-dashboard/svg-badge.svg)](https://weblate.geuthur.de/engage/allianceauth/)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W810Q5J4)

Simple Dashboard Memberaudit Addon to display not registred Chars

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=1 -->

- [AA Memberaudit Dashboard.](#aa-memberaudit-dashboard)
  - [Introduce](#introduce)
  - [Features](#features)
  - [Installation](#installation)
    - [Step 1 - Install the Package](#step-1---install-the-package)
    - [Step 2 - Configure Alliance Auth](#step-2---configure-alliance-auth)
    - [Step 3 - Migrate App and collect static](#step-3---migrate-app-and-collect-static)
  - [Highlights](#highlights)
  - [Translations](#translations)
  - [Contributing](#contributing)

<!-- mdformat-toc end -->

## Introduce<a name="introduce"></a>

Everyone knows the issue that some people not register correctly now the members see on the Dashboard that something is wrong...

## Features<a name="features"></a>

- Show not registred Characters on Dashboard
- Member Audit Character Issue Checker

## Installation<a name="installation"></a>

> [!NOTE]
> AA MemberAudit Dashboard needs at least Alliance Auth v5
> Please make sure to update your Alliance Auth before you install this APP

### Step 1 - Install the Package<a name="step-1---install-the-package"></a>

Make sure you're in your virtual environment (venv) of your Alliance Auth then install the pakage.

```shell
pip install aa-memberaudit-dashboard
```

### Step 2 - Configure Alliance Auth<a name="step-2---configure-alliance-auth"></a>

Configure your Alliance Auth settings (`local.py`) as follows:

```python
INSTALLED_APPS = [
    # other apps
    "memberaudit",  # only if it not already existing
    "madashboard",
    # other apps?
]
```

### Step 3 - Migrate App and collect static<a name="step-3---migrate-app-and-collect-static"></a>

Migrate the app and collect static.

```shell
python manage.py migrate madashboard
python manage.py collectstatic --noinput
```

## Highlights<a name="highlights"></a>

![Screenshot 2024-07-05 093013](https://github.com/Geuthur/aa-memberaudit-dashboard/assets/761682/4fe45fc5-c260-4c9e-bc7a-29a6c9e8cdd1)

## Translations<a name="translations"></a>

[![Translations](https://weblate.geuthur.de/widget/allianceauth/aa-memberaudit-dashboard/multi-auto.svg)](https://weblate.geuthur.de/engage/allianceauth/)

Help us translate this app into your language or improve existing translations. Join our team!"

## Contributing<a name="contributing"></a>

You want to improve the project?
Please ensure you read the [Contribution Guidelines]

<!-- MD Links -->

[contribution guidelines]: https://github.com/Geuthur/aa-memberaudit-dashboard/blob/master/CONTRIBUTING.md "Contribution Guidelines"
