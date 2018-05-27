from setuptools import setup, find_packages

setup(
    name='painter-assistant',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='The painter assistant',
    long_description=open('README.md').read(),
    url='https://github.com/bartoszpogoda/academic-py-painter-assistant',
    author='Bartosz Pogoda',
    author_email='bartek.pogoda1@gmail.com'
)