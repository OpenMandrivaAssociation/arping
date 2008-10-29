Summary:	ARP Ping
Name:           arping
Version:        2.08
Release:        %mkrel 2
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.habets.pp.se/synscan/programs.php
Source0:	ftp://ftp.habets.pp.se/pub/synscan/%{name}-%{version}.tar.gz
Patch0:		arping-mdv_conf.diff
BuildRequires:	libnet1.1.2-devel
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
%patch0 -p0

%build

make RPM_OPT_FLAGS="%{optflags}" LDFLAGS2="-Wl,--as-needed -Wl,--no-undefined"
  
%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -m0755 %{name}.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README arping-scan-net.sh
%attr(0755,root,root) %{_sbindir}/*
%attr(0644,root,root) %{_mandir}/man8/%{name}.8*
