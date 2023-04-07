from setuptools import setup, find_packages

setup(
    name='test_pip',
    version='0.0.5',
    install_requires=[
        "protobuf==4.22.1"
    ],
    # packages=find_packages(
    #     # All keyword arguments below are optional:
    #     # where='proto',  # '.' by default
    #     include=['proto*'],  # ['*'] by default
    #     # exclude=['mypackage.tests'],  # empty by default
    # ),
    packages=['test_pip.proto'],
    package_dir = {
        "test_pip.proto": "proto",
    },
    package_data={"test_pip.proto": ["*.proto"]},
    include_package_data=True
)