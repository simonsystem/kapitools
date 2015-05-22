import os
from setuptools import setup

setup(
    name = "kapitools",
    version = "0.0.3",
    author = "Simon Schroeter",
    author_email = "simon.schroeter@gmail.com",
    description = ("Caculate KapiRegnums producing rate using "
                   "webservice at http://www.kapitools.de."),
    license = "GPLv3",
    keywords = "kapi regnum kapitools network parse",
    packages=["kapitools"],
    install_requires=["requests>=2.0", "beautifulsoup4>=4.0"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Text Processing :: Markup :: HTML",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
