Summary:	Extra themes for GNOME environment
Summary(pl.UTF-8):	Dodatkowe motywy dla środowiska GNOME
Name:		gnome-themes-extra
Version:	3.28
Release:	2
License:	LGPL v2.1+
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-extra/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	f9f2c6c521948da427f702372e16f826
URL:		https://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.24.15
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-HighContrast = %{version}-%{release}
Requires:	%{name}-Adwaita = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extra themes for GNOME environment.

%description -l pl.UTF-8
Dodatkowe motywy dla środowiska GNOME.

%package Adwaita
Summary:	Adwaita and Adwaita-dark GTK+3 themes
Summary(pl.UTF-8):	Motywy GTK+3 Adwaita i Adwaita-dark
Group:		Themes
Requires:	adwaita-icon-theme
Requires:	gtk+3 >= 3.10.0
Obsoletes:	gnome-themes-standard < 3.27
BuildArch:	noarch

%description Adwaita
Adwaita and Adwaita-dark GTK+3 themes for use outside of GNOME.

%description Adwaita -l pl.UTF-8
Motywy GTK+3 Adwaita i Adwaita-dark przeznaczone do używania poza
GNOME.

%package HighContrast
Summary:	HighContrast accessibility theme for GNOME environment
Summary(pl.UTF-8):	Motyw uprzystępniający HighContrast dla środowiska GNOME
Group:		Themes
Requires(post):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	adwaita-icon-theme
Obsoletes:	gnome-themes-HighContrast < 3.0-1
Obsoletes:	gnome-themes-HighContrastLargePrint < 3.0-1
Obsoletes:	gnome-themes-standard-accessibility < 3.27
BuildArch:	noarch

%description HighContrast
HighContrast accessibility theme for GNOME environment.

%description HighContrast -l pl.UTF-8
Motyw uprzystępniający HighContrast dla środowiska GNOME.

%package -n gtk2-theme-engine-adwaita
Summary:	Adwaita GTK+ 2 theme
Summary(pl.UTF-8):	Motyw Adwaita dla GTK+ 2
Group:		Themes/GTK+
Requires:	adwaita-icon-theme
Requires:	gtk+2 >= 2:2.24.15

%description -n gtk2-theme-engine-adwaita
This package contains a GTK+ 2 theme for presenting widgets with a
GNOME look and feel.

%description -n gtk2-theme-engine-adwaita -l pl.UTF-8
Ten pakiet zawiera motyw GTK+ 2 do prezentowania widgetów z wyglądem i
zachowaniem GNOME.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.la

# gtk+2 cache
touch $RPM_BUILD_ROOT%{_iconsdir}/HighContrast/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post HighContrast
%update_icon_cache HighContrast

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.md

%files Adwaita
%defattr(644,root,root,755)
%dir %{_datadir}/themes/Adwaita
%{_datadir}/themes/Adwaita/gtk-3.0
%{_datadir}/themes/Adwaita/index.theme
%dir %{_datadir}/themes/Adwaita-dark
%{_datadir}/themes/Adwaita-dark/gtk-3.0
%{_datadir}/themes/Adwaita-dark/index.theme

%files HighContrast
%defattr(644,root,root,755)
%dir %{_datadir}/themes/HighContrast
%{_datadir}/themes/HighContrast/gtk-2.0
%{_datadir}/themes/HighContrast/gtk-3.0
%{_datadir}/themes/HighContrast/index.theme
%dir %{_iconsdir}/HighContrast
%{_iconsdir}/HighContrast/*x*
%{_iconsdir}/HighContrast/scalable
%ghost %{_iconsdir}/HighContrast/icon-theme.cache

%files -n gtk2-theme-engine-adwaita
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.so
%{_datadir}/themes/Adwaita/gtk-2.0
%{_datadir}/themes/Adwaita-dark/gtk-2.0
