Summary:	Simple interface for editing the font path for the X font server.
Summary(pl):	Prosty program do manipulacji �cie�kami font�w dla fontserwera
Name:		chkfontpath
Version:	1.5
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	popt-devel
Requires:	xfs

%description 
This is a simple terminal mode program for adding, removing and
listing the directories contained in the X font server's path. It is
mostly intended to be used 'internally' by RPM when packages with
fonts are added or removed, but it may be useful as a stand-alone
utility in some instances.

%description -l pl
Jest to prosty program pozwalaj�cy na dodawianie, usuwanie i
sprawdzanie katalog�w z czcionkami dla fontserwera. Program
przeznaczony jest przede wszystkim do wewn�trznego u�ycia przez RPM
kiedy pakiety dodaj� lub usuwaj� katalogi z czcionkami, ale mo�e by�
te� u�ywany samodzielnie.

%prep
%setup -q

%build
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8

%{__make} INSTROOT=$RPM_BUILD_ROOT install
mv -f $RPM_BUILD_ROOT%{_prefix}/man/man8/* $RPM_BUILD_ROOT/%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_sbindir}/chkfontpath
%{_mandir}/man8/chkfontpath.8*
