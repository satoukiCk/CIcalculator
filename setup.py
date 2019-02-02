from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    ld = fh.read()

setup(
    name="CIcalculator",
    version="0.0.1",
    author="cyw",
    author_email="",
    description="CI test with calculator",
    long_description=ld,
    long_description_content_type="text/markdown",
    url="https://github.com/satoukiCk/CIcalculator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT Lincense",
        "Operating System :: OS Independent"
    ],
)
