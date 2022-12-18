%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		uchardet
Version:	0.0.8
Release:	1
Summary:	Universal charset detection
Group:		Development/Other
License:	MPL
URL:		https://www.freedesktop.org/wiki/Software/uchardet/
Source0:	https://www.freedesktop.org/software/uchardet/releases/%{name}-%{version}.tar.xz
BuildRequires:	cmake

%description
uchardet is a C language binding of the original C++ implementation of the
universal charset detection library by Mozilla. uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text. Returned encoding names are iconv-compatible.

#------------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libname}
C language binding of the original C++ implementation of the
universal charset detection library by Mozilla.

#------------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Header and Libraries files for the package %{name}.

#------------------------------------------------------------------------------
%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%doc COPYING AUTHORS README.md
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1.*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
