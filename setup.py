from setuptools import setup, find_packages


description = 'New Relic extensions for Django'
long_desc = open('README.rst').read()

setup(
    name='django-newrelic-extensions',
    version='0.0.1',
    install_requires=[
        'newrelic'
    ],
    description=description,
    long_description=long_desc,
    author='SheepDogInc',
    author_email='development@sheepdoginc.ca',
    packages=find_packages()
)
