# Wollservice

Der Wollservice bietet die Grundlage für ein Wolle Vergleichsportal. Das Programm wird über 'scraper.py' gestartet. Produkte können über products.csv angepasst werden. Der Wollservice scraped die Verfügbarkeit, den Preis, die Zusammensetzung und die Nadelstärke der Produkte und speichert sie in einer MongoDB Datenbank, sowie in einer CSV Datei. Die gewünschte Ausgabe (Datei/DB) kann im Block `if __name__=="__main__"` der `scraper.py` durch Auskommentieren der jeweiligen Zeile angepasst werden. Die Requirements können über pip installiert werden

# Ideen für Vergleichsportal 

Man könnte die Seite in bestimmten Intervallen abfragen und den Preis in MongoDB als Time-Series abspeichern. Mit den Daten könnte man dem Nutzer im Front-End die Veränderung der Preise anzeigen, z.B. Grün wenn ein Preis gefallen und Rot wenn ein Preis gestiegen ist. Neben einer Website, könnte man eine Mobile-Application erstellen, die Push-Benachrichtigung bei Preisänderungen oder veränderter Verfügbarkeit sendet. Mit etwas mehr Zeit hätte ich einen Telegram Bot gebastelt, der automatisch eine Nachricht schickt, wenn sich ein Preis ändert und über den Befehl /prices eine Tabelle mit den aktuellen Preisen schickt. Die hinterlegten Produkte hätte ich über einen anderen Befehl anpassen lassen.

# Tests

Während der Tests habe ich gemerkt, dass es einen Fehler gibt, sobald Produkte reduziert sind. Mein Programm liest dann den alten Preis aus. Mit mehr Zeit würde ich das angehen. Außerdem konnte ich bisher nur Test-Cases für den scraper erstellen. Mit Mehr Zeit müsste ich das auch ausweiten.

# Ordnerstruktur

Leider sieht die Ordnerstruktur nicht gelungen aus. Ich wollte die Tests in einem seperaten Verzeichnis lagern. Die Struktur sollte wie folgt aussehen:
wollservice
    scripts
        db
        parse
        scraper
        ...
    tests
        db
        parse
        scraper
        ...

Leider konnte ich aus `tests/scraper` nicht die Dateien aus scripts/scraper importieren. Ich hätte hier mit dem Path etwas basteln können, aber das wäre nur auf meinem lokalen Computer lauffähig gewesen. Für relative Imports hätte ich mehr Zeit gebraucht. Das Problem ist nervig und ich konnte keine Lösung finden. Ich verweise auf folgenden [Thread](https://stackoverflow.com/questions/4383571/importing-files-from-different-folder)
