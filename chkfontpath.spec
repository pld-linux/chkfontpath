Summary:	Simple interface for editing the font path for the X font server.
Summary(pl):	Prosty program do manipulacji ¶cie¿kami fontów dla fontserwera
Name:		chkfontpath
Version:	1.4.1
Release: 	2
Copyright: 	GPL
Group: 		X11/Utilities
Group(pl):	X11/Narzêdzia
BuildRoot: 	/var/tmp/%{name}-%{version}-root
Source: 	%{name}-%{version}.tar.gz
BuildPrereq:	popt-devel
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
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make INSTROOT=$RPM_BUILD_ROOT install

gzip -9fn $RPM_BUILD_ROOT/usr/man/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)/usr/sbin/chkfontpath
/usr/man/man8/chkfontpath.8*

%changelog
* Wed Apr 28 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.4.1-2]
- added full attr description
- gzipped man pages
- added pl translation

* Wed Apr 14 1999 Preston Brown <pbrown@redhat.com>
- preserve permissions on config file

* Thu Apr 07 1999 Preston Brown <pbrown@redhat.com>
- if /proc isn't mounted, don't do a killall

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- don't use psmisc, use pidof from SysVinit

* Fri Mar 12 1999 Preston Brown <pbrown@redhat.com>
- made psmisc a requirement.

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- added "quiet" option.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- injected new group / description.

* Tue Feb 16 1999 Preston Brown <pbrown@redhat.com>
- important fix - kill font server with USR1 instead of HUP.

* Mon Feb 15 1999 Preston Brown <pbrown@redhat.com>
- initial spec file
