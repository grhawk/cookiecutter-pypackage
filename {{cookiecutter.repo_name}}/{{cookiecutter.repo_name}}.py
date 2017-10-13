#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "{{ cookiecutter.full_name }}"
__version__ = "{{ cookiecutter.version }}"
__email__ = "{{ cookiecutter.email }}"

import argparse
import logging
import {{ cookiecutter.repo_name }}

import {{ cookiecutter.repo_name }}.module_1

asd1.logger_setup()
log = logging.getLogger('main')


def main(args):
    """ Main entry point of the app """
    {{ cookiecutter.repo_name }}.module_1.simple() # test the logging
    return "Do some magic!"


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument("-v", "--verbose",
                        action="count",
                        default=0,
                        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument("--version",
                        action="version",
                        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
