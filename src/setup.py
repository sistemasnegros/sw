#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup  
  
setup(name="sw",  
      version="0.1",  
      description="This tool highlights with colors the console output by applying regular expressions on Hostname, Domain, Ip, Mac, Emails, Success and Error.",  
      author="Kevin Franco",  
      author_email="sistemasnegros@gmail.com",  
      url="https://github.com/sistemasnegros/sw",  
      license="GPL",  
      scripts=["sw.py"],
      #install_requires = ["argparse"]
      packages = find_packages()   
)  