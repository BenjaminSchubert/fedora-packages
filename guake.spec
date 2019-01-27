Name:           guake
Version:        3.4.0
Release:        1%{?dist}
Summary:        Drop-down terminal for GNOME
License:        GPL-2.0-only
Group:          System/X11/Terminals
Url:            http://guake-project.org/
Source0:         https://github.com/Guake/guake/archive/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pandoc
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       keybinder3
Recommends:     libutempter0
Suggests:       gtk3-metatheme-numix
BuildArch:      noarch

%description
Guake is a dropdown terminal made for the GNOME desktop environment.

%prep
%setup -q

%build
make

%install
PBR_VERSION=%{version} make install DESTDIR=%{buildroot} prefix=%{_prefix}
rm -r %{buildroot}%{python3_sitelib}/guake/tests/
rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled
%fdupes %{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%doc README.rst NEWS.rst
%license COPYING
%{python3_sitelib}/*
%{_bindir}/guake
%{_bindir}/guake-toggle
%{_datadir}/applications/guake-prefs.desktop
%{_datadir}/applications/guake.desktop
%{_datadir}/glib-2.0/schemas/org.guake.gschema.xml
%{_datadir}/pixmaps/
%{_datadir}/guake/

%changelog
