Summary:	Formats the output of mail clients to a good-looking printing
Summary(pl):	Program formatuj�cy wyj�cie klient�w pocztowych w dobrze wygl�daj�cy wydruk
Name:		muttprint
Version:	0.71
Release:	1
License:	GPL
Group:		Applications/Printing
# Source0-md5:	239c3fd51db6ebf7afc221a23c9a6a7b
Source0:	http://dl.sourceforge.net/muttprint/%{name}-%{version}.tar.gz
URL:		http://muttprint.sourceforge.net/
Requires:	psutils
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Muttprint formats the output of mail clients to a good-looking
printing.

%description -l pl
Muttprint formatuje wyj�cie klient�w pocztowych w dobrze wygl�daj�cy
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
%attr(755,root,root) %{_bindir}/muttprint
%dir %{_datadir}/muttprint
%{_datadir}/muttprint/*.eps
%{_datadir}/muttprint/README.pics

%doc sample-muttprintrc-en
%lang(de) %doc sample-muttprintrc-de
%lang(es) %doc sample-muttprintrc-es
%lang(it) %doc sample-muttprintrc-it

%dir %{_datadir}/muttprint/translations
%lang(cs) %{_datadir}/muttprint/translations/translation-cs.pl
%lang(de) %{_datadir}/muttprint/translations/translation-de.pl
%lang(es) %{_datadir}/muttprint/translations/translation-es.pl
%lang(fr) %{_datadir}/muttprint/translations/translation-fr.pl
%lang(it) %{_datadir}/muttprint/translations/translation-it.pl
%lang(pl) %{_datadir}/muttprint/translations/translation-pl.pl
%lang(ru) %{_datadir}/muttprint/translations/translation-ru.pl
%lang(sl) %{_datadir}/muttprint/translations/translation-sl.pl
%lang(sv) %{_datadir}/muttprint/translations/translation-sv.pl
%{_datadir}/muttprint/translations/translation-example.pl

%doc doc/manual/en/manual-en
%lang(de) %doc doc/manual/de/manual-de
%lang(es) %doc doc/manual/es/manual-es
%lang(it) %doc doc/manual/it/manual-it

%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(it) %{_mandir}/it/man1/*
