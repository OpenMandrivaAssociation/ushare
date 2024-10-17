%define debug_package %{nil}

Summary: UPnP (TM) A/V Media Server
Name: ushare
Version: 1.1a
Release: 9
Source0: http://ushare.geexbox.org/releases/%{name}-%{version}.tar.bz2
Source1: %{name}.service
Source2: ushare.crontab
Patch0: ushare-1.1a-fix-str-fmt.patch
Patch1:	01_all_ushare_build_system.patch
Patch3:	03_all_ushare_mp4_video_mime.patch
Patch4:	04_all_ushare_upnp_build_fix.patch
Patch5:	05_all_missing_headers.patch
License: GPLv2+
Group: Video
Url: https://ushare.geexbox.org/
Buildrequires: pkgconfig(libupnp)
Buildrequires: pkgconfig(libdlna)

%description
GeeXboX uShare is able to provide access to both images, videos, music or 
playlists files (see below for a complete file format support list).
It does not act as an UPnP Media Adaptor and thus,
can't transcode streams to fit the client requirements.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%setup_compile_flags
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --enable-dlna
make

%install
%makeinstall_std

%find_lang %{name}

#Installing a better initscript
rm -rf %{buildroot}/etc/init.d
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/etc/cron.daily
install -m0644 %SOURCE1 -D %{buildroot}%{_unitdir}/%{name}.service
install -m 755 %SOURCE2 %{buildroot}/etc/cron.daily/ushare

%post
%systemd_post ushare

%preun
%systemd_preun ushare

%files -f %{name}.lang
%attr(0644,root,root) %{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/ushare.conf
%{_bindir}/ushare
%{_sysconfdir}/cron.daily/ushare
