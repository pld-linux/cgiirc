%include	/usr/lib/rpm/macros.perl
Summary:	The CGI:IRC, chat on irc through WWW
Summary(pl):	CGI:IRC, rozmowy irc poprzez WWW
Name:		cgiirc
Version:	0.5.7
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/cgiirc/%{name}-%{version}.tar.gz
# Source0-md5:	19dde3e376b461bf601333bf99d923c4
URL:		http://cgiirc.sourceforge.net/
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
na obej�cie zap�r sieciowych blokuj�cych dost�p do port�w innych ni�
http, i u�ywanie irca na maszynach bez zainstalowanego klienta (np
kafejkach, biurach gdzie nie ma si� wp�ywu na zainstalowane
oprogramowanie). Wszystko co jest wymagane po stronie klienta to
przegl�darka i pod��czenie do Internetu.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{cgidir}/%{name}

cp -avR {cgiirc.*,*.cgi,.htaccess,formats,images,interfaces,modules} $RPM_BUILD_ROOT%{cgidir}/%{name}
cp ipaccess.example $RPM_BUILD_ROOT%{cgidir}/%{name}/ipaccess

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*
%dir %{cgidir}/%{name}
%{cgidir}/%{name}/formats
%{cgidir}/%{name}/images
%{cgidir}/%{name}/interfaces
%{cgidir}/%{name}/modules
%{cgidir}/%{name}/.htaccess
%{cgidir}/%{name}/cgiirc.config.full
%config(noreplace) %verify(not size mtime md5) %{cgidir}/%{name}/cgiirc.config
%config(noreplace) %verify(not size mtime md5) %{cgidir}/%{name}/ipaccess
%attr(755,root,root) %{cgidir}/%{name}/*.cgi
