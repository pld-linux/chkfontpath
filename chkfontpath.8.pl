.TH CHKFONTPATH 8 "FRI AUG 27 1999"
.UC 4
.SH NAZWA
chkfontpath \- jest prostym programem do dodawania, usuwania i sprawdzania
katalogów z czcionkami dla fontserwera X-ów.
.SH SK£ADNIA
\fBchkfontpath\fR [--add <katalog>] [--remove <katalog>] [--list] [--help]
.SH OPIS
\fBchkfontpath\fR pozwala na ³atw± konfiguracjê katalogów zawartych
w ¶cie¿ce fontserwera X-ów.  Ju¿ od Red Hat-a 6.0, wszystkie czcionki w X-ach
s± obs³ugiwane przez ten oddzielny proces fontserwera, a nie przez g³ówny
proces X serwera.  Pozwala to na przyspieszenie generowania czcionki oraz
u¿ycie fontserwerów, które nie s± uruchamiane na lokalnym komputerze.

\fBchkfontpath\fR g³ównie jest u¿ywany przez \fBrpm\fR w sekcji %post oraz %postun
w celu dodania lub usuniêcia nowych katalogów do pliku konfiguracyjnego xfs
w trakcie instalacji i deinstalacji pakietów zawieraj±cych czcionki.
\fB--add <katalog>\fR dodaje okre¶lony katalog do listy z czcionkami.
\fB--remove <katalog>\fR usuwa okre¶lony katalog z listy z czcionkami.
Mo¿na tak¿e sprawdziæ listê aktualnych katalogów z czcionkami u¿ywaj±c \fB--list\fR;
jest to domy¶lne zachowanie programu wówczas, gdy nie zostanie podana ¿adna opcja.

Podczas dodawania katalogów do ¶cie¿ki, program uprzednio sprawdza
czy dodawany katalog zawiera plik \fBfonts.dir\fR, który jest wykorzystywany przez server
do poprawnego generowania czcionek.  Kiedy katalog zostanie poprawnie dodany lub usuniêty,
proces \fBxfs\fR jest ponownie uruchamiany.

.PD
.SH "KODY ZWROTNE"
\fBchkfontpath\fR zwraca 0 przy poprawnie wykonanej operacji albo 1 w przypadku wyst±pienia b³êdu.

.SH PLIKI
.PD 0
.TP 20
\fI/etc/X11/fs/config\fR - plik konfiguracyjny dla fontserwera X-ów (xfs)

.PD
.SH "ZOBACZ TAK¯E"
.BR xfs (1), fslsfonts (1)

.SH AUTOR
.nf
Preston Brown <pbrown@redhat.com>
.fi
