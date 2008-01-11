%define debug_package	%{nil}

Name: x11-driver-input-mouse
Version: 1.2.3
Release: %mkrel 3
Summary: Xorg input driver for mice
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-mouse xorg/drivers/xf86-input-mouse
# cd xorg/drivers/xf86-input/mouse
# git-archive --format=tar --prefix=xf86-input-mouse-1.2.3/ xf86-input-mouse-1.2.3 | bzip2 -9 > xf86-input-mouse-1.2.3.tar.bz2
########################################################################
Source0: xf86-input-mouse-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-mouse-1.2.3..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch2: 0002-Don-t-disable-3-button-emulation-if-third-mouse-butt.patch
Patch3: 0003-Make-sure-xf86MouseProtocolIDToName-is-of-public-v.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
#BuildRequires: gcc			>= 4.2.2
#BuildRequires: glibc-devel		>= 2.7
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
This package provide Xorg input driver for mice.


%prep
%setup -q -n xf86-input-mouse-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/input/*.la
# FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME
# Maybe a better conflict fix should be implemented?
# I.e. install xorg module manpages in one place and/or have some
# prefix/sufix to not conflict with other manpages, in this case the
# manpage for the kernel interface.
# FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME
rm -f %{buildroot}%{_mandir}/man4/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/mouse_drv.so
