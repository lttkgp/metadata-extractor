import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

install_requires = [
    "beautifulsoup4==4.9.0",
    "lxml==4.5.0",
    "python-dotenv==0.12.0",
    "requests==2.23.0",
    "spotipy==2.10.0",
    "youtube-title-parse==1.0.0",
    "google-api-python-client==1.9.3",
    "google-auth-oauthlib==0.4.1",
    "google-auth-httplib2==0.0.3",
    "google-auth==1.18.0",
    "python-dateutil==2.8.1"
]

tests_require = ["pytest==5.4.1"]

# This call to setup() does all the work
setup(
    name="music_metadata_extractor",
    version="1.0.0",
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
