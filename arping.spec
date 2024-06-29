Summary:	ARP Ping
Name:		arping
Version:	2.25
Release:	1
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.habets.pp.se/synscan/programs.php?prog=arping
Source0:	http://www.habets.pp.se/synscan/files/%{name}-%{version}.tar.gz
BuildRequires:	libnet-devel >= 1.1.3
BuildRequires:	pkgconfig(libpcap)
Conflicts:	iputils
BuildSystem:	autotools

%description
Arping is a util to find out it a specific IP address on the LAN is 'taken'
and what MAC address owns it. Sure, you *could* just use 'ping' to find out if
it's taken and even if the computer blocks ping (and everything else) you still
get an entry in your ARP cache. But what if you aren't on a routable net? Or
the host blocks ping (all ICMP even)? Then you're screwed. Or you use arping.

%install -a
# "make install" doesn't install any libraries, so we don't
# need the headers either
rm -rf %{buildroot}%{_includedir}

%files
%doc README extra/arping-scan-net.sh
%attr(0755,root,root) %{_sbindir}/*
%attr(0644,root,root) %{_mandir}/man8/%{name}.8*
