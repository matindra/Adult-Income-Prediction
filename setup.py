from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requriments(filepath: str) -> List[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ i.replace("\n", "") for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(name='Adult Income Prediction',
      version='0.0.1',
      description='Adult Income Prediction ML pipeline project',
      author='Matindra Malik',
      author_email='matindramalik@gmail.com',
      url='https://matindra.github.io/',
      packages=find_packages(),
      install_requires = get_requriments("requirements.txt")
     )
