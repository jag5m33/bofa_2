from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    this function will reeturn the list of requirements 
    '''
    requirements = [] # generate it as a list 
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # when you read lines and move ot the next \n (new line) gets added, you want to remove this 
        requirements=[req.replace('\n', '') for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements
setup(
    name = 'bofa_v2',
    version = '0.0.1',
    author = 'jag',
    author_email = 'jag5m33@gmail.com',
    packages = find_packages(), 
    install_requires = get_requirements('requirements.txt')

)