Name:		python-gevent
Version:	24.11.1
Release:	1
Summary:	Coroutine-based network library
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/gevent/
Source0:	gevent-24.11.1.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(,
     # python 3.7 requires at least 0.4.14, which is abi incompatible with earlier
     # releases. python 3.9 and 3.10 require 0.4.16;
     # 0.4.17 is abi incompatible with earlier releases, but compatible with 1.0
     # 1.1.3 is needed for cpython 3.11.
     # 2.0 is not abi compatible with earlier releases, but with luck it won)
BuildRequires:	python%{pyver}dist(greenlet)
BuildRequires:	gcc
BuildRequires:	lib64python-devel
BuildRequires:	python%{pyver}dist(zope.event)
BuildRequires:	python%{pyver}dist(zope.interface)
%description
Coroutine-based network library.

%files
%{python_sitearch}/*
