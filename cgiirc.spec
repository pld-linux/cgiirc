%include	/usr/lib/rpm/macros.perl
Summary:	The CGI:IRC, chat on irc through www
Summary(pl):	CGI:IRC, rozmowy irc poprzez www
Name:		cgiirc
Version:	0.5.3
Release:	3
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ed0be082c88b5760ba3818f33b3789e9
URL:		http://cgiirc.sourceforge.net/doc.html
BuildRequires:	rpm-perlprov
Requires:	webserver
Provides:	wwwirc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains CGIIRC, a web based interface to irc, it allows
to bypass firewalls with blocked ports other then http, and use irc on
machines without installed client (i.e. internet cafes, offices where
you have no control of installed software etc.). All you need on the
client side is a www browser and internet connection.

%description -l pl
Pakiet ten zawiera CGIWEB, interfejs oparty na www do irca, pozwala
na obej¶cie zapór sieciowych blokuj±cych dostêp do portów innych ni¿
http, i u¿ywanie irca na maszynach bez zainstalowanego klienta (np
kafejkach, biurach gdzie nie ma siê wp³ywu na zainstalowane
oprogramowanie). Wszystko co jest wymagane po stronie klienta to
przegl±darka i pod³±czenie do internetu.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/srv/httpd/cgi-bin/

cp -avR {cgiirc.config,*.cgi,formats,images,interfaces,modules} $RPM_BUILD_ROOT/srv/httpd/cgi-bin
cp ipaccess.example $RPM_BUILD_ROOT/srv/httpd/cgi-bin/ipaccess

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs
%defattr(755,http,http,755)
%config(noreplace) %verify(not size mtime md5) /srv/httpd/cgi-bin/cgiirc.config
%config(noreplace) %verify(not size mtime md5) /srv/httpd/cgi-bin/ipaccess
/srv/httpd/cgi-bin/*
