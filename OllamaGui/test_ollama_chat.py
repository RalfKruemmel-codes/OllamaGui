import unittest
from OllamaGui import OllamaChatApp
from response_handler import OllamaResponseHandler

class TestOllamaChatApp(unittest.TestCase):

    def setUp(self):
        self.app = OllamaChatApp()
        self.response_handler = OllamaResponseHandler("mistral")

    def test_server_start(self):
        result = self.app.start_ollama_server_process()
        self.assertIsNotNone(result, "Der Server sollte erfolgreich gestartet werden")

    def test_get_response(self):
        response = asyncio.run(self.response_handler.get_response_async("Testnachricht"))
        self.assertIsNotNone(response, "Die Antwort sollte nicht None sein")

if __name__ == "__main__":
    unittest.main()
