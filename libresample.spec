Summary:	Free sampling-rate conversion library
Summary(pl):	Wolnodostêpna biblioteka do zmiany czêstotliwo¶ci próbkowania
Name:		libresample
Version:	0.1.3
Release:	1
License:	LGPL
Group:		Libraries
#Source0Download: http://www-ccrma.stanford.edu/~jos/resample/Free_Resampling_Software.html
Source0:	http://ccrma.stanford.edu/~jos/resample/%{name}-%{version}.tgz
# Source0-md5:	99bc5ea15ef76b83e5655a10968f674b
Patch0:		%{name}-shared.patch
URL:		http://www-ccrma.stanford.edu/~jos/resample/
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free sampling-rate conversion library.

%description -l pl
Wolnodostêpna biblioteka do zmiany czêstotliwo¶ci próbkowania.

%package devel
Summary:	Header files for libresample library
Summary(pl):	Pliki nag³ówkowe biblioteki libresample
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libresample library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libresample.

%package static
Summary:	Static libresample library
Summary(pl):	Statyczna biblioteka libresample
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libresample library.

%description static -l pl
Statyczna biblioteka libresample.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/resample-sndfile
%attr(755,root,root) %{_libdir}/libresample.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libresample.so
%{_libdir}/libresample.la
%{_includedir}/libresample.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libresample.a
