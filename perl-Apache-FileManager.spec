Summary:	Apache module: File Manager
Summary(pl):	Modu³ Apache'a: Zarz±dca plików
Name:		Apache-FileManager
Version:	0.19
Release:	0.1
License:	dunno
Group:		Networking/Daemons
Source0:	http://www.cpan.org/modules/by-module/Apache/PMC/%{name}-%{version}.tar.gz
# Source0-md5:	c9215148e78d20b3ef9774210d08daf3
URL:		http://freshmeat.net/projects/apache-filemanager/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache::FileManager module is a simple HTML file manager. It
provides file manipulations such as cut, copy, paste, delete, rename,
extract archive, create directory, create file, edit file, and upload
files. It also has the ability to rsync the server htdocs tree to
another server with the click of a button.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor
%{__make} \
        OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man3
install blib/man3/* $RPM_BUILD_ROOT%{_mandir}/man3/Apache-FileManager.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service apache restart

%postun
%service apache restart

%defattr(644,root,root,755)
%doc Changes
%{_mandir}/man3/*
