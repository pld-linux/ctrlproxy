Summary:	An IRC proxy with multi-server and plugin support
Summary(pl):	Proxy dla IRC z obs³ug± wielu serwerów i "wtyczek"
Name:		ctrlproxy
Version:	2.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://jelmer.vernstok.nl/oss/ctrlproxy/%{name}-%{version}.tar.gz
# Source0-md5:	b807dedad9f158e45d927e1744c8d36c
Source1:	%{name}rc
Patch0:		%{name}-gcc295.patch
URL:		http://jelmer.vernstok.nl/oss/ctrlproxy/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pcre-devel
BuildRequires:	popt-devel
BuildRequires:	tdb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ctrlproxy is a modular IRC proxy. It connects to a number of IRC
servers and then passes data it receives on to the modules that have
been loaded into it. Current modules are client_simple (for proxy
support) and log (for irssi-style log file generation).

By default, ctrlproxy listens for client connections on port 6668 and
any ports after that one, depending on the number of servers it is
connected to.

%description -l pl
ctrlproxy jest modularnym serwerem proxy dla IRC. £±czy siê z wieloma
serwerami IRC i przekazuje odebrane dane modu³om które zosta³y
za³adowane. W chwili obecnej dostêpne s± modu³y client_simple (do
obs³ugi proxy) i log (do tworzenia logów w formacie irssi).

Domy¶lnie, ctrlproxy oczekuje na po³±czenia od klientów na porcie 6668
i dowolnej liczbie kolejnych portów, zale¿nie od liczby serwerów do
których jest pod³±czony.

%package devel
Summary:	Header files and examples for developing ctrlproxy modules
Summary(pl):	Pliki nag³ówkowe i przyk³ady s³u¿±ce do rozwijania modu³ów ctrlproxy
Group:		Development/Libraries

%description devel
Header files and examples for developing ctrlproxy modules.

%description devel -l pl
Pliki nag³ówkowe i przyk³ady s³u¿±ce do rozwijania modu³ów ctrlproxy.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}rc
cp -r example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO ctrlproxyrc.dtd ctrlproxyrc.example
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/ctrlproxy.1*
%{_mandir}/man5/ctrlproxyrc.5*
%attr(755,root,root) %{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
%{_includedir}/*
