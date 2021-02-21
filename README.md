[![Build Status](https://travis-ci.org/pescobar/cookiecutter-ansible-role-molecule.svg?branch=master)](https://travis-ci.org/pescobar/cookiecutter-ansible-role-molecule)

# Cookiecutter template for ansible roles

Template for ansible role with [molecule](https://molecule.readthedocs.io/en/latest/) testing

## Requirements

The template itself only needs python, [cookicuter](https://cookiecutter.readthedocs.io/) and [pre-commit](https://pre-commit.com/). Install them doing `pip install cookiecutter pre-commit`

## What this template provides?

* Initialize a new git repo in the local machine
* Add [.yamllint](https://github.com/adrienverge/yamllint) config file (used by molecule)
* Add .pre-commit-config.yaml used by [pre-commit](http://pre-commit.com/)
* Add .gitignore with common files I don't want to track in git
* Add configuration for [Molecule](http://molecule.readthedocs.io) in the "molecule" folder
  * default molecule scenario runs on docker + debian10/systemd image
* And probably something else that I forget... :)

## Usage

### To initialize the role with cookiecuter
```
$ pip install cookiecutter pre-commit
$ cookiecutter gh:nekeal/cookiecutter-ansible-role-molecule
```

### To test the default scenario docker + debian10/systemd image
```
$ molecule test
```

## Directory structure
```
ansible-role-example/
├── defaults
│   └── main.yml
├── .gitignore
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── molecule
│   ├── default
│   │   ├── converge.yml
│   │   ├── INSTALL.rst
│   │   ├── molecule.yml
│   │   └── verify.yml
├── .pre-commit-config.yaml
├── README.md
├── tasks
│   └── main.yml
├── vars
│   └── main.yml
└── .yamllint
```
