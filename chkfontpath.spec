Summary:	Simple interface for editing the font path for the X font server
Summary(es):	Interfaz simple para corregir el camino de las fuentes para el servidor X
Summary(pl):	Prosty program do manipulacji �cie�kami font�w dla fontserwera
Summary(pt_BR):	Interface simples para editar a rota de fontes do servidor X
Summary(ru):	������� ��������� ��� �������������� ���� � ������� ��� Xfs
Summary(uk):	������� ��������� ��� ����������� ����� �� ����Ԧ� ��� Xfs
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

%description -l es
Esto es un programa simple del modo terminal para agregar, quitar y
enumerar los directorios de fuentes del servidor X. Usado internamente
por RPM cuando hace fuentes para agregar o quitar,

%description -l pl
Jest to prosty program pozwalaj�cy na dodawanie, usuwanie i
sprawdzanie katalog�w z czcionkami dla fontserwera. Program
przeznaczony jest przede wszystkim do wewn�trznego u�ycia przez RPM
kiedy pakiety dodaj� lub usuwaj� katalogi z czcionkami, ale mo�e by�
te� u�ywany samodzielnie.

%description -l pt_BR
Este � um programa simples para adicionar, remover e listar os
diret�rios de fontes do servidor X. Ele � usado internamente pelo
programa RPM quando instala ou remove pacotes com fontes.

%description -l ru
��� ������� ��������� ��� ������������ ��������� � ���� ������ �������
������� ������� X window.

�������������� � �������� ��� `�����������' �������������, ��� ������
�� ������������ �������� RPM ��� ���������� � �������� �������, �� �
��������� ������� ����� ���� ������� � ��� ��������������� �������.

%description -l uk
�� ������ �������� ��� ���Ʀ����æ� ������Ǧ� � ����� ������ �������
����Ԧ� ������� X window.

���������� � ��������� ��� `����Ҧ������' ������������, ��� ������� �
�������æ���� �����Ԧ� RPM ��� �����Φ �� �������Φ ����Ԧ�, ��� �
������ �������� ���� ���� �������� � �� �����Ԧ��� ���̦��.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc}

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
