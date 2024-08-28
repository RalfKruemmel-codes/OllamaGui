
# Ollama KI Chat Anwendung

Diese Anwendung ist eine Kivy-basierte GUI, die es Benutzern ermöglicht, mit verschiedenen KI-Modellen von Ollama zu interagieren. Der Benutzer kann ein Modell auswählen, eine Frage stellen und erhält dann eine Antwort, die direkt im Interface angezeigt wird. Die Anwendung startet im Hintergrund einen Ollama-Server, der die Anfragen bearbeitet.

## Features

- **Asynchrone GUI:** Die Benutzeroberfläche bleibt reaktionsfähig, während Anfragen verarbeitet werden.
- **Mehrere Modelle:** Der Benutzer kann zwischen verschiedenen KI-Modellen wählen.
- **Einfaches Layout:** Eine übersichtliche und benutzerfreundliche Oberfläche.
- **Automatische Serververwaltung:** Der Ollama-Server wird beim Start der Anwendung automatisch gestartet und beim Beenden der Anwendung gestoppt.
- **Protokollierung (Logging):** Die Anwendung nutzt Kivy's `Logger` für detaillierte Protokollierung, um das Verhalten der Anwendung zu überwachen und Fehler zu diagnostizieren.

## Installation

### 1. Voraussetzungen

- **Python**: Version 3.7 oder höher muss installiert sein.
- **Kivy**: Die Python-Bibliothek Kivy zur GUI-Entwicklung.
- **Ollama Python Client**: Das offizielle Python-Tool von Ollama.
- **Ollama**: Das Ollama-Tool muss installiert sein, um Modelle zu verwalten und Anfragen zu verarbeiten.

### 2. Abhängigkeiten installieren

Verwenden Sie pip, um die notwendigen Abhängigkeiten zu installieren:

```bash
pip install kivy ollama
```

### 3. Ollama installieren und ein Modell herunterladen

1. **Ollama installieren**:
   - Besuche die [Ollama-Website](https://ollama.ai) und folge den Anweisungen zur Installation des Ollama-Tools.

2. **Modell herunterladen**:
   - Nach der Installation von Ollama kannst du ein Modell herunterladen. Verwende den Befehl:
   
     ```bash
     ollama pull <modellname>
     ```
     Ersetze `<modellname>` durch den Namen des Modells, das du verwenden möchtest, z.B. `mistral` oder `llama3.1:8b`.

3. **Modellpfad konfigurieren**:
   - Stelle sicher, dass der Pfad zum heruntergeladenen Modell korrekt in deiner Umgebung gesetzt ist. Du kannst den Pfad mit dem folgenden Befehl setzen:

     ```bash
     export OLLAMA_MODELS=<pfad-zum-modell>
     ```
     Unter Windows kannst du den Pfad mit `set` setzen:
     
     ```bash
     set OLLAMA_MODELS=<pfad-zum-modell>
     ```

### 4. Projekt klonen

Klone das Repository auf dein lokales System:

```bash
git clone https://github.com/RalfKruemmel-codes/OllamaGui.git
cd OllamaGui
```

### 5. Modellnamen anpassen

Öffne die Datei `OllamaGui.py` und stelle sicher, dass der Name des Modells, das du verwenden möchtest, in der `Spinner`-Auswahl korrekt eingestellt ist. Du kannst dies im Abschnitt `self.model_spinner` ändern:

```python
self.model_spinner = Spinner(
    text="mistral",  # Standardmäßig auf ein gültiges Modell setzen
    values=("mistral", "llama3.1:8b", "andere Modelle..."),
    size_hint=(1, 0.1)
)
```

Ersetze die `values`-Liste durch die Namen der Modelle, die du verwenden möchtest.

## Verwendung

### 1. Starten der Anwendung

Navigiere in das Projektverzeichnis und führe das Python-Skript aus:

```bash
python OllamaGui.py
```

### 2. Interaktion

- Wähle ein Modell aus dem Dropdown-Menü.
- Gib deine Frage in das Textfeld ein.
- Klicke auf "Jetzt Fragen", um eine Antwort vom Modell zu erhalten.

## Projektstruktur

Eine Übersicht über die wichtigsten Dateien und deren Zweck:

- `OllamaGui.py`: Hauptskript für die Kivy-Anwendung.
- `response_handler.py`: Enthält die `OllamaResponseHandler`-Klasse, die für die Kommunikation mit der Ollama-API zuständig ist.
- `OllamaGui.kv`: Definiert das Layout der Anwendung in der Kivy-Language.
- `test_ollama_chat.py`: Enthält Unit-Tests für die Hauptfunktionen der Anwendung.
- `README.md`: Diese Datei, die Informationen zur Anwendung enthält.
- `.gitignore`: Enthält Dateien und Ordner, die vom Versionskontrollsystem ignoriert werden sollen.

## Code-Übersicht

### Hauptkomponenten

- **`OllamaChatApp`**: Die Hauptklasse der Anwendung, die von `kivy.app.App` erbt und das GUI sowie die Logik zur Kommunikation mit dem Ollama-Server enthält.
- **`start_ollama_server_process()`**: Startet den Ollama-Server-Prozess im Hintergrund.
- **`get_response_async()`**: Sendet eine Benutzereingabe asynchron an das ausgewählte Modell und zeigt die Antwort im GUI an.
- **`display_response(response_text)`**: Zeigt die erhaltene Antwort im GUI an.
- **`display_error(error_message)`**: Zeigt Fehlermeldungen im GUI an.
- **`OllamaResponseHandler`**: Eine separate Klasse, die die Kommunikation mit der Ollama-API übernimmt.

### Protokollierung (Logging)

Die Anwendung nutzt die Kivy-eigene `Logger`-Funktion, um wichtige Ereignisse und Fehler zu protokollieren. Dies hilft bei der Überwachung der Anwendung und der Fehlerbehebung. Die Logs können in der Konsole eingesehen werden und sind besonders nützlich bei der Diagnose von Problemen wie:

- Fehler beim Starten des Ollama-Servers
- Fehler bei der Kommunikation mit dem Modell
- Allgemeine Anwendungsfehler

### Beispielcode zur Verwendung

Hier ist ein Beispiel, wie du die Anwendung in einem Python-Skript aufrufen kannst:

```python
from OllamaGui import OllamaChatApp

if __name__ == "__main__":
    app = OllamaChatApp()
    asyncio.run(app.async_run(async_lib='asyncio'))
```

## Fehlerbehebung

Falls du auf Probleme stößt:

1. **Stelle sicher, dass der Ollama-Server korrekt gestartet wird:**
   - Überprüfe die Konsolenausgabe auf Fehler beim Starten des Servers.

2. **Überprüfe die Protokolle (Logs):**
   - Schau dir die Log-Ausgaben in der Konsole an, um Hinweise auf Fehler oder Warnungen zu erhalten.

3. **Überprüfe, ob das Modell korrekt heruntergeladen und konfiguriert ist:**
   - Stelle sicher, dass das Modell korrekt heruntergeladen wurde und der Pfad in der Umgebungsvariablen `OLLAMA_MODELS` gesetzt ist.

4. **Überprüfe deine Python-Umgebung:**
   - Stelle sicher, dass alle Abhängigkeiten korrekt installiert sind.

5. **Weitere Unterstützung:**
   - Öffne ein Issue auf GitHub oder kontaktiere mich über [ralf.kruemmel-python@outlook.de].

## Mitwirkende

- **[Ralf Krümmel](https://github.com/RalfKruemmel-codes)** - Entwicklung und Dokumentation.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe die [LICENSE](LICENSE) Datei für Details.


