Summary:	-
Summary(pl):	-
Name:		muttprint
Version:	0.52a
Release:	1
License:	GPL
Group:		Applications/Printing
Source0:	%{name}-%{version}.tar.gz
URL:		http://bwalle.exit.mytoday.de/muttprint/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

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
