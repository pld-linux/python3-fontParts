#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-fontParts.spec)

Summary:	Set of objects for performing math operations on font data
Summary(pl.UTF-8):	Zbiór obiektów do wykonywania operacji matematycznych na danych fontów
Name:		python-fontParts
# keep 0.8.x for python2 support
Version:	0.8.9
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/fontparts/
Source0:	https://files.pythonhosted.org/packages/source/f/fontparts/fontParts-%{version}.zip
# Source0-md5:	e6b517961d4da511e2ebe49fab763126
URL:		https://pypi.org/project/fontparts/
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-booleanOperations
# defcon[pens]
BuildRequires:	python-defcon >= 0.6.0
BuildRequires:	python-enum34 >= 1.1.6
BuildRequires:	python-fontMath >= 0.4.8
BuildRequires:	python-fontPens >= 0.1.0
# FontTools[ufo,lxml,unicode] >= 3.32.0
BuildRequires:	python-fonttools >= 3.32.0
BuildRequires:	python-fs >= 2.2.0
BuildRequires:	python-lxml >= 4.0
BuildRequires:	python-unittest2 >= 1.1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-booleanOperations
BuildRequires:	python3-fontMath >= 0.4.8
BuildRequires:	python3-fontPens >= 0.1.0
BuildRequires:	python3-fonttools >= 3.32.0
BuildRequires:	python3-fs >= 2.2.0
BuildRequires:	python3-lxml >= 4.0
BuildRequires:	python3-unittest2 >= 1.1.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
# missing in setup
Requires:	python-booleanOperations
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of objects that implement fast font, glyph, etc. math.

%description -l pl.UTF-8
Zbiór obiektów implementujących szybkie operacje matematyczne na
fontach, glifach itp.

%package -n python3-fontParts
Summary:	Set of objects for performing math operations on font data
Summary(pl.UTF-8):	Zbiór obiektów do wykonywania operacji matematycznych na danych fontów
Group:		Libraries/Python
# missing in setup
Requires:	python3-booleanOperations
Requires:	python3-modules >= 1:3.6

%description -n python3-fontParts
A collection of objects that implement fast font, glyph, etc. math.

%description -n python3-fontParts -l pl.UTF-8
Zbiór obiektów implementujących szybkie operacje matematyczne na
fontach, glifach itp.

%prep
%setup -q -n fontParts-%{version}

%build
export LC_ALL=C.UTF-8

%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/Lib \
%{__python} Lib/fontParts/fontshell/test.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/Lib \
%{__python3} Lib/fontParts/fontshell/test.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

export LC_ALL=C.UTF-8

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/fontParts/test
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/fontParts/fontshell/test.py*
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/fontParts/test
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/fontParts/fontshell/test.py*
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/fontParts/fontshell/__pycache__/test.*.py*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/fontParts
%{py_sitescriptdir}/fontParts-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-fontParts
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/fontParts
%{py3_sitescriptdir}/fontParts-%{version}-py*.egg-info
%endif
