Summary:	Simple interface for editing the font path for the X font server
Summary(es):	Interfaz simple para corregir el camino de las fuentes para el servidor X 
Summary(pl):	Prosty program do manipulacji ╤cie©kami fontСw dla fontserwera
Summary(pt_BR):	Interface simples para editar a rota de fontes do servidor X
Summary(ru):	Простой интерфейс для редактирования пути к шрифтам для Xfs
Summary(uk):	Простий ╕нтерфейс для редагування шляху до шрифт╕в для Xfs
Name:		chkfontpath
Version:	1.9.5
Release:	3
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaГУes
Group(pt):	X11/AplicaГУes
Source0:	%{name}-%{version}.tar.gz
Requires:	xfs
Requires:	/sbin/pidof
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This is a simple terminal mode program for adding, removing and
listing the directories contained in the X font server's path. It is
mostly intended to be used 'internally' by RPM when packages with
fonts are added or removed, but it may be useful as a stand-alone
utility in some instances.

%description -l es
Esto es un programa simple del modo terminal para agregar, quitar y
enumerar los directorios de fuentes del servidor X. Usado internamente
por RPM cuando hace fuentes para agregar o quitar,

%description -l pl
Jest to prosty program pozwalaj╠cy na dodawianie, usuwanie i
sprawdzanie katalogСw z czcionkami dla fontserwera. Program
przeznaczony jest przede wszystkim do wewnЙtrznego u©ycia przez RPM
kiedy pakiety dodaj╠ lub usuwaj╠ katalogi z czcionkami, ale mo©e byФ
te© u©ywany samodzielnie.

%description -l pt_BR
Este И um programa simples para adicionar, remover e listar os
diretСrios de fontes do servidor X. Ele И usado internamente pelo
programa RPM quando instala ou remove pacotes com fontes.

%description -l ru
Это простая программа для конфигурации каталогов в пути поиска сервера
шрифтов системы X window.

Предназначется в основном для `внутреннего' использования, для вызова
из установочных скриптов RPM при добавлении и удалении шрифтов, но в
некоторых случаях может быть полезна и как самостоятельная утилита.

%description -l uk
Це проста програма для конф╕гурац╕╖ каталог╕в в шляху пошуку сервера
шрифт╕в системи X window.

Призначена в основному для `внутр╕шнього' використання, для виклику з
╕нсталяц╕йних скрипт╕в RPM при доданн╕ чи видаленн╕ шрифт╕в, але в
деяких випадках може бути корисною ╕ як самост╕йна утил╕та.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT \
	BINDIR=%{_sbindir} \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_sbindir}/chkfontpath
%{_mandir}/man8/chkfontpath.8*
