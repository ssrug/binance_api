from setuptools import setup, find_packages

setup(name='binance_api',
      version='0.0.1',
      description='python package to access the binance api',
      author='EasyAI, ssrug',
      url='https://github.com/ssrug/binance_api',
      packages=['binance_api'],
      install_requires=[
          'numpy',
          'requests',
          'websocket-client'
        ]
      )
