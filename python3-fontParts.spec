#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Set of objects for performing math operations on font data
Summary(pl.UTF-8):	Zbiór obiektów do wykonywania operacji matematycznych na danych fontów
Name:		python3-fontParts
Version:	0.9.11
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/fontparts/
#Source0:	https://files.pythonhosted.org/packages/source/f/fontparts/fontParts-%{version}.zip
Source0:	https://files.pythonhosted.org/packages/1b/73/90add4f89c74b7aff5ed7c90522bfc620cecd1c2fa3cee3bd5b006d44a9c/fontParts-%{version}.zip
# Source0-md5:	28dea9f06a9eb45af6e9f06e465fd826
URL:		https://pypi.org/project/fontparts/
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-booleanOperations >= 0.9.0
BuildRequires:	python3-fontMath >= 0.4.8
BuildRequires:	python3-fontPens >= 0.1.0
# FontTools[ufo,lxml,unicode]>=3.32.0
BuildRequires:	python3-fonttools >= 3.32.0
BuildRequires:	python3-fs >= 2.2.0
BuildRequires:	python3-lxml >= 4.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of objects that implement fast font, glyph, etc. math.

%description -l pl.UTF-8
Zbiór obiektów implementujących szybkie operacje matematyczne na
fontach, glifach itp.

%prep
%setup -q -n fontParts-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/Lib \
%{__python3} Lib/fontParts/fontshell/test.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/fontParts/test
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/fontParts/fontshell/test.py*
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/fontParts/fontshell/__pycache__/test.*.py*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/fontParts
%{py3_sitescriptdir}/fontParts-%{version}-py*.egg-info
