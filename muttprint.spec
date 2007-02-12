Summary:	Formats the output of mail clients to a good-looking printing
Summary(pl.UTF-8):   Program formatujący wyjście klientów pocztowych w dobrze wyglądający wydruk
Name:		muttprint
Version:	0.72c
Release:	1
License:	GPL
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/muttprint/%{name}-%{version}.tar.gz
# Source0-md5:	b3e99f8f6f37c0711f6e20f8cf3ef6cb
URL:		http://muttprint.sourceforge.net/
Requires:	perl-Text-Iconv
Requires:	psutils
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Muttprint formats the output of mail clients to a good-looking
printing.

%description -l pl.UTF-8
Muttprint formatuje wyjście klientów pocztowych w dobrze wyglądający
wydruk.

%prep
%setup -q

%{__make} -C langinfo clean

%build
%{__make} -C langinfo \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	sharedir=$RPM_BUILD_ROOT%{_datadir} \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* CHANGES
%attr(755,root,root) %{_bindir}/muttprint
%attr(755,root,root) %{_bindir}/muttprint-langinfo
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
%lang(fi) %{_datadir}/muttprint/translations/translation-fi.pl
%lang(fr) %{_datadir}/muttprint/translations/translation-fr.pl
%lang(hu) %{_datadir}/muttprint/translations/translation-hu.pl
%lang(it) %{_datadir}/muttprint/translations/translation-it.pl
%lang(nl) %{_datadir}/muttprint/translations/translation-nl.pl
%lang(pl) %{_datadir}/muttprint/translations/translation-pl.pl
%lang(pt) %{_datadir}/muttprint/translations/translation-pt.pl
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
