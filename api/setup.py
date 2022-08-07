from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='backend',
    version='1.0',
    description='Simple portfolio api',
    license="MIT",
    author='Azalurg',
    url="https://azalurg.github.io/",
    install_requires=requirements
)
