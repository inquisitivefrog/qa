
tim@Timothys-MacBook-Air scripts % pip3 install pytest
Defaulting to user installation because normal site-packages is not writeable
Collecting pytest
  Downloading pytest-8.4.1-py3-none-any.whl (365 kB)
     |████████████████████████████████| 365 kB 4.4 MB/s 
Collecting exceptiongroup>=1
  Downloading exceptiongroup-1.3.0-py3-none-any.whl (16 kB)
Collecting packaging>=20
  Downloading packaging-25.0-py3-none-any.whl (66 kB)
     |████████████████████████████████| 66 kB 5.2 MB/s 
Collecting iniconfig>=1
  Downloading iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Collecting pygments>=2.7.2
  Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
     |████████████████████████████████| 1.2 MB 4.9 MB/s 
Requirement already satisfied: tomli>=1 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest) (2.2.1)
Collecting pluggy<2,>=1.5
  Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Requirement already satisfied: typing-extensions>=4.6.0 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from exceptiongroup>=1->pytest) (4.14.1)
Installing collected packages: pygments, pluggy, packaging, iniconfig, exceptiongroup, pytest
Successfully installed exceptiongroup-1.3.0 iniconfig-2.1.0 packaging-25.0 pluggy-1.6.0 pygments-2.19.2 pytest-8.4.1
WARNING: You are using pip version 21.2.4; however, version 25.2 is available.
You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.
tim@Timothys-MacBook-Air scripts % which pytest 
/Users/tim/Library/Python/3.9/bin/pytest


tim@Timothys-MacBook-Air scripts % pip3 install pytest-mock
Defaulting to user installation because normal site-packages is not writeable
Collecting pytest-mock
  Downloading pytest_mock-3.14.1-py3-none-any.whl (9.9 kB)
Requirement already satisfied: pytest>=6.2.5 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest-mock) (8.4.1)
Requirement already satisfied: tomli>=1 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-mock) (2.2.1)
Requirement already satisfied: pluggy<2,>=1.5 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-mock) (1.6.0)
Requirement already satisfied: iniconfig>=1 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-mock) (2.1.0)
Requirement already satisfied: pygments>=2.7.2 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-mock) (2.19.2)
Requirement already satisfied: exceptiongroup>=1 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-mock) (1.3.0)
Requirement already satisfied: packaging>=20 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-mock) (25.0)
Requirement already satisfied: typing-extensions>=4.6.0 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from exceptiongroup>=1->pytest>=6.2.5->pytest-mock) (4.14.1)
Installing collected packages: pytest-mock
Successfully installed pytest-mock-3.14.1

tim@Timothys-MacBook-Air cli % pip3 install pytest-cov
Defaulting to user installation because normal site-packages is not writeable
Collecting pytest-cov
  Downloading pytest_cov-6.2.1-py3-none-any.whl (24 kB)
Requirement already satisfied: pluggy>=1.2 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest-cov) (1.6.0)
Requirement already satisfied: coverage[toml]>=7.5 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest-cov) (7.10.2)
Requirement already satisfied: pytest>=6.2.5 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest-cov) (8.4.1)
Requirement already satisfied: tomli in /Users/tim/Library/Python/3.9/lib/python/site-packages (from coverage[toml]>=7.5->pytest-cov) (2.2.1)
Requirement already satisfied: iniconfig>=1 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-cov) (2.1.0)
Requirement already satisfied: pygments>=2.7.2 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-cov) (2.19.2)
Requirement already satisfied: packaging>=20 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-cov) (25.0)
Requirement already satisfied: exceptiongroup>=1 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from pytest>=6.2.5->pytest-cov) (1.3.0)
Requirement already satisfied: typing-extensions>=4.6.0 in /Users/tim/Library/Python/3.9/lib/python/site-packages (from exceptiongroup>=1->pytest>=6.2.5->pytest-cov) (4.14.1)
Installing collected packages: pytest-cov
Successfully installed pytest-cov-6.2.1
WARNING: You are using pip version 21.2.4; however, version 25.2 is available.
You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.

tim@Timothys-MacBook-Air cli % pip3 show pytest pytest-mock pytest-cov
Name: pytest
Version: 8.4.1
Summary: pytest: simple powerful testing with Python
Home-page: 
Author: Holger Krekel, Bruno Oliveira, Ronny Pfannschmidt, Floris Bruynooghe, Brianna Laugher, Florian Bruhin, Others (See AUTHORS)
Author-email: 
License: MIT
Location: /Users/tim/Library/Python/3.9/lib/python/site-packages
Requires: pluggy, packaging, exceptiongroup, pygments, iniconfig, tomli
Required-by: pytest-mock, pytest-cov
---
Name: pytest-mock
Version: 3.14.1
Summary: Thin-wrapper around the mock package for easier use with pytest
Home-page: 
Author: 
Author-email: Bruno Oliveira <nicoddemus@gmail.com>
License: MIT
Location: /Users/tim/Library/Python/3.9/lib/python/site-packages
Requires: pytest
Required-by: 
---
Name: pytest-cov
Version: 6.2.1
Summary: Pytest plugin for measuring coverage.
Home-page: https://github.com/pytest-dev/pytest-cov
Author: Marc Schlaich
Author-email: marc.schlaich@gmail.com
License: MIT
Location: /Users/tim/Library/Python/3.9/lib/python/site-packages
Requires: pytest, pluggy, coverage
Required-by: 
tim@Timothys-MacBook-Air cli % 

