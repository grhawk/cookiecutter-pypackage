#!/usr/bin/env python3
"""Module Docstring just to try!


"""

__author__ = "{{ cookiecutter.full_name }}"
__version__ = "{{ cookiecutter.version }}"
__email__ = "{{ cookiecutter.email }}"

import logging
log = logging.getLogger('main')

# Do not put log at this level. Could not work properly.

def simple(optional=None):
    """Just a simple function to test logging.

    There is nothing to say about examples.

    Args:
        optional: A dummy argument to create this entry.

    Return:
        None and only none.

    TODO: something decent.

    """

    log.warning('Testing log')


if __name__ == '__main__':
    print('Do something special!')
