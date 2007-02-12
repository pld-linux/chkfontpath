Summary:	Simple interface for editing the font path for the X font server
Summary(es.UTF-8):	Interfaz simple para corregir el camino de las fuentes para el servidor X
Summary(pl.UTF-8):	Prosty program do manipulacji ścieżkami fontów dla fontserwera
Summary(pt_BR.UTF-8):	Interface simples para editar a rota de fontes do servidor X
Summary(ru.UTF-8):	Простой интерфейс для редактирования пути к шрифтам для Xfs
Summary(uk.UTF-8):	Простий інтерфейс для редагування шляху до шрифтів для Xfs
Name:		chkfontpath
Version:	1.9.5
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	7b954b2e2c79aa5a963d6b4723097811
Source1:	%{name}.8.pl
BuildRequires:	popt-devel
Requires:	xfs
Requires:	/sbin/pidof
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple terminal mode program for adding, removing and
listing the directories contained in the X font server's path. It is
mostly intended to be used 'internally' by RPM when packages with
fonts are added or removed, but it may be useful as a stand-alone
utility in some instances.

%description -l es.UTF-8
Esto es un programa simple del modo terminal para agregar, quitar y
enumerar los directorios de fuentes del servidor X. Usado internamente
por RPM cuando hace fuentes para agregar o quitar,

%description -l pl.UTF-8
Jest to prosty program pozwalający na dodawanie, usuwanie i
sprawdzanie katalogów z czcionkami dla fontserwera. Program
przeznaczony jest przede wszystkim do wewnętrznego użycia przez RPM
kiedy pakiety dodają lub usuwają katalogi z czcionkami, ale może być
też używany samodzielnie.

%description -l pt_BR.UTF-8
Este é um programa simples para adicionar, remover e listar os
diretórios de fontes do servidor X. Ele é usado internamente pelo
programa RPM quando instala ou remove pacotes com fontes.

%description -l ru.UTF-8
Это простая программа для конфигурации каталогов в пути поиска сервера
шрифтов системы X window.

Предназначется в основном для `внутреннего' использования, для вызова
из установочных скриптов RPM при добавлении и удалении шрифтов, но в
некоторых случаях может быть полезна и как самостоятельная утилита.

%description -l uk.UTF-8
Це проста програма для конфігурації каталогів в шляху пошуку сервера
шрифтів системи X window.

Призначена в основному для `внутрішнього' використання, для виклику з
інсталяційних скриптів RPM при доданні чи видаленні шрифтів, але в
деяких випадках може бути корисною і як самостійна утиліта.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man8

%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT \
	BINDIR=%{_sbindir} \
	MANDIR=%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/chkfontpath
%{_mandir}/man8/chkfontpath.8*
