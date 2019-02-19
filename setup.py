#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0',
                'folium>=0.6.0',
                'geopy>=1.17.0',
                'ip2geotools>=0.1.3',
                'kneed>=0.2.4',
                'scipy>=1.1.0',
                'sklearn>=0.0'
                ]

setup_requirements = None

test_requirements = None

setup(
    author="Oldřich Klíma",
    author_email='xklima27@vutbr.cz',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                ],
    description="""An extension of the ip2geotools package that refines
                the estimation of the location of different geolocation databases using statistical 
                methods.""",
    entry_points={'console_scripts': ['ip2geotools_locator=ip2geotools_locator.cli:main']},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ip2geotools_locator',
    name='ip2geotools_locator',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Ionicson/ip2geotools-locator',
    version='1.1.3',
    zip_safe=False,
)
