#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "{{ cookiecutter.full_name }}"
__version__ = "{{ cookiecutter.version }}"
__email__ = "{{ cookiecutter.email }}"

from {{ cookiecutter.repo_name }} import Logger
log = Logger().setup()

log.warning('Testing log')


if __name__ == '__main__':
    print('Do something special!')
