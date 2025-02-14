from setuptools import find_packages,setup    #to find the packges and setup used for metadata(name, version, authour for our data)
from typing import List  # for hint, the output will be in list format

HYPEN_E_DOT='-e .'   # creating a variable for installation of the packages in pip

# creating a function to get the requirement.txt folder.

def get_requirements(file_path: str)->List[str]: #file_path:str----expecting the filepath as string and output will in list format
    '''
    This function will return list of elements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='MLproject',
    version='0.0.1',
    description="secondendtoend",
    author='Prasdraj oddepogu',
    author_email='prasadrajoddepogu525@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
