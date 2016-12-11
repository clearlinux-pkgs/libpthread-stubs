#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpthread-stubs
Version  : 0.3
Release  : 8
URL      : http://xorg.freedesktop.org/releases/individual/xcb/libpthread-stubs-0.3.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/xcb/libpthread-stubs-0.3.tar.bz2
Summary  : Stubs missing from libc for standard pthread functions
Group    : Development/Tools
License  : MIT-feh

%description
This library provides weak aliases for pthread functions not provided in libc
or otherwise available by default.  Libraries like libxcb rely on pthread
stubs to use pthreads optionally, becoming thread-safe when linked to
libpthread, while avoiding any performance hit when running single-threaded.
libpthread-stubs supports this behavior even on platforms which do not supply
all the necessary pthread stubs.  On platforms which already supply all the
necessary pthread stubs, this package ships only the pkg-config file
pthread-stubs.pc, to allow libraries to unconditionally express a dependency
on pthread-stubs and still obtain correct behavior.

%package dev
Summary: dev components for the libpthread-stubs package.
Group: Development
Provides: libpthread-stubs-devel

%description dev
dev components for the libpthread-stubs package.


%prep
%setup -q -n libpthread-stubs-0.3

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/pthread-stubs.pc
