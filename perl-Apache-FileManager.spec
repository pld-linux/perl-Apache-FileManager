#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	FileManager
Summary:	Apache::FileManager - Apache mod_perl File Manager
Summary(pl):	Apache::FileManager - zarz�dca plik�w oparty na Apache i mod_perl
Name:		perl-Apache-FileManager
Version:	0.19
Release:	1
License:	?
Group:		Applications/Shells
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9215148e78d20b3ef9774210d08daf3
URL:		http://freshmeat.net/projects/apache-filemanager/
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	rc-scripts
%if %{with tests}
BuildRequires:	perl(Apache::Constants) >= 1.09
BuildRequires:	perl(Apache::File) >= 1.01
BuildRequires:	perl(Apache::Request)
BuildRequires:	perl(Apache::Util)
BuildRequires:	perl(File::NCopy) >= 0.32
BuildRequires:	perl(File::Remove) >= 0.2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache::FileManager module is a simple HTML file manager. It
provides file manipulations such as cut, copy, paste, delete, rename,
extract archive, create directory, create file, edit file, and upload
files. It also has the ability to rsync the server htdocs tree to
another server with the click of a button.

%description -l pl
Modu� Apache::FileManager to prosty zarz�dca plik�w HTML. Udost�pnia
operacje na plikach takie jak wycinanie, kopiowanie, wstawianie,
usuwanie, zmiana nazw, rozpakowywanie archiw�w, tworzenie katalog�w,
tworzenie plik�w, modyfikowanie plik�w oraz wysy�anie (upload) plik�w.
Ma tak�e mo�liwo�� rsyncowania drzewa htdocs z serwera na inny serwer
poprzez klikni�cie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Apache/FileManager.pm
