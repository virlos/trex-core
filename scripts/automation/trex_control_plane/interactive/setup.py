"""A setup module for Trex interactive client.

See:
https://trex-tgn.cisco.com/ and
https://trex-tgn.cisco.com/trex/doc/cp_stl_docs/api/index.html
"""

import setuptools
import os

setuptools.setup(
    name="trex_client",
    version="2.61",
    description="Control API for Trex traffic generator.",
    author="Cisco Systems Inc. and/or its affiliates",
    author_email="trex-tgn@googlegroups.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Networking"
    ],
    keywords="traffic generator networking",
    packages=setuptools.find_packages(
        exclude=['trex_stl_lib', '*docs*', '*examples*', '*test*']),
    install_requires=[
        'PyYAML',
        'dpkt',
        'pyzmq-ctypes',
        'repoze.lru',
        'scapy',
        'simpy',
        'texttable',
    ],
    project_urls={
        "Source": "https://github.com/cisco-system-traffic-generator/trex-core",
    },
)
