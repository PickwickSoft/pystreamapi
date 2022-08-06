from setuptools import setup

setup(
    name='pystreamapi',
    version='0.1',
    packages=['pystreamapi'],
    package_dir={'': 'tests'},
    url='https://github.com/PickwickSoft/pystreamapi',
    license=' GPL-3.0',
    author='Stefan Garlonta',
    author_email='stefan@pickwicksoft.org',
    description='A stream library for Python inspired by Java Stream API.',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"]
)
