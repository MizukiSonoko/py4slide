from setuptools import setup, find_packages

requires = ['colorama']

NAME = 'py4slide'

VER  = '0.0.1'

setup(
    name=NAME,
    version=VER,
    description='slide application by python.',
    author='Sonoko Mizuki',
    url='http://mizuki.co/',
    license='BSD',
    install_requires=requires,
    packages=[NAME]
)
