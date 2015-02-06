%define name spew
%define version 1.0.8
%define release 2

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



%changelog
* Wed Mar 16 2011 St√©phane T√©letch√©a <steletch@mandriva.org> 1.0.8-1mdv2011.0
+ Revision: 645429
- update to new version 1.0.8

* Wed May 27 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 1.0.7-1mdv2010.0
+ Revision: 380045
- update to new version 1.0.7
- fix str fmt
- fix license (GPLv2)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2008.1
+ Revision: 127535
- kill re-definition of %%buildroot on Pixel's request
- fix man pages extension


* Tue Dec 13 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.0.5-1mdk
- New release 1.0.5

* Tue Oct 04 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.0.4-3mdk
- Fix BuildRequires

* Tue Oct 04 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.0.4-2mdk
- Fix BuildRequires

* Fri Jun 24 2005 Erwan Velu <velu@seanodes.com> 1.0.4-1mdk
- Initial Release

