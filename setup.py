from setuptools import setup, find_packages
import sys
import os

version = '0.0'

setup(name='redshovel',
      version=version,
      description="Simple python rpc for redmine.",
      long_description="""\
A simple python rpc interface for redmine.""",
      # Get strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='',
      author='Russell Sim',
      author_email='russell.sim@gmail.com',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'requests',
          'PrettyTable'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      rs-issue = redshovel.issue:main
      """,
      )
