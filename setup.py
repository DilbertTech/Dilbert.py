import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dilbert", # Replace with your own username
    version="1.0.0",
    author="John Atkinson",
    description="A Python library for the Dilbert comic strip.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DilbertTech/Dilbert.py",
    packages=setuptools.find_packages(),
    install_requires=["install", "requests", "BeautifulSoup4", "randomtimestamp"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)