from math import gcd
from collections import Counter

# Funktion zur Identifikation von 3er-Paaren im Eingabetext
def finde_3er_paare(input_str):
    gefunden = set()  # Menge für gefundene 3er-Paare
    gefunden_haeufigkeit = []  # Liste für die Häufigkeiten der Vorkommen

    # Schleife durch den String für 3er-Paare
    for i in range(len(input_str) - 2):
        aktuelles_3er_paar = input_str[i: i + 3]

        # Überprüfen, ob das Paar bereits gefunden wurde
        if aktuelles_3er_paar not in gefunden:
            gefunden.add(aktuelles_3er_paar)
            gefunden_haeufigkeit.append(1)

            # Zählung der Vorkommen
            gefunden_haeufigkeit[-1] += input_str[i + 3:].count(aktuelles_3er_paar)

    # Entfernen von Einzelvorkommen
    gefunden = [paar for paar, haeufigkeit in zip(gefunden, gefunden_haeufigkeit) if haeufigkeit != 1]

    return gefunden

# Funktion zur Berechnung der Abstände zwischen gefundenen 3er-Paaren
def berechne_abstaende(input_str, gefunden_paare):
    abstaende = set()  # Ein Set, um sicherzustellen, dass die Abstände eindeutig sind
    for paar in gefunden_paare:
        positionen = [pos for pos, char in enumerate(input_str) if input_str[pos:pos+3] == paar]
        if len(positionen) > 1:  # Nur wenn das Paar mehr als einmal vorkommt
            abstaende.update([positionen[i+1] - positionen[i] for i in range(len(positionen)-1)])

    # Sortieren der Abstände und Rückgabe
    sortierte_abstaende = sorted(abstaende)
    return sortierte_abstaende

# Funktion zum Finden von Teilern einer Zahl, ausgenommen 1 und 2
def finde_teiler_ohne_1_2(zahl):
    teiler = []
    for i in range(3, zahl + 1):
        if zahl % i == 0:
            teiler.append(i)
    return teiler

# Funktion zum Finden gemeinsamer Teiler und ihrer Häufigkeiten
def finde_teiler_und_haeufigkeiten(zahlen):
    gemeinsamer_teiler = gcd(*zahlen)

    teiler_und_haeufigkeiten = Counter()

    # Iteration durch die Zahlen für die Teiler
    for zahl in zahlen:
        teiler = finde_teiler_ohne_1_2(zahl)
        teiler_und_haeufigkeiten.update(teiler)

    # Ignorieren von Teiler 1 und 2
    del teiler_und_haeufigkeiten[1]
    del teiler_und_haeufigkeiten[2]

    # Teiler und Häufigkeiten in zwei Listen aufteilen
    teiler_liste, haeufigkeiten_liste = zip(*[(t, h) for t, h in teiler_und_haeufigkeiten.items() if h != 1])

    # Sortieren der Listen nach der Häufigkeit
    sortierte_listen = sorted(zip(haeufigkeiten_liste, teiler_liste), reverse=False)
    haeufigkeiten_liste, teiler_liste = zip(*sortierte_listen)

    return teiler_liste, haeufigkeiten_liste

# Funktion zum Aufteilen des Textes entsprechend der Schlüssellänge
def split_input_text(schluessel_laenge, input_str):
    input_split = [""] * schluessel_laenge

    # Aufteilen des Eingabetextes entsprechend der Schlüssellänge
    for i in range(len(input_str)):
        index = i % schluessel_laenge
        input_split[index] += input_str[i]

    input_split = [teil for teil in input_split if teil]
    return input_split

# Funktion zur Caesar-Entschlüsselung
def caesar_entschluesseln(geheimtext, verschiebung):
    klartext = ""
    for zeichen in geheimtext:
        if zeichen.isalpha():
            if zeichen.isupper():
                # Berechnung des entschlüsselten Zeichens für Großbuchstaben
                entschluesseltes_zeichen = chr((ord(zeichen) - verschiebung - 65) % 26 + 65)
            else:
                # Berechnung des entschlüsselten Zeichens für Kleinbuchstaben
                entschluesseltes_zeichen = chr((ord(zeichen) - verschiebung - 97) % 26 + 97)
            klartext += entschluesseltes_zeichen
        else:
            klartext += zeichen
    return klartext

