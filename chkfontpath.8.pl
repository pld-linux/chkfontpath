.TH CHKFONTPATH 8 "FRI AUG 27 1999"
.UC 4
.SH NAZWA
chkfontpath \- jest prostym programem do dodawania, usuwania i sprawdzania
katalog�w z czcionkami dla fontserwera X-�w.
.SH SK�ADNIA
\fBchkfontpath\fR [--add <katalog>] [--remove <katalog>] [--list] [--help]
.SH OPIS
\fBchkfontpath\fR pozwala na �atw� konfiguracj� katalog�w zawartych
w �cie�ce fontserwera X-�w.  Ju� od Red Hat-a 6.0, wszystkie czcionki w X-ach
s� obs�ugiwane przez ten oddzielny proces fontserwera, a nie przez g��wny
proces X serwera.  Pozwala to na przyspieszenie generowania czcionki oraz
u�ycie fontserwer�w, kt�re nie s� uruchamiane na lokalnym komputerze.

\fBchkfontpath\fR g��wnie jest u�ywany przez \fBrpm\fR w sekcji %post oraz %postun
w celu dodania lub usuni�cia nowych katalog�w do pliku konfiguracyjnego xfs
w trakcie instalacji i deinstalacji pakiet�w zawieraj�cych czcionki.
\fB--add <katalog>\fR dodaje okre�lony katalog do listy z czcionkami.
\fB--remove <katalog>\fR usuwa okre�lony katalog z listy z czcionkami.
Mo�na tak�e sprawdzi� list� aktualnych katalog�w z czcionkami u�ywaj�c \fB--list\fR;
jest to domy�lne zachowanie programu w�wczas, gdy nie zostanie podana �adna opcja.

Podczas dodawania katalog�w do �cie�ki, program uprzednio sprawdza
czy dodawany katalog zawiera plik \fBfonts.dir\fR, kt�ry jest wykorzystywany przez server
do poprawnego generowania czcionek.  Kiedy katalog zostanie poprawnie dodany lub usuni�ty,
proces \fBxfs\fR jest ponownie uruchamiany.

.PD
.SH "KODY ZWROTNE"
\fBchkfontpath\fR zwraca 0 przy poprawnie wykonanej operacji albo 1 w przypadku wyst�pienia b��du.

.SH PLIKI
.PD 0
.TP 20
\fI/etc/X11/fs/config\fR - plik konfiguracyjny dla fontserwera X-�w (xfs)

.PD
.SH "ZOBACZ TAK�E"
.BR xfs (1), fslsfonts (1)

.SH AUTOR
.nf
Preston Brown <pbrown@redhat.com>
.fi
