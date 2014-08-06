Name:		x11-driver-input-mouse
Version:	1.9.0
Release:	8
Summary:	Xorg input driver for mice
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-%{version}.tar.bz2
Patch0:		xf86-input-mouse-1.8.1-link-against-xi.patch
# see mdvbz#33033, do not disable!
Patch1:		0001-Don-t-disable-3-button-emulation-if-third-mouse-butt.patch
BuildRequires:	pkgconfig(xproto) >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.12
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xi)
# strange deps?
#Requires:	%(xserver-sdk-abi-requires xinput || echo xserver-abi(xinput-20) >= 0)
#Requires:	%(xserver-sdk-abi-requires ansic || xserver-abi(ansic-0) >= 4)

Conflicts:	xorg-x11-server < 7.0

%description
This package provide Xorg input driver for mice.

%package	devel
Summary:	Development files for Xorg mouse driver
Requires:	%{name} = %{EVRD}

%description	devel
This package provides development files for Xord input driver for mice.

%prep
%setup -qn xf86-input-mouse-%{version}
%patch0 -p1
%patch1 -p1
autoreconf -fiv

%build
%configure

%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/input/mouse_drv.so
%{_mandir}/man4/mousedrv.*

%files devel
%{_includedir}/xorg/xf86-mouse-properties.h
%{_libdir}/pkgconfig/xorg-mouse.pc
