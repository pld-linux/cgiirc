%include	/usr/lib/rpm/macros.perl
Summary:	The CGI:IRC, chat on irc through www
Summary(pl):	CGI:IRC, rozmowy irc poprzez www
Name:		cgiirc
Version:	0.4.2
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	980d241a295c724a8c5b1a04370c35f2
URL:		http://cgiirc.sourceforge.net/doc.html
BuildRequires:	rpm-perlprov
Requires:	webserver
Provides:	wwwirc
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains CGIIRC, a web based interface to irc, it allows
to bypass firewalls with blocked ports other then http, and use irc on
machines without installed client (i.e. internet cafes, offices where
you have no control of installed software etc.). All you need on the
client side is a www browser and internet connection.

%description -l pl
Pakitet ten zawiera CGIWEB, interfejs oparty na www do irca, pozwala
na obej¶cie zapór sieciowych blokuj±cych dostêp do portów innych ni¿
http, i u¿ywanie irca na maszynach bez zainstalowanego klienta (np
kafejkach, biurach gdzie nie ma siê wp³ywu na zainstalowane
oprogramowanie). Wszystko co jest wymagane po stronie klienta to
przegl±darka i pod³±czenie do internetu.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/services/httpd/{html/%{name},cgi-bin/formats} \
	$RPM_BUILD_ROOT%{_datadir}/docs/%{name}

install html/*  $RPM_BUILD_ROOT/home/services/httpd/html/%{name}
cp -avR cgi-bin/* $RPM_BUILD_ROOT/home/services/httpd/cgi-bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README TODO doc.html
%defattr(755,http,http,755)
%config(noreplace) %verify(not size mtime md5) /home/services/httpd/cgi-bin/config
%config(noreplace) %verify(not size mtime md5) /home/services/httpd/cgi-bin/ipaccess
/home/services/httpd/html/%{name}
/home/services/httpd/cgi-bin/*.cgi