# Funktion zur Findung der wahrscheinlichsten Verschiebung für Caesar-Entschlüsselung
def finde_wahrscheinlichste_verschiebung(text):
    alphabet_tabelle = []

    # Erstellung einer Tabelle mit dem Alphabet für die Berechnung der Buchstabenwahrscheinlichkeiten
    for char in range(ord('A'), ord('Z') + 1):
        alphabet_tabelle.append([chr(char)])
    
    # Wahrscheinlichkeiten für die Häufigkeit der Buchstaben im Englischen
    buchstaben_wahrscheinlichkeit = [6.51, 1.89, 3.06, 5.08, 17.4, 1.66, 3.01, 4.76, 7.55, 0.27, 1.21, 3.44, 2.53, 9.78, 2.51, 0.79, 0.02, 7.00, 7.27, 6.15, 4.35, 0.67, 1.89, 0.003, 0.04, 1.13]
    differenz_aller_verschiebungen = []

    # Für alle 26 möglichen Verschiebungen
    for verschiebung in range(25):
        differenz = 0
        wahrscheinlichkeit_aller_buchstaben = []
        entschluesselter_text = caesar_entschluesseln(text, verschiebung)

        # Für alle 26 Buchstaben
        for buchstabe in range(25):
            anzahl_von_buchstaben = 0

            # Für alle Zeichen im entschlüsselten Text
            for zeichen in entschluesselter_text:
                if zeichen.upper() == alphabet_tabelle[buchstabe][0]:
                    anzahl_von_buchstaben += 1

            prozentzahl = anzahl_von_buchstaben / len(text) * 100
            wahrscheinlichkeit_aller_buchstaben.append(prozentzahl)

        # Berechnung der Differenz zwischen den erwarteten und tatsächlichen Wahrscheinlichkeiten
        for i in range(25):
            differenz = differenz + abs(buchstaben_wahrscheinlichkeit[i] - wahrscheinlichkeit_aller_buchstaben[i])
        differenz_aller_verschiebungen.append(differenz)

    # Sortierung der Verschiebungen nach Differenz (je kleiner, desto besser)
    sortiertes_alphabet = sorted(zip(differenz_aller_verschiebungen, alphabet_tabelle), reverse=False)
    return sortiertes_alphabet[0]

# Hauptprogrammstart, falls die Datei direkt ausgeführt wird
if __name__ == "__main__":
    schluesselwort = ""
    # Benutzereingabe für den zu entschlüsselnden Text
    input_str = input("Gib deinen Text ein (Bitte schon normalisiert): ")

    # Identifikation der 3er-Paare im Text
    gefunden_paare = finde_3er_paare(input_str)

    # Berechnung der Abstände zwischen den gefundenen Paaren
    abstaende = berechne_abstaende(input_str, gefunden_paare)

    # Identifikation von gemeinsamen Teilern und deren Häufigkeiten
    teiler_liste, haeufigkeiten_liste = finde_teiler_und_haeufigkeiten(abstaende)

    # Ausgabe der gefundenen Teiler und ihrer Häufigkeiten
    for i in range(len(teiler_liste)):
        print("DIe Schlüssellänge", teiler_liste[i], "hat die Häufigkeit:", haeufigkeiten_liste[i])

    # Benutzereingabe für die Auswahl der Schlüssellänge
    schluessel_laenge = int(input("Wähle eine Schlüssellänge (muss nicht immer die mit der höchsten Wahrscheinlichkeit sein): "))
    
    # Aufteilen des Textes in Teile entsprechend der Schlüssellänge
    text_split = split_input_text(schluessel_laenge, input_str)
    
    # Iteration durch die aufgeteilten Textteile  
    for i, text in enumerate(text_split):
        # Finden der wahrscheinlichsten Verschiebung für jeden Textteil
        wahrscheinlichste_verschiebung = finde_wahrscheinlichste_verschiebung(text)
        schluesselwort += str(wahrscheinlichste_verschiebung[1])
        bereinigtes_schluesselwort = schluesselwort.replace("[", "").replace("]", "").replace("'", "")
        # Ausgabe der Ergebnisse
        print("Die wahrscheinlichste Verschiebung für Stelle", (i + 1), "ist:", wahrscheinlichste_verschiebung[1])
    print("Das Schlüsselwort ist warscheinlich: " , bereinigtes_schluesselwort)
