%define name ushare
%define version 1.1a
%define release %mkrel 6

Summary: UPnP (TM) A/V Media Server
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ushare.geexbox.org/releases/%{name}-%{version}.tar.bz2
Source1: %{name}
Source2: ushare.crontab
License: GPLv2+
Group: Video
Url: http://ushare.geexbox.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: libupnp-devel >= 1.4.2, libdlna-devel

%description
GeeXboX uShare is able to provide access to both images, videos, music or 
playlists files (see below for a complete file format support list).
It does not act as an UPnP Media Adaptor and thus,
can't transcode streams to fit the client requirements.

%prep
%setup -q

%build
%setup_compile_flags
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --enable-dlna
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

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

%files -f %name.lang
%defattr(-,root,root)
%{_initrddir}/ushare
%config(noreplace) %{_sysconfdir}/ushare.conf
%{_bindir}/ushare
%{_sysconfdir}/cron.daily/ushare
