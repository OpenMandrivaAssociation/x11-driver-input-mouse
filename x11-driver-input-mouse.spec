Name: x11-driver-input-mouse
Version: 1.2.3
Release: %mkrel 2
Summary: Xorg input driver for mice
Group: System/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-mouse  xorg/drivers/xf86-input-mouse
# cd xorg/drivers/xf86-input/mouse
# git-archive --format=tar --prefix=xf86-input-mouse-1.2.3/ master | bzip2 -9 > xf86-input-mouse-1.2.3.tar.bz2
########################################################################
Source0: xf86-input-mouse-%{version}.tar.bz2

License: MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch2: 0002-Don-t-disable-3-button-emulation-if-third-mouse-butt.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
This package provide Xorg input driver for mice.

%prep
%setup -q -n xf86-input-mouse-%{version}

%patch1 -p1
%patch2 -p1

%build
autoreconf -ifs
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

