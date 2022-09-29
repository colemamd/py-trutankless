"""Setup for pytrutankless."""
from setuptools import find_packages, setup

from pytrutankless import __version__

LONG_DESC = open("README.md").read()
PACKAGES = find_packages(exclude=["dist", "*.test", "*.test.*", "test"])
REQUIREMENTS = list(val.strip() for val in open("requirements.txt"))
MIN_PY_VERSION = "3.8"

setup(
    name="pytrutankless",
    version=__version__,
    description="A Python client library for the TruTankless API",
    license="MIT",
    url="https://github.com/colemamd/pytrutankless",
    download_url="https://github.com/CyanBook/pytrutankless/releases/latest",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    author="Matt Coleman",
    author_email="mdcoleman001@gmail.com",
    install_requires=REQUIREMENTS,
    packages=PACKAGES,
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    project_urls={
        "Source": "https://github.com/colemamd/pytrutankless",
        "Bug Reports": "https://github.com/colemamd/pytrutankless/issues",
        "Release Notes": "https://github.com/colemamd/pytrutankless/releases/)",
    },
)
