Summary:	Lightweight C library which eases the writing of UNIX daemons
Name:		libdaemon
Version:	0.14
Release:	4
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz
# Source0-md5:	509dc27107c21bcd9fbf2f95f5669563
URL:		http://0pointer.de/lennart/projects/libdaemon/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdaemon is a lightweight C library which eases the writing of UNIX
daemons.

%package devel
Summary:	Header files and development documentation for libdaemon
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains Header files and development documentation for
libdaemon.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-lynx		\
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %ghost %{_libdir}/libdaemon.so.?
%attr(755,root,root) %{_libdir}/libdaemon.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdaemon.so
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

