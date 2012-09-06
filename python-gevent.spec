%define module	gevent
%define name	python-%{module}
%define version	0.13.8
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %rel
%else
%define release	%rel
%endif

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A coroutine-based Python networking library

Group:		Development/Python 
License:	MIT
URL:		http://www.gevent.org/
Source0:	http://pypi.python.org/packages/source/g/%{module}/%{module}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	python-greenlet
BuildRequires:  python-greenlet, python-devel, python-setuptools, python-sphinx
BuildRequires:	libevent-devel >= 1.4.0

%description
gevent is a coroutine-based Python networking library that uses greenlet to
provide a high-level synchronous API on top of libevent event loop.

Features include:

* Fast event loop based on libevent.
* Lightweight execution units based on greenlet.
* Familiar API that re-uses concepts from the Python standard library.
* Cooperative sockets with ssl support.
* DNS queries performed through libevent-dns.
* Ability to use standard library and 3rd party modules written for
  standard blocking sockets
* Fast WSGI server based on libevent-http.

gevent is inspired by eventlet but features a more consistent API, a simpler 
implementation, and better performance. 

%prep
%setup -q -n %{module}-%{version}

%build
PYTHONDONTWRITEBYTECODE= CFLAGS="%{optflags}" %{__python} setup.py build

pushd doc
export PYTHONPATH=`dir -1d ../build/lib.linux*`
make html
rm -rf _build/html/.buildinfo 
popd

%install
%__rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Fix non-standard-executable-perm error
%{__chmod} 0755 %{buildroot}%{python_sitearch}/%{module}/core.so

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS changelog.rst LICENSE* README* TODO examples/ doc/_build/html/
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}-*.egg-info
