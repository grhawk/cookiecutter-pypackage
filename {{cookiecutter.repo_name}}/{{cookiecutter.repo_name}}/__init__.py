__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

import os
import logging.config

import yaml


class Logger:
    log = False

    def __setup(self,
              default_path='../logging.yaml',
              default_level=logging.INFO,
              env_key='LOG_CFG'):
        """Setup logging configuration

        """
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)

        self.log = logging.getLogger()
        return self.log

    def setup(self,
              default_path='../logging.yaml',
              default_level=logging.INFO,
              env_key='LOG_CFG'):
        if self.log:
            return self.log
        else:
            return self.__setup(default_path=default_path,
                               default_level=default_level,
                               env_key=env_key)
