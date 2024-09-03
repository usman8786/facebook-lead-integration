from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in facebook_lead_integration/__init__.py
from facebook_lead_integration import __version__ as version

setup(
	name='facebook_lead_integration',
	version=version,
	description='Automatically create and manage Facebook leads in Frappe/ERPNext with seamless integration and real-time data capture.',
	author='Muhammad Usman',
	author_email='usman.mushtaq8786@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
