from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "toCase",
    version = "1.1.2",
    description = "toCase is a Case converter.",
    url = "https://github.com/RickBarretto/toCase",
    author = "Rick Barretto",
    author_email = "pdant.mailme@protonmail.ch",
    license = "MIT License",
    packages=['toCase', 're'],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Topic :: Text Editors :: Text Processing",
        "Topic :: Text Editors :: Word Processors",
        "Topic :: Text Processing"
    ]
)