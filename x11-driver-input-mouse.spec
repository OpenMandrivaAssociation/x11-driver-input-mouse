Name: x11-driver-input-mouse
Version: 1.2.3
Release: %mkrel 1
Summary: Xorg input driver for mice
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-%{version}.tar.bz2
# open mouse twice to workaround a bug in the kernel when dealing
# with a PS/2 mouse and an USB keuboard
Patch0: x11-driver-input-mouse-twice.patch 
Patch1: 0001-DontDisable3ButtonEmulation.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
This package provide Xorg input driver for mice.

%prep
%setup -q -n xf86-input-mouse-%{version}
%patch0 -p1 -b .mouse-twice
%patch1 -p1 -b .dont-disable-3-button-emulation

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_mandir}/man4/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/mouse_drv.la
%{_libdir}/xorg/modules/input/mouse_drv.so

