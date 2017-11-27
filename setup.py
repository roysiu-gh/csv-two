# Thank you to pypa for providing a template for this setup.py:
# https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages
# To use a consistent encoding
import os, codecs

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='CSV-Two',
    
    version='2.0.0',

    description='A CSV to SQL database converter',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/roysoup/csv-two',

    # Author details
    author='Roy Siu',
    author_email='roysiu@outlook.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='csv sql',
    
    packages=["csvtwo"],
    
    install_requires=[],
)