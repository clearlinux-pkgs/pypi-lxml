#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-lxml
Version  : 4.8.0
Release  : 86
URL      : https://files.pythonhosted.org/packages/3b/94/e2b1b3bad91d15526c7e38918795883cee18b93f6785ea8ecf13f8ffa01e/lxml-4.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/94/e2b1b3bad91d15526c7e38918795883cee18b93f6785ea8ecf13f8ffa01e/lxml-4.8.0.tar.gz
Summary  : Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: pypi-lxml-license = %{version}-%{release}
Requires: pypi-lxml-python = %{version}-%{release}
Requires: pypi-lxml-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : pypi(cython)
BuildRequires : zlib-dev
Provides: lxml
Provides: lxml-python3

%description
What is lxml?
=============
lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.
It's also very fast and memory friendly, just so you know.

%package license
Summary: license components for the pypi-lxml package.
Group: Default

%description license
license components for the pypi-lxml package.


%package python
Summary: python components for the pypi-lxml package.
Group: Default
Requires: pypi-lxml-python3 = %{version}-%{release}

%description python
python components for the pypi-lxml package.


%package python3
Summary: python3 components for the pypi-lxml package.
Group: Default
Requires: python3-core
Provides: pypi(lxml)
Requires: pypi(cython)

%description python3
python3 components for the pypi-lxml package.


%prep
%setup -q -n lxml-4.8.0
cd %{_builddir}/lxml-4.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645117236
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  %{?_smp_mflags}

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-lxml
cp %{_builddir}/lxml-4.8.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-lxml/9952214ce0aca4410ff3c7711d8389893713fe3b
cp %{_builddir}/lxml-4.8.0/LICENSES.txt %{buildroot}/usr/share/package-licenses/pypi-lxml/495ceccaff92184d795e03cfc863c015dc3dced9
cp %{_builddir}/lxml-4.8.0/doc/licenses/GPL.txt %{buildroot}/usr/share/package-licenses/pypi-lxml/dfac199a7539a404407098a2541b9482279f690d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-lxml/495ceccaff92184d795e03cfc863c015dc3dced9
/usr/share/package-licenses/pypi-lxml/9952214ce0aca4410ff3c7711d8389893713fe3b
/usr/share/package-licenses/pypi-lxml/dfac199a7539a404407098a2541b9482279f690d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
