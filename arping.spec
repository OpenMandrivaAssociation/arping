Summary:	ARP Ping
Name:           arping
Version:        2.09
Release:        %mkrel 2
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.habets.pp.se/synscan/programs.php
Source0:	ftp://ftp.habets.pp.se/pub/synscan/%{name}-%{version}.tar.gz
BuildRequires:	net-devel >= 1.1.3
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README extra/arping-scan-net.sh
%attr(0755,root,root) %{_sbindir}/*
%attr(0644,root,root) %{_mandir}/man8/%{name}.8*
