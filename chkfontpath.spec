Summary: Simple interface for editing the font path for the X font server.
Name: chkfontpath
%define version	1.4.1
Version: %{version}
Release: 1
Copyright: GPL
Group: System Environment/Base
BuildRoot: /var/tmp/%{name}-root
Source: %{name}-%{version}.tar.gz
Requires: XFree86-xfs

%description 
This is a simple terminal mode program for adding, removing and listing
the directories contained in the X font server's path. It is mostly
intended to be used 'internally' by RPM when packages with fonts are
added or removed, but it may be useful as a stand-alone utility in
some instances.

%prep
%setup -q

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make INSTROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root)/usr/sbin/chkfontpath
%attr(-,root,root)/usr/man/man8/chkfontpath.8

%changelog
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
