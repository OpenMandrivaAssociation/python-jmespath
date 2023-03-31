Name:		python-jmespath
Version:	1.0.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/j/jmespath/jmespath-%{version}.tar.gz
Summary:	JSON Matching Expressions
URL:		https://pypi.org/project/jmespath/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
JSON Matching Expressions

%prep
%autosetup -p1 -n jmespath-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/jp.py
%{py_sitedir}/jmespath
%{py_sitedir}/jmespath-*.*-info
