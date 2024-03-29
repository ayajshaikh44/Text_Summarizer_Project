import setuptools
from typing import List


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

hypen_obj = '-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
        This function is returns the list of requirements
    '''
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "" ) for req in requirements]

        if hypen_obj in requirements:
            requirements.remove(hypen_obj)
    return requirements 


__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer_Project"
AUTHOR_USER_NAME = "ayajshaikh44"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "ayajshaikh44@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"))
