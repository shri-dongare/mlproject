from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.strip() for req in requirements]
        print("Before:", requirements)
        if HYPEN_E_DOT in requirements:
          requirements.remove(HYPEN_E_DOT)

        print("After:", requirements)

    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='shri-dongare',
    author_email='dongares666@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)