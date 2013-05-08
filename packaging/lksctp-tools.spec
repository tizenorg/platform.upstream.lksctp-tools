Name:           lksctp-tools
Version:        1.0.10
Release:        0
License:        LGPL-2.1+
Summary:        Utilities for SCTP (Stream Control Transmission Protocol)
Url:            http://lksctp.sourceforge.net
Group:          System/Network
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  libtool

%description
This package contains the SCTP base runtime library and command line
tools.

SCTP (Stream Control Transmission Protocol) is a message-oriented,
reliable transport protocol with congestion control, support for
transparent multihoming, and multiple ordered streams of messages.

%package devel
Summary:        Development files for SCTP (Stream Control Transmission Protocol)
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
This package contains the SCTP development libraries and C header
files.

SCTP (Stream Control Transmission Protocol) is a message oriented,
reliable transport protocol, with congestion control, support for
transparent multi-homing, and multiple ordered streams of messages.

%prep
%setup -q

%build
autoreconf --force --install
CPPFLAGS="-I`pwd`/include" \
%configure --prefix=/usr \
	--enable-shared \
	--disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}/%{_libdir}/lksctp-tools/*.la
rm %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING  COPYING.lib
%{_bindir}/*
%{_libdir}/libsctp.so.*
%dir %{_libdir}/lksctp-tools
%{_libdir}/lksctp-tools/*.so.*
%{_mandir}/man7/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/netinet/sctp.h
%{_libdir}/libsctp.so
%dir %{_libdir}/lksctp-tools
%{_libdir}/lksctp-tools/*.so
%{_datadir}/lksctp-tools/
%{_mandir}/man3/*

%changelog
