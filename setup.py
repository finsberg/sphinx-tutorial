from setuptools import setup, find_packages

NAME = 'myproject'
VERSION = '1.0'
AUTHORS = 'Henrik Finsberg'

setup(name=NAME,
      description='Dummy package for this tutorial',
      version=VERSION,
      author=AUTHORS,
      license='LGPL version 3 or later',
      author_email="henrikn@simula.no",
      packages=find_packages("."))
# package_dir={"mps": "mps"},

