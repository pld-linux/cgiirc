%include	/usr/lib/rpm/macros.perl
Summary:	The CGI:IRC, chat on irc through WWW
Summary(pl):	CGI:IRC, rozmowy irc poprzez WWW
Name:		cgiirc
Version:	0.5.4
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/cgiirc/%{name}-%{version}.tar.gz
# Source0-md5:	c32ce6514626729ef8cf30cf7bd1a51e
URL:		http://cgiirc.sourceforge.net/doc.html
BuildRequires:	rpm-perlprov
Requires:	webserver
Provides:	wwwirc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cgidir		/home/services/httpd/cgi-bin

%description
This package contains CGIIRC, a web based interface to irc, it allows
to bypass firewalls with blocked ports other then http, and use irc on
machines without installed client (i.e. internet cafes, offices where
you have no control of installed software etc.). All you need on the
client side is a WWW browser and Internet connection.

%description -l pl
Pakiet ten zawiera CGIWEB, interfejs oparty na WWW do irca, pozwala
na obej¶cie zapór sieciowych blokuj±cych dostêp do portów innych ni¿
http, i u¿ywanie irca na maszynach bez zainstalowanego klienta (np
kafejkach, biurach gdzie nie ma siê wp³ywu na zainstalowane
oprogramowanie). Wszystko co jest wymagane po stronie klienta to
przegl±darka i pod³±czenie do Internetu.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{cgidir}

cp -avR {cgiirc.config,*.cgi,formats,images,interfaces,modules} $RPM_BUILD_ROOT%{cgidir}
cp ipaccess.example $RPM_BUILD_ROOT%{cgidir}/ipaccess

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs
%defattr(755,http,http,755)
%config(noreplace) %verify(not size mtime md5) %{cgidir}/cgiirc.config
%config(noreplace) %verify(not size mtime md5) %{cgidir}/ipaccess
%{cgidir}/*
