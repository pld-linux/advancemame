#
# Conditional build:
%bcond_with	svga	# SVGAlib support

Summary:	AdvanceMAME emulator
Summary(pl.UTF-8):	Emulator AdvanceMAME
Name:		advancemame
Version:	3.10
Release:	1
License:	GPL v2+ (Advance), BSD (MAME)
Group:		Applications/Emulators
#Source0Download: http://www.advancemame.it/download
Source0:	https://github.com/amadvance/advancemame/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	620129fd17916e052bf594b866714133
Patch0:		%{name}-format.patch
Patch1:		%{name}-slang.patch
Patch2:		%{name}-missing.patch
URL:		http://www.advancemame.it/readme
# or SDL>=1.2.14
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
BuildRequires:	expat-devel >= 1.95.7
BuildRequires:	freetype-devel >= 2.4.4
BuildRequires:	gcc >= 2.95.3
BuildRequires:	libstdc++-devel
BuildRequires:	make >= 1:3.79.1
BuildRequires:	nasm >= 0.98
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.674
BuildRequires:	sed >= 4.0
BuildRequires:	slang-devel >= 1.4.3
%{?with_svga:BuildRequires:	svgalib-devel >= 1.9.14}
BuildRequires:	zlib-devel >= 1.2.5
Requires:	expat >= 1.95.7
Requires:	freetype >= 2.4.4
Requires:	slang >= 1.4.3
%{?with_svga:Requires:	svgalib >= 1.9.14}
Requires:	zlib >= 1.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AdvanceMAME is an unofficial MAME 0.106 version with an advanced video
support for helping the use with TVs, Arcade monitors, PC monitors and
LCD screens.

%description -l pl.UTF-8
AdvanceMAME to nieoficjalna wersja MAME 0.106 z rozszerzoną obsługą
obrazu, pozwalającą na korzystanie z telewizorów, monitorów gier
wideo, monitorów PC oraz ekranów LCD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	%{?with_svga:--enable-svgalib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# racy mkdir vs copy
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir} \
	mandir=%{_mandir}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/advance

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README RELEASE doc/{authors,cardlinx,cost,faq,script}.html
%attr(755,root,root) %{_bindir}/advcfg
%attr(755,root,root) %{_bindir}/advj
%attr(755,root,root) %{_bindir}/advk
%attr(755,root,root) %{_bindir}/advm
%attr(755,root,root) %{_bindir}/advmame
%attr(755,root,root) %{_bindir}/advmenu
%attr(755,root,root) %{_bindir}/advmess
%attr(755,root,root) %{_bindir}/advs
%attr(755,root,root) %{_bindir}/advv
%{_mandir}/man1/advcfg.1*
%{_mandir}/man1/advdev.1*
%{_mandir}/man1/advj.1*
%{_mandir}/man1/advk.1*
%{_mandir}/man1/advm.1*
%{_mandir}/man1/advmame.1*
%{_mandir}/man1/advmenu.1*
%{_mandir}/man1/advmess.1*
%{_mandir}/man1/advs.1*
%{_mandir}/man1/advv.1*
%dir %{_datadir}/advance
%dir %{_datadir}/advance/artwork
%dir %{_datadir}/advance/crc
%dir %{_datadir}/advance/image
%dir %{_datadir}/advance/rom
%dir %{_datadir}/advance/sample
%dir %{_datadir}/advance/snap
%{_datadir}/advance/category.ini
%{_datadir}/advance/cheat.dat
%{_datadir}/advance/event.dat
%{_datadir}/advance/hiscore.dat
%{_datadir}/advance/history.dat
%{_datadir}/advance/sysinfo.dat

# TODO: some subpackages with images?
%dir %{_datadir}/advance/image/ti99_4a
%{_datadir}/advance/image/ti99_4a/alpiner.zip
%{_datadir}/advance/image/ti99_4a/attack.zip
%{_datadir}/advance/image/ti99_4a/carwars.zip
%{_datadir}/advance/image/ti99_4a/munchmn.zip
%{_datadir}/advance/image/ti99_4a/parsec.zip
%{_datadir}/advance/image/ti99_4a/ti-inva.zip
%{_datadir}/advance/image/ti99_4a/tombcit.zip
%{_datadir}/advance/image/ti99_4a/v-chess.zip
%{_datadir}/advance/image/ti99_4a/vidgam1.zip
%{_datadir}/advance/image/ti99_4a/vidgam2.zip
%{_datadir}/advance/rom/gridlee.zip
%{_datadir}/advance/rom/polyplay.zip
%{_datadir}/advance/rom/robby.zip
%{_datadir}/advance/rom/ti99_4a.zip
%{_datadir}/advance/sample/gridlee.zip
%{_datadir}/advance/snap/gridlee.zip
%{_datadir}/advance/snap/polyplay.zip
%{_datadir}/advance/snap/robby.zip
%{_datadir}/advance/snap/ti99_4a.png
%dir %{_datadir}/advance/snap/ti99_4a
%{_datadir}/advance/snap/ti99_4a/alpiner.zip
%{_datadir}/advance/snap/ti99_4a/attack.zip
%{_datadir}/advance/snap/ti99_4a/carwars.zip
%{_datadir}/advance/snap/ti99_4a/munchmn.zip
%{_datadir}/advance/snap/ti99_4a/parsec.zip
%{_datadir}/advance/snap/ti99_4a/ti-inva.zip
%{_datadir}/advance/snap/ti99_4a/tombcit.zip
%{_datadir}/advance/snap/ti99_4a/v-chess.zip
%{_datadir}/advance/snap/ti99_4a/vidgam1.zip
%{_datadir}/advance/snap/ti99_4a/vidgam2.zip
