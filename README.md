# Python Solar Plus Intelbras

[![Python package](https://github.com/hudsonbrendon/python-solar-plus-intelbras/actions/workflows/pythonpackage.yml/badge.svg?branch=main)](https://github.com/hudsonbrendon/python-solar-plus-intelbras/actions/workflows/pythonpackage.yml)
[![Upload Python Package](https://github.com/hudsonbrendon/python-solar-plus-intelbras/actions/workflows/python-publish.yml/badge.svg)](https://github.com/hudsonbrendon/python-solar-plus-intelbras/actions/workflows/python-publish.yml)
[![Dependabot Updates](https://github.com/hudsonbrendon/python-solar-plus-intelbras/actions/workflows/dependabot/dependabot-updates/badge.svg?branch=main)](https://github.com/hudsonbrendon/python-solar-plus-intelbras/actions/workflows/dependabot/dependabot-updates)
[![pages-build-deployment](https://github.com/hudsonbrendon/python-solar-plus-intelbras/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/hudsonbrendon/python-solar-plus-intelbras/actions/workflows/pages/pages-build-deployment)

A wrapper for api solar plus intelbras


Install using pip:


```shell
pip install solar-plus-intelbras
```

Now, let's get started:


```pycon
>>> from solar_plus_intelbras import SolarPlusIntelbras
>>> solar_plus_intelbras = SolarPlusIntelbras(email="test@email.com", plus="i2gH3zuE68ClMDop50h8OxKlOYjvWd0vCDACBtN9sEo")
>>> solar_plus_intelbras.records(plant_id=12345, period="day", key="energy_today", start_date="2025-01-01", end_date="2025-01-01")
```

## Features

Python Solar Plus Intelbras supports the main endpoints of the Intelbras API:

- Plants: return the list of plants of account;
- Records: return the records of especific range;
- Inverters: return the inverters of account;
- Alerts: return the alerts of account;
- Notifications: return the notifications of account.

## Documentation

Project documentation is available at [https://hudsonbrendon.github.io/python-solar-plus-intelbras/](https://hudsonbrendon.github.io/python-solar-plus-intelbras/).

## Contribute

If you want to contribute with Python Solar Plus Intelbras check out the Contributing Guide to learn how to start.

```shell
$ git clone git@github.com:hudsonbrendon/python-solar-plus-intelbras.git
```

```shell
$ cd python-solar-plus-intelbras
```

```shell
$ poetry install
```

### Run tests

```shell
$ pytest
```
Or running via vscode interface.

## Dependencies

The Python Solar Plus project relies on these excellent libraries:

- poetry - A manager for virtualenvs and dependencies;
- requests - A client for http requests;
- pytest - The best lib python for tests;
- python 3 - support for python >= 3.8.

<div align="center">

`python solar plus intelbras` is made with 💙 by the [@hudsonbrendon](https://github.com/hudsonbrendon) and distributed under [MIT License](LICENSE.md).




</div>
