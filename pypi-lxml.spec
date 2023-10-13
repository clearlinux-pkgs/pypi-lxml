#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-lxml
Version  : 4.9.3
Release  : 104
URL      : https://files.pythonhosted.org/packages/30/39/7305428d1c4f28282a4f5bdbef24e0f905d351f34cf351ceb131f5cddf78/lxml-4.9.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/30/39/7305428d1c4f28282a4f5bdbef24e0f905d351f34cf351ceb131f5cddf78/lxml-4.9.3.tar.gz
Summary  : Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: pypi-lxml-license = %{version}-%{release}
Requires: pypi-lxml-python = %{version}-%{release}
Requires: pypi-lxml-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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

%description python3
python3 components for the pypi-lxml package.


%prep
%setup -q -n lxml-4.9.3
cd %{_builddir}/lxml-4.9.3
pushd ..
cp -a lxml-4.9.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688572307
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build  %{?_smp_mflags}

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-lxml
cp %{_builddir}/lxml-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-lxml/9952214ce0aca4410ff3c7711d8389893713fe3b || :
cp %{_builddir}/lxml-%{version}/LICENSES.txt %{buildroot}/usr/share/package-licenses/pypi-lxml/495ceccaff92184d795e03cfc863c015dc3dced9 || :
cp %{_builddir}/lxml-%{version}/doc/licenses/GPL.txt %{buildroot}/usr/share/package-licenses/pypi-lxml/dfac199a7539a404407098a2541b9482279f690d || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
