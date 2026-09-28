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
BuildRequires:	python%{pyver}dist(greenlet)
BuildRequires:	gcc
BuildRequires:	lib64python-devel
BuildRequires:	python%{pyver}dist(zope.event)
BuildRequires:	python%{pyver}dist(zope.interface)

%prep -a
# Bundled libev's configure fails dependency tracking under clang.
sed -i 's|sh ./configure -C|sh ./configure -C --disable-dependency-tracking|' _setuplibev.py

%description
Coroutine-based network library.

%files
%{python_sitearch}/*
