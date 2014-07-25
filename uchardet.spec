# define distsuffix mrb
# define debug_package %{nil}


%define lib_major 0
%define lib_name %mklibname uchardet %{lib_major}
%define develname %mklibname -d uchardet

Name: uchardet
Summary: Universal char-set detection
Version: 0.0.1
Release: 2
Group: Development/Other
License: MPLv1.1 
URL: http://code.google.com/p/uchardet/
Source0: http://uchardet.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: cmake

%description
uchardet is a C language binding of the original C++ implementation of the
universal char-set detection library by Mozilla. uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text.


%package -n %{lib_name}
Summary:    Universal charset detection
Group:      Development/Other

%description -n %{lib_name}
C language binding of the original C++ implementation of the
universal char-set detection library by Mozilla.

%files
%doc COPYING AUTHORS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%files -n %{lib_name}
%doc COPYING AUTHORS
%{_libdir}/lib%{name}.so.%{lib_major}*





%package -n %develname
Summary: Development files for uchardet
Provides:  %{name}-devel = %{version}-%{release}
Requires:  %{lib_name} = %{version}-%release

%description -n %develname
Header files and Libraries for the package uchardet.

%files -n %develname
%doc COPYING AUTHORS
%{_includedir}/%{name}
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build





