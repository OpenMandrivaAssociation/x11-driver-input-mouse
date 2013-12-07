Name:		x11-driver-input-mouse
Version:	1.9.0
Release:	5
Summary:	Xorg input driver for mice
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mouse-%{version}.tar.bz2
Patch0:		xf86-input-mouse-1.8.1-link-against-xi.patch
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xi)

Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

Conflicts:	xorg-x11-server < 7.0

%description
This package provide Xorg input driver for mice.

%package devel
Summary: Development files for Xorg mouse driver
Requires: %{name} = %{version}

%description devel
This package provides development files for Xord input driver for mice.

%prep
%setup -qn xf86-input-mouse-%{version}
%patch0 -p1


%build
autoreconf -fiv
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


%changelog
* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.7.2-2
+ Revision: 787166
- Rebuild for x11-server 1.12

* Sat Mar 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7.2-1
+ Revision: 785460
- version update 1.7.2

* Fri Dec 30 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.7.1-3
+ Revision: 748313
- rebuild, cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-2
+ Revision: 703623
- rebuild for new x11-server

* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-1
+ Revision: 699289
- update to new version 1.7.1

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.7.0-1
+ Revision: 683598
- New version 1.7.0.

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.6.99.901-3
+ Revision: 683550
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.99.901-2
+ Revision: 671128
- mass rebuild

  + Paulo Ricardo Zanoni <pzanoni@mandriva.com>
    - New version: 1.6.99.901
      Older versions don't compile under Xserver 1.10

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.6.0-3mdv2011.0
+ Revision: 595746
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.6.0-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Sat Sep 11 2010 Thierry Vignaud <tv@mandriva.org> 1.6.0-1mdv2011.0
+ Revision: 577218
- new release

* Tue Nov 10 2009 Thierry Vignaud <tv@mandriva.org> 1.5.0-2mdv2010.1
+ Revision: 464330
- rebuild for new xserver

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 1.5.0-1mdv2010.1
+ Revision: 463599
- new release

* Sat Jan 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.0-1mdv2009.1
+ Revision: 328151
- update to new version 1.4.0

* Fri Aug 01 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.0-2mdv2009.0
+ Revision: 259647
- Ship driver man page

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.0-1mdv2009.0
+ Revision: 194285
- Update to version 1.3.0.

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.3-5mdv2008.1
+ Revision: 160490
- Revert to use only upstream tarballs and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.3-4mdv2008.1
+ Revision: 156585
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.3-3mdv2008.1
+ Revision: 154966
- Updated BuildRequires and resubmit package.
- Make sure xf86MouseProtocolIDToName is of public visibility as this
  function is used by the xf86misc extension to change mouse parameters,
  and besides xorgcfg, others programs/installers out there may still
  use it... Probably the extension should be ``extended'' to also handle
  other types input devices and/or some method other than LoaderSymbol(...)
  used to check for availability of the option in a module.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update to properly use tag xf86-input-mouse-1.2.3. This tag has no diff with
  current master, but "comment documentation" properly updated to match command
  to generate tarball and patches.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.3-1mdv2008.1
+ Revision: 97212
- new upstream version: 1.2.3
- minor spec cleanup

* Mon Sep 10 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.2.2-2mdv2008.0
+ Revision: 84259
- This should fix Bugzilla #33033 as with the added patch it should never
  disable 3 button emulation if a 2 button mouse is detected, as it can be
  due to a mouse being plugged/unplugged.

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

* Wed Aug 01 2007 Thierry Vignaud <tv@mandriva.org> 1.2.2-1mdv2008.0
+ Revision: 57748
- new release


* Fri Dec 01 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.2.1-1mdv2007.0
+ Revision: 89744
- new release

* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.2.0-1mdv2007.1
+ Revision: 85915
- new release
- fix group
- fill in more missing descriptions

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - new upstream release (1.1.1):
      * Overhaul of wheel processing. Does work correctly with multibit
      zaxis events now. Autodetect (one way only) single wheel only for
      EXPS2. Use singlebit protocol for multiwheel EXPS2 mice.
      * Fixed manpage and default ZAxisMapping configuration.
    - added patch: open mouse twice to workaround a bug in the kernel when dealing
      with a PS/2 mouse and an USB keuboard
    - rebuild to fix cooker uploading
    - Updated drivers for X11R7.1
    - increment release
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

