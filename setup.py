import os
from setuptools import setup, find_packages
from distutils.core import setup

# Utility function to read the README file.

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "domain_adaptability",
	version = "1.35",
	author = "Dainis Boumber",
	author_email = "dainis.boumber@gmail.com",
	description = ("Measuring domain adaptability in Python"),
	license = "GNU GENERAL PUBLIC LICENSE v3",
	url = "https://github.com/dainis-boumber/domain_adaptability",
	keywords = "domain adaptation, natural language processing, computational linguistics, corpus, corpora, similarity",
	packages = find_packages(exclude=["*.pyc", "__pycache__"]),
	package_data={'': ['domain_adaptability.in_domain_features.*', 'domain_adaptability.out_of_domain_features.*', 'domain_adaptability.threshold_values.*']},
	install_requires=[
			"cytoolz",
			"numpy",
			"clean-text",
			"scipy",
			"scikit-learn",
			"pandas",
			],
	include_package_data=True,
	long_description=read('README.md'),
    	long_description_content_type='text/markdown',
	)
