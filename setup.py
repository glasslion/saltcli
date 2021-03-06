#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pip
from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [str(req.req) for req in parse_requirements(
    'requirements/prod.txt',
    session=pip.download.PipSession()
)]

test_requirements = [str(req.req) for req in parse_requirements(
    'requirements/test.txt',
    session=pip.download.PipSession()
)]

extra_requirements = {
    'salt': [
        'salt >= 2015'
    ],
}

setup(
    name='saltcli',
    version='0.0.1',
    description="A CLI with autocompletion and syntax highlighting for salt commands.",
    long_description=readme + '\n\n' + history,
    author="Leo Zhou",
    author_email='glasslion@gmail.com',
    url='https://github.com/glasslion/saltcli',
    packages=[
        'saltcli',
    ],
    package_dir={'saltcli':
                 'saltcli'},
    include_package_data=True,
    install_requires=requirements,
    extra_requires=extra_requirements,
    entry_points={
        'console_scripts': 'saltcli = saltcli.main:cli'
    },

    license="ISCL",
    zip_safe=False,
    keywords='saltcli',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
