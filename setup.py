from setuptools import setup, find_packages
import pathlib

# The directory containing this file
ROOOT = pathlib.Path(__file__).parent

# The text of the README file
README = (ROOOT / "README.md").read_text()

setup(
    name='loguru-logger-lite',
    version="0.0.1",
    author="Dmitry Amanov",
    author_email="",
    description="Simple logger built on top of loguru to make a quick setup for basic logging",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/doctor3030/loguru-logger-lite",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License"
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "setuptools>=57",
        "wheel",
        "loguru~=0.5.3",
        "kafka-python~=2.0.2"
    ]
)
