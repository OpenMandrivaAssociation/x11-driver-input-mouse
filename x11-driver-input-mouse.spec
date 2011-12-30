Name: x11-driver-input-mouse
Version: 1.7.1
Release: 3
Summary: Xorg input driver for mice
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-%{version}.tar.bz2
Patch1: 0001-Don-t-disable-3-button-emulation-if-third-mouse-butt.patch

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

Conflicts: xorg-x11-server < 7.0

%description
This package provide Xorg input driver for mice.

%prep
%setup -qn xf86-input-mouse-%{version}
%apply_patches

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/input/mouse_drv.so
%{_mandir}/man4/mousedrv.*

