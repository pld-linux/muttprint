Summary:	Formats the output of mail clients to a good-looking printing
Summary(pl):	Program formatuj±cy wyj¶cie klientów pocztowych w dobrze wygl±daj±cy wydruk
Name:		muttprint
Version:	0.52a
Release:	1
License:	GPL
Group:		Applications/Printing
Group(de):	Applikationen/Drucken
Group(pl):	Aplikacje/Drukowanie
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

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
