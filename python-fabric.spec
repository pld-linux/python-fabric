# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		fabric
%define		egg_name	fabric
%define		pypi_name	fabric
Summary:	Execute shell commands remotely over SSH, yielding useful Python objects in return
Name:		python-%{module}
Version:	2.5.0
Release:	7
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Libraries/Python
Source0:	https://pypi.debian.net/fabric/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	de403c610dc1dd0f7c3e7ad46c620c33
URL:		http://www.fabfile.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-invoke
BuildRequires:	python-paramiko
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-invoke
BuildRequires:	python3-paramiko
%endif
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fabric is a high level library designed to execute shell commands
remotely over SSH, yielding useful Python objects in return.

%package -n python3-%{module}
Summary:	Execute shell commands remotely over SSH, yielding useful Python objects in return
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Fabric is a high level library designed to execute shell commands
remotely over SSH, yielding useful Python objects in return.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/fab
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
