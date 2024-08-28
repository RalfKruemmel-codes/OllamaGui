import asyncio
import subprocess
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.logger import Logger  # Für Protokollierung
from ollama import chat


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
        self.ollama_process = self.start_ollama_serve()

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Dropdown für Modell-Auswahl
        self.model_spinner = Spinner(
            text="Wähle ein Modell",
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

        return layout

    def start_ollama_serve(self):
        """
        Startet den Ollama-Server-Prozess im Hintergrund.

        Rückgabewert:
            process (Popen): Der gestartete Server-Prozess oder None bei Fehlern.
        """
        try:
            process = subprocess.Popen(["ollama", "serve"])
            Logger.info("OllamaChatApp: Ollama-Server erfolgreich gestartet")
            return process
        except Exception as e:
            error_message = f"Ein Fehler ist beim Starten des Servers aufgetreten: {str(e)}"
            Logger.error(f"OllamaChatApp: {error_message}")
            self.response_textbox.text = error_message
            return None

    def stop_ollama_serve(self):
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
        self.get_response()

    def get_response(self):
        """
        Holt die Antwort von der ollama API und zeigt sie in der GUI an.
        """
        user_input = self.user_input.text.strip()
        selected_model = self.model_spinner.text

        if selected_model == "Wähle ein Modell":
            self.response_textbox.text = "Bitte wähle ein Modell aus."
            return

        if not user_input:
            self.response_textbox.text = "Bitte gib eine Frage ein."
            return

        self.response_textbox.text = "Antwort wird geladen..."

        try:
            messages = [{'role': 'user', 'content': user_input}]
            response_text = ""

            for part in chat(selected_model, messages=messages, stream=True):
                response_text += part['message']['content']
                self.response_textbox.text = response_text  # Aktualisiert die Antwort in der GUI

            Logger.info("OllamaChatApp: Antwort erfolgreich empfangen und angezeigt")
        except Exception as e:
            error_message = f"Ein Fehler ist aufgetreten: {str(e)}"
            Logger.error(f"OllamaChatApp: {error_message}")
            self.response_textbox.text = error_message

    def on_stop(self):
        """
        Beendet den Ollama-Server beim Schließen der Anwendung.
        """
        self.stop_ollama_serve()


if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    asyncio.ensure_future(OllamaChatApp().async_run(async_lib='asyncio'))
    loop.run_forever()
