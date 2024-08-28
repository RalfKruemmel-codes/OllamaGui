import asyncio
from ollama import chat
from kivy.logger import Logger

class OllamaResponseHandler:
    """
    Diese Klasse kümmert sich um das Senden von Benutzereingaben an die Ollama-API und das Empfangen der Antworten.
    """

    def __init__(self, model_name):
        self.model_name = model_name

    async def get_response_async(self, user_input):
        """
        Sendet eine Benutzereingabe asynchron an die Ollama-API und erhält die Antwort.
        
        Parameter:
            user_input (str): Die Eingabe des Benutzers.

        Rückgabewert:
            str: Die Antwort des Modells oder None bei Fehlern.
        """
        messages = [{'role': 'user', 'content': user_input}]
        response_text = ""

        try:
            for part in chat(self.model_name, messages=messages, stream=True):
                response_text += part['message']['content']
            return response_text
        except Exception as e:
            Logger.error(f"OllamaResponseHandler: Ein Fehler ist aufgetreten: {str(e)}")
            return None
