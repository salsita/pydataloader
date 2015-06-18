# [PyDataLoader](https://github.com/salsita/pydataloader) <a href='https://github.com/salsita'><img align='right' title='Salsita' src='https://www.google.com/a/cpanel/salsitasoft.com/images/logo.gif?alpha=1' /></a>

Extensible JSON/YAML/RAML/... data loader.

[![Latest Version](https://pypip.in/version/PyDataLoader/badge.svg)]
(https://pypi.python.org/pypi/PyDataLoader/)
[![Downloads](https://pypip.in/download/PyDataLoader/badge.svg)]
(https://pypi.python.org/pypi/PyDataLoader/)
[![Supported Python versions](https://pypip.in/py_versions/PyDataLoader/badge.svg)]
(https://pypi.python.org/pypi/PyDataLoader/)
[![License](https://pypip.in/license/PyDataLoader/badge.svg)]
(https://pypi.python.org/pypi/PyDataLoader/)


## Supported Platforms

* [Python](http://www.python.org/) >= 2.6, 3.3


## Get Started

Install using [pip](https://pip.pypa.io/) or [easy_install](http://pythonhosted.org/setuptools/easy_install.html):
```bash
pip install PyDataLoader
easy_install PyDataLoader
```

Optionally, you can specify `yaml` or `raml` extras to install related dependencies:
```bash
pip install "PyDataLoader[yaml,raml]"
easy_install "PyDataLoader[yaml,raml]"
```

## Features

- Load data stored in any of supported markup languages.
  - Support [YAML](http://yaml.org/) using [PyYAML](http://pyyaml.org/wiki/PyYAML).
  - Support [RAML](http://raml.org/) using [pyraml-parser](https://github.com/an2deg/pyraml-parser).
  - Support [JSON](http://json.org/) using [Python 2.6+ json module](https://docs.python.org/2/library/json.html), or [Python 3.x json module](https://docs.python.org/3/library/json.html).
- Allow extending supported markup languages.
- Allow extending with data postprocessing.

## Changelog

### 0.1.3

#### Fixes

- Update dependencies to support Python 3.
- Fix package setup on Python 3.

### 0.1.2

#### Fixes

- Fix Python 2.6 support.

### 0.1.1

#### Fixes

- Fix package setup to not require dependencies preinstalled.

### 0.1.0

#### Features

- Initial release.
