============
Installation
============

You can run the program directly using the env.sh::

	$ source env.sh
	$ {{ cookiecutter.repo_name }}

At the command line either via easy_install or pip::

    $ easy_install {{ cookiecutter.repo_name }}
    $ pip install {{ cookiecutter.repo_name }}

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv {{ cookiecutter.repo_name }}
    $ pip install {{ cookiecutter.repo_name }}
