# Wollservice

Der Wollservice bietet die Grundlage für ein Wolle Vergleichsportal. Das Programm wird über 'scraper.py' gestartet. Produkte können über products.csv angepasst werden. Der Wollservice scraped die Verfügbarkeit, den Preis, die Zusammensetzung und die Nadelstärke der Produkte und speichert sie in einer MongoDB Datenbank, sowie in einer CSV Datei. Die gewünschte Ausgabe (Datei/DB) kann im Block `if __name__=="__main__"` der `scraper.py` durch Auskommentieren der jeweiligen Zeile angepasst werden. Die Requirements können über pip installiert werden

# Ideen für Vergleichsportal 

Man könnte die Seite in bestimmten Intervallen abfragen und den Preis in MongoDB als Time-Series abspeichern. Mit den Daten könnte man dem Nutzer im Front-End die Veränderung der Preise anzeigen, z.B. Grün wenn ein Preis gefallen und Rot wenn ein Preis gestiegen ist. Neben einer Website, könnte man eine Mobile-Application erstellen, die Push-Benachrichtigung bei Preisänderungen oder veränderter Verfügbarkeit sendet. Mit etwas mehr Zeit hätte ich einen Telegram Bot gebastelt, der automatisch eine Nachricht schickt, wenn sich ein Preis ändert und über den Befehl /prices eine Tabelle mit den aktuellen Preisen schickt. Die hinterlegten Produkte hätte ich über einen anderen Befehl anpassen lassen.
