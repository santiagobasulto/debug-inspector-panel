import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="inspector_panel",
    version="0.0.1",
    author="Santiago Basulto",
    author_email="santiago.basulto@gmail.com",
    description=("A django-debug-toolbar panel to get more information about "
                                "your variables when developing django apps."),
    license="MIT",
    keywords="debugger django-debug-toolbar panels",
    url="https://github.com/santiagobasulto/debug-inspector-panel",
    packages=['inspector_panel', 'inspector_panel.panels'],
    package_data={'inspector_panel': ['templates/*', ]},
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Topic :: Utilities",
        "Topic :: Software Development :: Debuggers",
        "License :: OSI Approved :: MIT License",
    ],
    tests_require=["Django>=1.1"],
    test_suite='runtests.runtests'
)
