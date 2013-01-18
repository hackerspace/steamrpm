#
# spec file for package steam
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

Name:           steam
Version:        1.0.0.21
Release:        1
License:        Steam License Agreement
Summary:        Installer for Valve's digital software distribution service
Url:            http://www.steampowered.com/
Group:          Amusements/Games/Other
# taken from http://media.steampowered.com/client/installer/steam.deb
# and repackaged using ar vx steam.deb
Source0:        steam-%{version}-binary.tar.gz
# also taken from the deb Description field
Source1:        STEAM-LICENSE.txt
Patch0:         desktop_file.patch
BuildRequires:  dos2unix
%if 0%{?suse_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%else
BuildRequires:  desktop-file-utils
%endif

# dep_postfix macro is used to append "-32bit" to dependencies for x86_64 on openSUSE

%define dep_postfix %{nil}

%ifarch x86_64

%if 0%{?suse_version}
%define dep_postfix -32bit
%endif

%if 0%{?fedora}
%define dep_postfix (x86-32)
%endif

%endif

%if 0%{?fedora}
Requires:       SDL%{dep_postfix} >= 1.2.10
Requires:       alsa-lib%{dep_postfix} >= 1.0.23
Requires:       cairo%{dep_postfix} >= 1.6.0
Requires:       dbus-libs%{dep_postfix} >= 1.2.14
Requires:       freetype%{dep_postfix} >= 2.3.9
Requires:       gdk-pixbuf2%{dep_postfix} >= 2.22.0
Requires:       glib2%{dep_postfix} >= 2.14.0
Requires:       gtk2%{dep_postfix} >= 2.24.0
Requires:       libX11%{dep_postfix} >= 1.4.99.1
Requires:       libXext%{dep_postfix}
Requires:       libXfixes%{dep_postfix}
Requires:       libXi%{dep_postfix} >= 1.2.99.4
Requires:       libXrandr%{dep_postfix} >= 1.2.99.3
Requires:       libXrender%{dep_postfix}
Requires:       libcurl%{dep_postfix} >= 7.16.2-1
Requires:       libgcc%{dep_postfix} >= 4.1.1
Requires:       libgcrypt%{dep_postfix} >= 1.4.5
Requires:       libjpeg-turbo%{dep_postfix}
Requires:       libogg%{dep_postfix} >= 1.0
Requires:       libstdc++%{dep_postfix} >= 4.6
Requires:       libtheora%{dep_postfix} >= 1.0
Requires:       libvorbis%{dep_postfix} >= 1.1.2
Requires:       nspr%{dep_postfix} >= 1.8.0.10
Requires:       nss%{dep_postfix} >= 3.12.3
Requires:       pango%{dep_postfix} >= 1.22.0
Requires:       pixman%{dep_postfix} >= 0.24.4
Requires:       pulseaudio-libs%{dep_postfix} >= 0.99.1
# Beyond what Debian claims
Requires:       mesa-dri-drivers%{dep_postfix}
%endif
%if 0%{?fedora} >= 18
Requires:       libpng12%{dep_postfix} >= 1.2.13
%endif
%if 0%{?fedora} == 17
Requires:       libpng-compat%{dep_postfix} >= 1.2.13
%endif
%if 0%{?fedora} <= 16
Requires:       libpng >= 1.2.13
%endif
%if 0%{?suse_version}
Requires:       Mesa-libGL1%{dep_postfix}
Requires:       Mesa-libGL1%{dep_postfix}
Requires:       alsa%{dep_postfix} >= 1.0.23
Requires:       gtk2-engine-oxygen%{dep_postfix}
Requires:       libSDL-1_2-0%{dep_postfix} >= 1.2.10
Requires:       libX11-6%{dep_postfix} >= 1.4.99.1
Requires:       libXext6%{dep_postfix}
Requires:       libXfixes3%{dep_postfix}
Requires:       libXi6%{dep_postfix} >= 1.2.99.4
Requires:       libXrandr2%{dep_postfix} >= 1.2.99.3
Requires:       libXrender1%{dep_postfix}
Requires:       libatk-1_0-0%{dep_postfix}
Requires:       libcairo2%{dep_postfix} >= 1.6.0
Requires:       libcurl4%{dep_postfix} >= 7.16.2-1
Requires:       libdbus-1-3%{dep_postfix} >= 1.2.14
Requires:       libfreetype6%{dep_postfix} >= 2.3.9
Requires:       libgcc47%{dep_postfix} >= 4.1.1
Requires:       libgcrypt11%{dep_postfix} >= 1.4.5
Requires:       libgdk_pixbuf-2_0-0%{dep_postfix} >= 2.22.0
Requires:       libglib-2_0-0%{dep_postfix} >= 2.14.0
Requires:       libgmodule-2_0-0%{dep_postfix}
Requires:       libgobject-2_0-0%{dep_postfix}
Requires:       libgtk-2_0-0%{dep_postfix} >= 2.24.0
Requires:       libjpeg8%{dep_postfix}
Requires:       libogg0%{dep_postfix} >= 1.0
Requires:       libopenal1-soft%{dep_postfix} >= 1.13
Requires:       libpango-1_0-0%{dep_postfix} >= 1.22.0
Requires:       libpixman-1-0%{dep_postfix} >= 0.24.4
Requires:       libpng12-0%{dep_postfix} >= 1.2.13
Requires:       libpulse0%{dep_postfix} >= 0.99.1
Requires:       libstdc++47%{dep_postfix} >= 4.6
Requires:       libtheora0%{dep_postfix} >= 1.0
Requires:       libvorbis0%{dep_postfix} >= 1.1.2
Requires:       mozilla-nspr%{dep_postfix} >= 1.8.0.10
Requires:       mozilla-nss%{dep_postfix} >= 3.12.3
%endif
Requires:       cups-libs%{dep_postfix} >= 1.4.0
Requires:       fontconfig%{dep_postfix} >= 2.8.0
Requires:       glibc%{dep_postfix} >= 2.15
Requires:       openal-soft >= 1.13
Requires:       zlib%{dep_postfix} >= 1.2.3.3

%description
Installer for the Beta of the Steam software distribution service
Steam is a software distribution service with an online store, automated
installation, automatic updates, achievements, SteamCloud synchronized
savegame and screenshot functionality, and many social features.

%prep
%setup -q -c %{name}-%{version}
dos2unix usr/share/applications/steam.desktop
%patch0 -p1
cp %{SOURCE1} .

%build
# Nothing to build

%install
mkdir -p %{buildroot}
rm usr/bin/steamdeps
cp -a usr %{buildroot}/

%if 0%{?fedora}
desktop-file-validate %{buildroot}/%{_datadir}/applications/steam.desktop
%endif
%if 0%{?suse_version}
%suse_update_desktop_file -r steam Game Amusement
%endif

%post
%if 0%{?fedora}
if [ ! -f /usr/lib/libjpeg.so.8 ]; then
  # Ubuntu has a different soname for this library.
  ln -s /usr/lib/libjpeg.so.62 /usr/lib/libjpeg.so.8
fi
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%if 0%{?suse_version} >= 1140
%desktop_database_post
%icon_theme_cache_post
%endif

%postun
%if 0%{?fedora}
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%endif

%if 0%{?suse_version} >= 1140
%desktop_database_postun
%icon_theme_cache_postun
%endif

%if 0%{?fedora}
%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%defattr(-,root,root)
%doc STEAM-LICENSE.txt
%{_bindir}/steam
%{_prefix}/lib/steam
%{_datadir}/pixmaps/steam.png
%{_datadir}/applications/steam.desktop
%{_datadir}/icons/hicolor/*/apps/steam.png
%doc %{_datadir}/doc/steam/
%{_mandir}/man6/steam.*

%changelog
* Fri Jan 18 2013 rissko@gmail.com - 1.0.0.21-1

- updated to 1.0.0.21

* Fri Dec 21 2012 prusnak@opensuse.org - 1.0.0.18-1

- updated to 1.0.0.18

* Thu Dec 20 2012 prusnak@opensuse.org

- spec cleanup

* Sat Dec 8 2012 jdmulloy@gmail.com

- Added support for x86_64 packages
- Fixed libpng dependency for openSUSE
- Added libopenal1-soft and Mesa-libGL1 dependencices for openSUSE

* Tue Nov 20 2012 mailaender@opensuse.org

- SUSE specific fixes

* Wed Nov 7 2012 spot@fedoraproject.org

- add more Requires (from downloaded bits, not packaged bits)

* Tue Nov 6 2012 spot@fedoraproject.org

- fedora specific libpng conditionalization

* Tue Nov 6 2012 spot@fedoraproject.org

- initial Fedora RPM packaging

