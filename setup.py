import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "kapitools",
    version = "0.0.1",
    author = "Simon Schroeter",
    author_email = "simon.schroeter@gmail.com",
    description = ("Caculate KapiRegnums producing rate using "
                   "webservice at http://www.kapitools.de."),
    license = "GPLv3",
    keywords = "kapi regnum kapitools network parse",
    packages=["kapitools"],
    install_requires=["requests>=2.0", "beautifulsoup4>=4.0"],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Text Processing :: Markup :: HTML",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
