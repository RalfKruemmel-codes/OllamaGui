import asyncio
import subprocess
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.logger import Logger
from response_handler import OllamaResponseHandler


class OllamaChatApp(App):
    """
    Eine Kivy-Anwendung für die Interaktion mit dem Ollama-Chat-Modell.
    Erstellt eine GUI, in der der Benutzer ein Modell auswählen, eine Frage stellen und die Antwort anzeigen kann.
    """

    def build(self):
        """
        Erstellt das GUI-Layout und definiert die Interaktionen.
        """
        self.title = "Ollama KI CHAT"
        Window.size = (800, 600)

        # Startet den Ollama-Server
        self.ollama_process = self.start_ollama_server_process()

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Dropdown für Modell-Auswahl
        self.model_spinner = Spinner(
            text="mistral",  # Standardmäßig auf ein gültiges Modell setzen
            values=("mistral", "llama3.1:8b", "andere Modelle..."),
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.model_spinner)

        # Eingabefeld für die Benutzereingabe
        self.user_input = TextInput(
            hint_text="Gib deine Frage ein...",
            multiline=True,
            size_hint=(1, 0.3)
        )
        layout.add_widget(self.user_input)

        # Button zum Senden der Anfrage
        self.submit_button = Button(
            text="Jetzt Fragen",
            size_hint=(1, 0.1)
        )
        self.submit_button.bind(on_press=self.on_submit)
        layout.add_widget(self.submit_button)

        # TextInput für die Anzeige der Antwort (readonly)
        self.response_textbox = TextInput(
            text="Antwort wird hier angezeigt...",
            multiline=True,
            readonly=True,  # Setzt den TextInput in den Nur-Lesen-Modus
            size_hint=(1, 0.5)
        )
        layout.add_widget(self.response_textbox)

        # Initialisiere den Response-Handler
        self.response_handler = None

        return layout

    def start_ollama_server_process(self):
        """
        Startet den Ollama-Server-Prozess im Hintergrund.

        Rückgabewert:
            process (Popen): Der gestartete Server-Prozess oder None bei Fehlern.
        """
        try:
            process = subprocess.Popen(["ollama", "serve"])
            Logger.info("OllamaChatApp: Ollama-Server erfolgreich gestartet")
            return process
        except FileNotFoundError:
            error_message = "Ollama-Server konnte nicht gefunden werden. Bitte überprüfen Sie die Installation."
            self.handle_error(error_message)
        except Exception as e:
            error_message = f"Ein unerwarteter Fehler ist aufgetreten: {str(e)}"
            self.handle_error(error_message)
        return None

    def stop_ollama_server_process(self):
        """
        Beendet den Ollama-Server-Prozess, falls er läuft.
        """
        if self.ollama_process:
            self.ollama_process.terminate()
            self.ollama_process.wait()
            Logger.info("OllamaChatApp: Ollama-Server erfolgreich beendet")

    def on_submit(self, instance):
        """
        Startet die Verarbeitung der Benutzereingabe.
        """
        asyncio.ensure_future(self.get_response_async())

    async def get_response_async(self):
        """
        Holt die Antwort von der ollama API und zeigt sie in der GUI an.
        """
        user_input = self.user_input.text.strip()  # Validierung der Eingabe
        selected_model = self.model_spinner.text

        if selected_model == "Wähle ein Modell":
            self.display_error("Bitte wähle ein gültiges Modell aus.")
            return

        if not user_input:
            self.display_error("Bitte gib eine Frage ein.")
            return

        self.response_textbox.text = "Antwort wird geladen..."

        # Initialisiere den Response-Handler mit dem ausgewählten Modell
        self.response_handler = OllamaResponseHandler(selected_model)

        response = await self.response_handler.get_response_async(user_input)
        if response:
            self.display_response(response)
        else:
            self.handle_error("Fehler bei der Antwortverarbeitung")

    def display_response(self, response_text):
        """
        Zeigt die erhaltene Antwort im GUI an.
        """
        self.response_textbox.text = response_text

    def display_error(self, error_message):
        """
        Zeigt eine Fehlermeldung im GUI an.
        """
        self.response_textbox.text = error_message

    def handle_error(self, error_message):
        """
        Protokolliert und zeigt Fehlermeldungen im GUI an.
        """
        Logger.error(f"OllamaChatApp: {error_message}")
        self.display_error(error_message)

    def on_stop(self):
        """
        Beendet den Ollama-Server beim Schließen der Anwendung.
        """
        self.stop_ollama_server_process()


if __name__ == "__main__":
    app = OllamaChatApp()
    asyncio.run(app.async_run(async_lib='asyncio'))
