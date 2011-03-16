%define name spew
%define version 1.0.8
%define release %mkrel 1

Summary: An I/O benchmark tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.berlios.de/pub/spew/%{version}/%{name}-%{version}.tgz
Patch0: %{name}-1.0.7-fix-str-fmt.patch
License: GPLv2
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
%patch0 -p1 -b .strfmt

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace)/%{_sysconfdir}/spew.conf
%{_bindir}/gorge
%{_bindir}/regorge
%{_bindir}/spew
%{_mandir}/man1/gorge.1*
%{_mandir}/man1/regorge.1*
%{_mandir}/man1/spew.1*

