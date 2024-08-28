# Ollama KI Chat Anwendung

Diese Anwendung ist eine Kivy-basierte GUI, die es Benutzern ermöglicht, mit verschiedenen KI-Modellen von Ollama zu interagieren. Der Benutzer kann ein Modell auswählen, eine Frage stellen und erhält dann eine Antwort, die direkt im Interface angezeigt wird. Die Anwendung startet im Hintergrund einen Ollama-Server, der die Anfragen bearbeitet.

## Features

- **Asynchrone GUI:** Die Benutzeroberfläche bleibt reaktionsfähig, während Anfragen verarbeitet werden.
- **Mehrere Modelle:** Der Benutzer kann zwischen verschiedenen KI-Modellen wählen.
- **Einfaches Layout:** Eine übersichtliche und benutzerfreundliche Oberfläche.
- **Automatische Serververwaltung:** Der Ollama-Server wird beim Start der Anwendung automatisch gestartet und beim Beenden der Anwendung gestoppt.

## Installation

1. **Voraussetzungen:**
   - Python 3.7 oder höher
   - Kivy
   - Ollama Python Client

2. **Abhängigkeiten installieren:**

   Verwenden Sie pip, um die notwendigen Abhängigkeiten zu installieren:

   ```bash
   pip install kivy ollama
   ```

3. **Projekt klonen:**

   Klone das Repository auf dein lokales System:

   ```bash
   git clone https://github.com/RalfKruemmel-codes/OllamaGui.git
   cd OllamaGui
   ```

## Verwendung

1. **Starten der Anwendung:**

   Navigiere in das Projektverzeichnis und führe das Python-Skript aus:

   ```bash
   python OllamaGui.py
   ```

2. **Interaktion:**

   - Wähle ein Modell aus dem Dropdown-Menü.
   - Gib deine Frage in das Textfeld ein.
   - Klicke auf "Jetzt Fragen", um eine Antwort vom Modell zu erhalten.

## Dateien im Repository

- `OllamaGui.py`: Hauptskript für die Kivy-Anwendung.
- `README.md`: Diese Datei, die Informationen zur Anwendung enthält.
- `.gitignore`: Enthält Dateien und Ordner, die vom Versionskontrollsystem ignoriert werden sollen.

## Fehlerbehebung

Falls du auf Probleme stößt:

1. **Stelle sicher, dass der Ollama-Server korrekt gestartet wird:**
   - Überprüfe die Konsolenausgabe auf Fehler beim Starten des Servers.

2. **Überprüfe deine Python-Umgebung:**
   - Stelle sicher, dass alle Abhängigkeiten korrekt installiert sind.

3. **Weitere Unterstützung:**
   - Öffne ein Issue auf GitHub oder kontaktiere mich über [ralf.kruemmel-python@outlook.de].

## Mitwirkende

- **[Ralf Krümmel]** - Entwicklung und Dokumentation.

## Lizenz

