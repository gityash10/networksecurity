'''
the setup.py file is an essential file of packaging and distributing a Python project. 
It is used by setuptools (or distutils in older python versions) to define 
the configuration for the package or project, such as its metadata, dependencies, and other settings.'''

from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str = 'requirements.txt') -> List[str]:
    """this function will return list of requirements from the given file path"""
    requirement_lst: List[str] = []
    try:
        with open(file_path, 'r') as file:
            # process each line and drop comments/editable entries
            for line in file:
                requirement = line.split('#', 1)[0].strip()
                if requirement and not requirement.startswith('-e'):
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print(f"requirements file not")
    return requirement_lst

setup(
    name='networks_security',
    version='0.0.1',
    author='Yash',
    description='A package for network security project',
    author_email="yashh.jain24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
 