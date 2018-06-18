Summary:	ARP Ping
Name:		arping
Version:	2.19
Release:	1
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.habets.pp.se/synscan/programs.php?prog=arping
Source0:	http://www.habets.pp.se/synscan/files/%{name}-%{version}.tar.gz
BuildRequires:	libnet-devel >= 1.1.3
BuildRequires:	libpcap-devel
Conflicts:	iputils

%description
Arping is a util to find out it a specific IP address on the LAN is 'taken'
and what MAC address owns it. Sure, you *could* just use 'ping' to find out if
it's taken and even if the computer blocks ping (and everything else) you still
get an entry in your ARP cache. But what if you aren't on a routable net? Or
the host blocks ping (all ICMP even)? Then you're screwed. Or you use arping.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc README extra/arping-scan-net.sh
%attr(0755,root,root) %{_sbindir}/*
%attr(0644,root,root) %{_mandir}/man8/%{name}.8*
