Summary:	an IRC proxy with multi-server and plugin support
Summary(pl):	IRC proxy z obs³ug± wielu serwerów i "wtyczek"
Name:		ctrlproxy
Version:	2.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://jelmer.vernstok.nl/oss/ctrlproxy/%{name}-%{version}.tar.gz
# Source0-md5:	b807dedad9f158e45d927e1744c8d36c
Source1:	%{name}rc
URL:		http://jelmer.vernstok.nl/oss/ctrlproxy/
BuildRequires:	libxml2-devel
BuildRequires:	tdb-devel
BuildRequires:	pcre-devel
BuildRequires:	glib2-devel
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
ctrlproxy jest modularnym serwerem IRC proxy. £±czy siê z wieloma
serwerami IRC i przekazuje odebrane dane modu³om które zosta³y
za³adowane. W chwili obecnej dostêpne s± modu³y client_simple (do
obs³ugi proxy) i log (do tworzenia logów w formacie irssi)

Domy¶lnie, ctrlproxy oczekuje na po³±czenia od klientów na porcie 6668
i dowolnej ilo¶ci kolejnych portów, zale¿nie od ilo¶ci serwerów do
których jest pod³±czony.

%package devel
Summary:	Header files and examples for developing ctrlproxy modules
Summary(pl):	Pliki nag³ówkowe i przyk³ady s³u¿±ce do rozwijania modu³ów ctrlproxy
Group:		Development/Libraries

%description devel
Header files and examples for developing ctrlproxy modules

%description devel -l pl
Pliki nag³ówkowe i przyk³ady s³u¿±ce do rozwijania modu³ów ctrlproxy

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}rc
cp -r example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_prefix}/doc/%{name}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/ctrlproxy.1*
%{_mandir}/man5/ctrlproxyrc.5*
%{_libdir}/%{name}/*

%files devel
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
%{_includedir}/*
