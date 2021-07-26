from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='dlist_top',
    version='0.1.0',
    description='DList.top client for Python',
    long_description=readme,
    author='DList.top',
    # author_email='',
    url='https://github.com/dlist-top/client-py',
    # license=license,
    packages=find_packages(where='dlist_top', exclude=('example'))
)
