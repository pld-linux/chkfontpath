Summary:	Simple interface for editing the font path for the X font server.
Summary(pl):	Prosty program do manipulacji ¶cie¿kami fontów dla fontserwera
Name:		chkfontpath
Version:	1.4.1
Release: 	3
Copyright: 	GPL
Group: 		X11/Utilities
Group(pl):	X11/Narzêdzia
BuildRoot:	/tmp/%{name}-%{version}-root
Source: 	%{name}-%{version}.tar.gz
BuildRequires:	popt-devel
Requires: 	xfs

%description 
This is a simple terminal mode program for adding, removing and listing
the directories contained in the X font server's path. It is mostly
intended to be used 'internally' by RPM when packages with fonts are
added or removed, but it may be useful as a stand-alone utility in
some instances.

%description -l pl
Jest to prosty program pozwalaj±cy na dodawianie, usuwanie i sprawdzanie
katalogów z czcionkami dla fontserwera. Program przeznaczony jest 
przedewszystkim do wewnêtrznego u¿ycia przez RPM kiedy pakiety dodaj± lub 
usuwaj± katalogi z czcionkami, ale mo¿e byæ te¿ u¿ywany samodzielnie.

%prep
%setup -q

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_mandir}/man8

make INSTROOT=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT/usr/man/man8/* $RPM_BUILD_ROOT/%{_mandir}/man8

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_sbindir}/chkfontpath
%{_mandir}/man8/chkfontpath.8*
