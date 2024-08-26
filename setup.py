"""
The module is used for setting up the repository with project details.
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.1.0"

REPO_NAME = "Google-PaLM-and-Langchain-based-QnA-System"
AUTHOR_USER_NAME = "sudhanshusinghaiml"
SRC_REPO = "src"
AUTHOR_EMAIL = "mailmeatss2112@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "."},
    packages=setuptools.find_packages()
)