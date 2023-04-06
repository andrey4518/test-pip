from setuptools import setup, find_packages

setup(
    name='test_pip',
    version='0.0.2',
    install_requires=[
        "protobuf==4.22.1"
    ],
    packages=find_packages(
        # All keyword arguments below are optional:
        where='proto',  # '.' by default
        # include=['mypackage*'],  # ['*'] by default
        # exclude=['mypackage.tests'],  # empty by default
    ),
)