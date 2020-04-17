import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="music_metadata_extractor",
    version="1.0.0b1",
    description="Fetch music metadata from common Music APIs for a variety of data sources",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lttkgp/metadata-extractor",
    author="lttkgp",
    author_email="ghostwriternr@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": []
    },
)
