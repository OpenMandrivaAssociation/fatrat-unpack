%define _disable_ld_no_undefined 1

Summary:	UnPack plugin for FatRat
Name:		fatrat-unpack
Version:	1.1.3
Release:	1
License:	GPLv2+
Group:		Networking/File transfer
Url:		http://fatrat.dolezel.info/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	fatrat-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(libzip)
Requires:	fatrat
Requires:	libzip

%description
FatRat is an open source download manager for Linux/Unix systems written in C++
with the help of the Trolltech Qt 4 library. It is rich in features and is
continuously developed.

Unpack or pipe RAR (and ZIP optionally) archives inside the application.

%files
%{_libdir}/fatrat/plugins/libfatrat-unpack.so
%{_datadir}/fatrat/data/plugins/%{name}/pipecmds
%{_docdir}/%{name}/TRANSLATIONS
%{_docdir}/%{name}/3RDPARTIES

#----------------------------------------------------------------------------

%prep
%setup -q
sed s,lib/fatrat/plugins,%{_lib}/fatrat/plugins,g -i CMakeLists.txt

%build
%cmake_qt4 \
	-DWITH_ZIP=ON
cp config.h ..
%make

%install
%makeinstall_std -C build

