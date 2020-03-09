from setuptools import setup
import os

def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name='aioquery',
    version='0.0.2',
    description='Asynchronous wrapper for source query.',
    author='WardPearce',
    author_email='contact@districtnine.host',
    license='Apache License 2.0',
    packages=['aioquery'],
    install_requires=get_requirements(),
    zip_safe=False
)