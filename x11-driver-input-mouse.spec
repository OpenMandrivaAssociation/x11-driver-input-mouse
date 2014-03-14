Name:		x11-driver-input-mouse
Version:	1.9.0
Release:	5
Summary:	Xorg input driver for mice
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-%{version}.tar.bz2
Patch0:		xf86-input-mouse-1.8.1-link-against-xi.patch
# see mdvbz#33033, do not disable!
Patch1:		0001-Don-t-disable-3-button-emulation-if-third-mouse-butt.patch
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xi)

Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

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
%configure2_5x

%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/input/mouse_drv.so
%{_mandir}/man4/mousedrv.*

%files devel
%{_includedir}/xorg/xf86-mouse-properties.h
%{_libdir}/pkgconfig/xorg-mouse.pc
