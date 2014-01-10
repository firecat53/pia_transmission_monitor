#!/usr/bin/env python
"""This file is part of pia_transmission_monitor.

The MIT License (MIT)

Copyright 2013 by Scott Hansen <firecat4153 @gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
from distutils.core import setup

setup(name="PIA Transmission Port Forwarding Monitor",
      version="0.1",
      description=("Update transmission forwarded port and bound IP address "
                   "when using privateinternetaccess.com VPN"),
      long_description=open('README.rst').read(),
      author="Scott Hansen",
      author_email="firecat4153@gmail.com",
      url="https://github.com/firecat53/pia_transmission_monitor",
      scripts=['bin/pia_transmission_monitor'],
      data_files=[('share/doc/pia_transmission_monitor',
                   ['README.rst', 'LICENSE.txt', 'config.ini.sample'])],
      classifiers=['Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 2.7',
                   'Operating System :: POSIX :: Linux',
                   'License :: OSI Approved :: MIT License',
                   'Development Status :: 4 - Beta',
                   'Environment :: No Input/Output (Daemon)',
                   'Topic :: System :: Networking'],
      license="MIT")
