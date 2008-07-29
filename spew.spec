%define name spew
%define version 1.0.5
%define release %mkrel 3

Summary: An I/O benchmark tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.berlios.de/pub/spew/%{version}/%{name}-%{version}.tar.bz2
License: GPL
Group:	 System/Kernel and hardware 
Url: http://spew.berlios.de/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: popt-devel 
BuildRequires: ncurses-devel
%description
Spew is used to measure I/O performance of character devices,
block devices, and regular files. It can also be used to generate 
high I/O loads to stress systems while verifying data integrity.


%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace)/%{_sysconfdir}/spew.conf
%{_bindir}/gorge
%{_bindir}/regorge
%{_bindir}/spew
%{_mandir}/man1/gorge.1*
%{_mandir}/man1/regorge.1*
%{_mandir}/man1/spew.1*

