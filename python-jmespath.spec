%define module jmespath
%bcond tests 0

Name:		python-jmespath
Version:	1.1.0
Release:	2
Summary:	JSON Matching Expressions
License:	MIT
Group:		Development/Python
URL:		https://github.com/jmespath/jmespath.py
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(hypothesis)
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
JSON Matching Expressions.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%{_bindir}/jp.py
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
