%define name ushare
%define version 1.0
%define release %mkrel 2 

Summary: uShare is a UPnP (TM) A/V Media Server
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}
Source2: ushare.crontab
License: GPL
Group: Video
Url: http://ushare.geexbox.org/
Buildrequires: libupnp-devel >= 1.4.2

%description
GeeXboX uShare is able to provide access to both images, videos, music or 
playlists files (see below for a complete file format support list).
It does not act as an UPnP Media Adaptor and thus,
can't transcode streams to fit the client requirements.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
#Installing a better initscript
rm -rf $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
mkdir -p %{buildroot}/etc/cron.daily
install -m 755 %SOURCE1 $RPM_BUILD_ROOT/%{_initrddir}/ushare
install -m 755 %SOURCE2 %{buildroot}/etc/cron.daily/ushare

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service ushare

%preun
%_preun_service ushare

%files
%defattr(-,root,root)
%{_initrddir}/ushare
%config(noreplace) %{_sysconfdir}/ushare.conf
%{_bindir}/ushare
%{_datadir}/locale/*/*/*
%{_mandir}/man1/ushare.1.*
%{_sysconfdir}/cron.daily/ushare


