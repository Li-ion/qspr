from setuptools import setup, find_packages

setup_attrs = {
    'name': 'qspr',
    'description': 'Deep Learning toolkit for Computational Chemistry',
    'long_description': 'OpenChem',
    'long_description_content_type': "text/markdown",
    'url': '',
    'author': '',
    'author_email': '',
    'license': 'MIT',
    'packages': find_packages(),
    'include_package_data': True,
    'use_scm_version': True,
    'setup_requires': ['setuptools_scm'],
    'install_requires': [
        'tensorboard',
        'networkx',
        'tqdm',
        'torchani'
    ],
    'python_requires': ">=3.5",
    'zip_safe': False
}

setup(**setup_attrs)
