#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-meson_python
Version  : 0.8.1
Release  : 9
URL      : https://files.pythonhosted.org/packages/c3/94/957a04750188722d09ade6ae3731b115366177faee32ace175c3ca59358b/meson_python-0.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c3/94/957a04750188722d09ade6ae3731b115366177faee32ace175c3ca59358b/meson_python-0.8.1.tar.gz
Summary  : Meson Python build backend (PEP 517)
Group    : Development/Tools
License  : MIT
Requires: pypi-meson_python-license = %{version}-%{release}
Requires: pypi-meson_python-python = %{version}-%{release}
Requires: pypi-meson_python-python3 = %{version}-%{release}
Requires: ninja
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : pypi(meson)
BuildRequires : pypi(ninja)
BuildRequires : pypi(pyproject_metadata)
BuildRequires : pypi(tomli)

%description
# meson-python [![PyPI version](https://badge.fury.io/py/meson-python.svg)](https://pypi.org/project/meson-python/)

%package license
Summary: license components for the pypi-meson_python package.
Group: Default

%description license
license components for the pypi-meson_python package.


%package python
Summary: python components for the pypi-meson_python package.
Group: Default
Requires: pypi-meson_python-python3 = %{version}-%{release}

%description python
python components for the pypi-meson_python package.


%package python3
Summary: python3 components for the pypi-meson_python package.
Group: Default
Requires: python3-core
Provides: pypi(meson_python)
Requires: pypi(meson)
Requires: pypi(ninja)
Requires: pypi(pyproject_metadata)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-meson_python package.


%prep
%setup -q -n meson_python-0.8.1
cd %{_builddir}/meson_python-0.8.1
pushd ..
cp -a meson_python-0.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660585185
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-meson_python
cp %{_builddir}/meson_python-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-meson_python/bd79060eebf1013a670a70a31e15b6bc53b02cd8
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-meson_python/bd79060eebf1013a670a70a31e15b6bc53b02cd8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
