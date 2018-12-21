from distutils.core import setup

setup(
    # Application name:
    name="Beauteous",

    # Version number (initial):
    version="1.4.3",

    # Application author details:
    author="Lucas Thoresen",
    author_email="reoky@tuta.io",

    # Packages
    packages=["beauteous"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/beauteous/",
    download_url = 'https://github.com/reoky/beauteous',
    #
    # license="LICENSE.txt",
    description="Colors the terminal in many beauteous fashions with the codes of ANSI.",

    # Dependent packages (distributions)
    install_requires=[
        "binascii",
    ],
)