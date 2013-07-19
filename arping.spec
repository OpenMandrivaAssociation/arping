Summary:	ARP Ping
Name:		arping
Version:	2.13
Release:	1
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.habets.pp.se/synscan/programs.php?prog=arping
Source0:	http://www.habets.pp.se/synscan/files/%{name}-%{version}.tar.gz
BuildRequires:	net-devel >= 1.1.3
BuildRequires:	libpcap-devel

%description
Arping is a util to find out it a specific IP address on the LAN is 'taken'
and what MAC address owns it. Sure, you *could* just use 'ping' to find out if
it's taken and even if the computer blocks ping (and everything else) you still
get an entry in your ARP cache. But what if you aren't on a routable net? Or
the host blocks ping (all ICMP even)? Then you're screwed. Or you use arping.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README extra/arping-scan-net.sh
%attr(0755,root,root) %{_sbindir}/*
%attr(0644,root,root) %{_mandir}/man8/%{name}.8*


%changelog
* Mon Jul 02 2012 Oden Eriksson <oeriksson@mandriva.com> 2.12-1
+ Revision: 807769
- 2.12

* Thu Mar 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.11-1
+ Revision: 781672
- update to 2.11

* Sun Feb 26 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.10-1
+ Revision: 780941
- update to 2.10

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.09-2mdv2011.0
+ Revision: 609992
- rebuild

* Fri Apr 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.09-1mdv2010.1
+ Revision: 530764
- 2.09

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 2.08-3mdv2010.0
+ Revision: 382694
- rebuilt against libnet 1.1.3

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 2.08-2mdv2009.1
+ Revision: 298233
- rebuilt against libpcap-1.0.0

* Fri Aug 15 2008 Oden Eriksson <oeriksson@mandriva.com> 2.08-1mdv2009.0
+ Revision: 272263
- 2.08
- use the new LDFLAGS

* Fri Aug 08 2008 Frederik Himpe <fhimpe@mandriva.org> 2.07-1mdv2009.0
+ Revision: 269496
- Update to new version 2.07
- Fix license

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 2.06-2mdv2009.0
+ Revision: 226171
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Sep 14 2007 Oden Eriksson <oeriksson@mandriva.com> 2.06-1mdv2008.0
+ Revision: 85629
- Import arping


