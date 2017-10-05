#!/usr/bin/env python
"""The setup and build script for the newsapi library."""

import codecs
import tweetemotion
from setuptools import setup, find_packages


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

with codecs.open('README.md', 'r', 'utf-8') as fd:
    setup(name='tweetemotion',
          version=tweetemotion.__version__,
          author='Nikhil Hegde',
          author_email='nikhilmhegde@gmail.com',
          license='LGPLv3',
          url='',
          keywords='indicio twitter emotion',
          description='Get emotion for tweets right away',
          long_description=fd.read(),
          packages=find_packages(exclude=['tests*']),
          install_requires=requirements(),
          include_package_data=True,
          classifiers=[
              'Development Status :: 5 - Production/Stable',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
              'Operating System :: OS Independent',
              'Topic :: Software Development :: Libraries :: Python Modules',
              'Topic :: Natural Language Processing :: Api',
              'Topic :: Data Analysis',
              'Programming Language :: Python :: 2.7',
          ],)