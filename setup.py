import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'py_arp',
    version = '0.0.1',
    author = 'Dane Morgan',
    author_email = 'danemorgan91@gmail.com',
    description = 'Quick and dirty arp scan, save results to a file',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/deadlift1226/py_arp',
    install_requires = ['colorama', 'scapy', 'requests', 'pprint'], #3rd party pip packages
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

