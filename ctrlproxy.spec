Summary:	An IRC proxy with multi-server and plugin support
Summary(pl.UTF-8):	Proxy dla IRC z obsługą wielu serwerów i "wtyczek"
Name:		ctrlproxy
Version:	2.6.2
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://jelmer.vernstok.nl/releases/%{name}-%{version}.tar.gz
# Source0-md5:  62fc258cb17902b38b39dc5c5a4e27f9
Source1:	%{name}rc
Patch0:		%{name}-no_doc.patch
URL:		http://jelmer.vernstok.nl/oss/ctrlproxy/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
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

%description -l pl.UTF-8
ctrlproxy jest modularnym serwerem proxy dla IRC. Łączy się z wieloma
serwerami IRC i przekazuje odebrane dane modułom które zostały
załadowane. W chwili obecnej dostępne są moduły client_simple (do
obsługi proxy) i log (do tworzenia logów w formacie irssi).

Domyślnie, ctrlproxy oczekuje na połączenia od klientów na porcie 6668
i dowolnej liczbie kolejnych portów, zależnie od liczby serwerów do
których jest podłączony.

%package devel
Summary:	Header files and examples for developing ctrlproxy modules
Summary(pl.UTF-8):	Pliki nagłówkowe i przykłady służące do rozwijania modułów ctrlproxy
Group:		Development/Libraries

%description devel
Header files and examples for developing ctrlproxy modules.

%description devel -l pl.UTF-8
Pliki nagłówkowe i przykłady służące do rozwijania modułów ctrlproxy.

%prep
%setup -q
%patch -P0 -p1

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
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}rc
cp -r example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install %{name}-setup $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO ctrlproxyrc.dtd ctrlproxyrc.example doc/*.xml doc/figures/*.pdf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
%{_includedir}/*
