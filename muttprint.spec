Summary:	Formats the output of mail clients to a good-looking printing
Summary(pl):	Program formatuj±cy wyj¶cie klientów pocztowych w dobrze wygl±daj±cy wydruk
Name:		muttprint
Version:	0.63a
Release:	2
License:	GPL
Group:		Applications/Printing
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/muttprint/%{name}-%{version}.tar.gz
URL:		http://muttprint.sourceforge.net/
Requires:	tetex-latex
Requires:	psutils
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
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    mandir=$RPM_BUILD_ROOT%{_mandir} \
    sharedir=$RPM_BUILD_ROOT%{_datadir} \
    docdir=$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* CHANGES
%attr(755, root, root) %{_bindir}/muttprint
%{_datadir}/muttprint

%doc sample-muttprintrc-en
%lang(de) %doc sample-muttprintrc-de
%lang(es) %doc sample-muttprintrc-es
%lang(it) %doc sample-muttprintrc-it

%lang(cs) %{_libdir}/muttprint/translation-cs.pl
%lang(de) %{_libdir}/muttprint/translation-de.pl
%lang(es) %{_libdir}/muttprint/translation-es.pl
%lang(fr) %{_libdir}/muttprint/translation-fr.pl
%lang(it) %{_libdir}/muttprint/translation-it.pl
%lang(pl) %{_libdir}/muttprint/translation-pl.pl
%lang(si) %{_libdir}/muttprint/translation-si.pl
%lang(sv) %{_libdir}/muttprint/translation-sv.pl
%{_libdir}/muttprint/translation-example.pl

%doc doc/manual/en/manual-en
%lang(de) %doc doc/manual/de/manual-de
%lang(es) %doc doc/manual/es/manual-es
%lang(it) %doc doc/manual/it/manual-it

%{_mandir}/man1/*
%lang(cs) %doc %{_mandir}/cs/man1/*
%lang(de) %doc %{_mandir}/de/man1/*
%lang(es) %doc %{_mandir}/es/man1/*
%lang(it) %doc %{_mandir}/it/man1/*
