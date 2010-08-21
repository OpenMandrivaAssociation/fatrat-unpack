%define name fatrat-unpack
%define oname fatrat
%define version 1.1.2
%define release %mkrel 2

Summary: UnPack plugin for FatRat
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPLv2
Group: Networking/File transfer
Url:   http://fatrat.dolezel.info/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libqt4-devel 
BuildRequires: libzip-devel
BuildRequires: cmake 

BuildRequires: fatrat-devel = %{version}
Requires: fatrat = %{version}
Requires: libzip

%description
FatRat is an open source download manager for Linux/Unix systems written in C++ with the help of the Trolltech Qt 4 library. It is rich in features and is continuously developed.
Unpack or pipe RAR (and ZIP optionally) archives inside the application


%prep
%setup -q

%build
cmake . -DWITH_ZIP=ON -DCMAKE_INSTALL_PREFIX=%{_prefix}

%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/%{oname}/plugins/libfatrat-unpack.so
%{_datadir}/%{oname}/data/plugins/%{name}/pipecmds
%{_docdir}/%{name}/TRANSLATIONS
%{_docdir}/%{name}/3RDPARTIES

%changelog
