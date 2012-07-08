Summary:	Formats the output of mail clients to a good-looking printing
Summary(pl.UTF-8):	Program formatujący wyjście klientów pocztowych w dobrze wyglądający wydruk
Name:		muttprint
Version:	0.73
Release:	1
License:	GPL v2+
Group:		Applications/Printing
Source0:	http://downloads.sourceforge.net/muttprint/%{name}-%{version}.tar.gz
# Source0-md5:	39b76058b838e3078df93236eda2c316
Source1:	%{name}-missing-files.tar.xz
# Source1-md5:	c3d4a8796b85445bc378233c6203e4f2
Patch0:		%{name}-docbook-fixes.patch
URL:		http://muttprint.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	perl-tools-pod
BuildRequires:	tar >= 1:1.22
BuildRequires:	texlive-fonts-stmaryrd
BuildRequires:	texlive-latex-marvosym
BuildRequires:	xz
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
%setup -q -a1
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
# doc/manual build races
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/muttprint

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES NEWS README README.{Gnus,Latex,translations} doc/manual/en/manual-en.html sample-muttprintrc-en
%lang(de) %doc doc/manual/de/manual-de.html sample-muttprintrc-de
%lang(es) %doc README.es doc/manual/es/manual-es.html sample-muttprintrc-es
%lang(fr) %doc sample-muttprintrc-fr
%lang(it) %doc doc/manual/it/manual-it.html sample-muttprintrc-it
%lang(nl) %doc sample-muttprintrc-nl
%lang(sl) %doc doc/manual/sl/manual-sl.html sample-muttprintrc-si
%attr(755,root,root) %{_bindir}/muttprint
%attr(755,root,root) %{_bindir}/muttprint-langinfo
%dir %{_datadir}/muttprint
%{_datadir}/muttprint/*.eps
%{_datadir}/muttprint/*.jpg
%{_datadir}/muttprint/*.png
%{_datadir}/muttprint/README.pics

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

%{_mandir}/man1/muttprint.1*
%lang(de) %{_mandir}/de/man1/muttprint.1*
%lang(es) %{_mandir}/es/man1/muttprint.1*
%lang(it) %{_mandir}/it/man1/muttprint.1*
