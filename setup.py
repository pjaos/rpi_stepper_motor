import setuptools

MODULE_NAME    = "smotor"                                                       # The python module name
VERSION        = "1.0"                                                          # The version of the application
AUTHOR         = "Paul Austen"                                                  # The name of the applications author
AUTHOR_EMAIL   = "pausten.os@gmail.com"                                         # The email address of the author
DESCRIPTION    = "Basic control of a stepper motor on a Raspberry Pi platform." # A short description of the application
LICENSE        = "MIT License"                                                  # The License that the application is distributed under
REQUIRED_LIBS  = ['p3lib>=1.1.29', 'pigpio']                                              # A python list of required libs (optionally including versions)
STARTUP_SCRIPTS= ['scripts/smotor']                                             # The command line startup scripts to be installed.

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=MODULE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description="",                                                        #This will be read from the README.md file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: %s" % (LICENSE),
        "Operating System :: OS Independent",
    ],
    install_requires=[
        REQUIRED_LIBS
    ],
    scripts=STARTUP_SCRIPTS
)
