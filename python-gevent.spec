%define module	gevent

Summary:	A coroutine-based Python networking library


Name:		python-%{module}
Version:	1.0.1
Release:	1
Group:		Development/Python 
License:	MIT
Url:		http://www.gevent.org/
Source0:	http://pypi.python.org/packages/source/g/gevent/gevent-%{version}.tar.gz

BuildRequires:  python-greenlet
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(python)
Requires:	python-greenlet

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
%setup -qn %{module}-%{version}

%build
PYTHONDONTWRITEBYTECODE= CFLAGS="%{optflags}" python setup.py build

pushd doc
export PYTHONPATH=`dir -1d ../build/lib.linux*`
make html
rm -rf _build/html/.buildinfo 
popd

%install
python setup.py install -O1 --skip-build --root %{buildroot}

# Fix non-standard-executable-perm error
chmod 0755 %{buildroot}%{py_platsitedir}/%{module}/core.so

%files
%doc AUTHORS changelog.rst LICENSE* README* TODO examples/ doc/_build/html/
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-%{version}-*.egg-info



