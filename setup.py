from setuptools import *

setup(
    name = "toCase",
    version = "1.2.3",
    description = "toCase is a Case converter.",
    long_description = "toCase is a Case converter made in python, for peoples who wants simplify this feature. It can convert to and from Camel, Pascal, Snake, Kebab and Strings Sentences. And, You don't need say what is the input type, the code parse it. Just say whats is the output type.",
    url = "https://github.com/RickBarretto/toCase",
    author = "Rick Barretto",
    author_email = "pdant.mailme@protonmail.ch",
    license = "MIT License",
    packages=["toCase"],

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