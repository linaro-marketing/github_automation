# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    install_requires=required,
    name='github_automation',
    version='0.1.0',
    description='This module makes basic GitHub tasks, like creating a pull request, easy. Built for the ConnectAutomation container',
    long_description=readme,
    author='Kyle Kirkby',
    author_email='kyle.kirkby@linaro.org',
    url='https://github.com/linaro-marketing/github_automation',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
