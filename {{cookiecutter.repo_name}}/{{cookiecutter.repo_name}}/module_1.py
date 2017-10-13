#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "{{ cookiecutter.full_name }}"
__version__ = "{{ cookiecutter.version }}"
__email__ = "{{ cookiecutter.email }}"

import logging
log = logging.getLogger('main')

# Do not put log at this level. Could not work properly.

def simple():
    log.warning('Testing log')


if __name__ == '__main__':
    print('Do something special!')
