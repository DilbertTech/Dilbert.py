import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="dilbert",
    version="1.0.0",
    description="Get the latest Dilbert comics.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DilbertTech/Dilbert.py",
    author="John Atkinson",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["dilbert"],
    include_package_data=True,
    install_requires=["requests", "BeautifulSoup4", "randomtimestamp"],
)