import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

install_requires = [
    "spotipy==2.13.0",
    "requests==2.24.0",
    "youtube_title_parse==1.0.0",
    "lxml==4.5.2",
    "beautifulsoup4==4.9.1",
    "google_api_python_client==1.10.0",
    "pytest==6.0.1",
    "python-dotenv==0.14.0",
    "python_dateutil==2.8.1",
]

tests_require = ["pytest==6.0.1"]

# This call to setup() does all the work
setup(
    name="music_metadata_extractor",
    version="1.3.2",
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
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points={"console_scripts": []},
)
