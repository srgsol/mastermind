from setuptools import setup, find_packages

setup(
    name='mastermind',
    version='0.0.0',
    description='Mastermind',
    author='Sergi Soler i Segura',
    author_email='',
    license="Apache 2.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'mastermind=mastermind.main:main'
        ]
    }
)