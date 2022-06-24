from setuptools import find_packages, setup

setup(
    name='irismodellib',
    packages=find_packages(include=['irismodel']),
    include_package_data=True,
    version='0.1.7',
    description='Library with a trained Iris ML predictor',
    author='AZ',
    license='MIT'
)