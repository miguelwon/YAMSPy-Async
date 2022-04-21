import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 7):
    sys.exit('Sorry, Python < 3.7 is not supported.')

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="yamspy_async",
    packages=[package for package in find_packages()],
    version="0.3.3",
    license="GPL",
    description="Fork of YAMSPY where async was added",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="",
    author_email="",
    url="https://github.com/miguelwon/YAMSPy-Async",
    download_url="https://github.com/miguelwon/YAMSPy-Async/archive/refs/heads/master.zip",
    keywords=['CogniFly', 'Betaflight', 'iNAV', 'drone', 'UAV', 'Multi Wii Serial Protocol', 'MSP'],
    install_requires=['pyserial','asyncio','aioserial','approxeng.input'],
    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Framework :: Robot Framework :: Library',
          'Topic :: Education',
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ]
)
