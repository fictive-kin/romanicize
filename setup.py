import os
import setuptools


def readme():
    path = os.path.dirname(__file__)
    with open(os.path.join(path, "README.rst")) as f:
        return f.read()


name = "romanicize"
description = "Roman Numeral Conversion Utilities"
version = "0.1.2"
author = "Fictive Kin LLC"
email = "hello@fictivekin.com"
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development",
]

if __name__ == "__main__":
    setuptools.setup(
        name=name,
        version=version,
        description=description,
        long_description=readme(),
        classifiers=classifiers,
        url="https://github.com/fictive-kin/romanicize",
        author=author,
        author_email=email,
        maintainer=author,
        maintainer_email=email,
        license="MIT",
        python_requires=">=3.6",
        packages=[
            "romanicize",
        ],
        scripts=[
            "bin/romanicize",
        ],
    )
