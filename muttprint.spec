Summary:	Formats the output of mail clients to a good-looking printing
Summary(pl):	Program formatuj±cy wyj¶cie klientów pocztowych w dobrze wygl±daj±cy wydruk
Name:		muttprint
Version:	0.53a
Release:	1
License:	GPL
Group:		Applications/Printing
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/muttprint/%{name}-%{version}.tar.gz
URL:		http://muttprint.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Muttprint formats the output of mail clients to a good-looking
printing.

%description -l pl
Muttprint formatuje wyj¶cie klientów pocztowych w dobrze wygl±daj±cy
wydruk.

%prep
%setup  -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    prefix=$RPM_BUILD_ROOT%{_prefix}
    mandir=$RPM_BUILD_ROOT%{_mandir}
    sharedir=$RPM_BUILD_ROOT%{_datadir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755, root, root) %{_bindir}/muttprint
%{_datadir}/muttprint

%doc doc/manual/muttprint-doc-en.html
%lang(es) %doc doc/manual/muttprint-doc-es.html
%lang(it) %doc doc/manual/muttprint-doc-it.html
%lang(de) %doc doc/manual/muttprint-doc-de.html
%{_mandir}/man1/*
%lang(es) %doc %{_mandir}/es/man1/*
%lang(it) %doc %{_mandir}/it/man1/*
%lang(de) %doc %{_mandir}/de/man1/*
