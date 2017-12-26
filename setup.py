from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name='react-flask-template',
    version=__version__,
    author='Ben Wu',
    url='https://github.com/Ben-Wu/react-flask-template',
    packages=find_packages(),
    install_requires=[
        'Flask==0.12.2',
    ]
)
