import tkinter as tk
import ollama

def get_response():
    user_input = user_textbox.get("1.0", "end-1c")
    selected_model = menu_var.get()  # Hier holen wir den ausgewählten Wert
    response = ollama.chat(model=selected_model, messages=[
        {
            'role': 'user',
            'content': user_input,
        },
    ])
    response_textbox.delete("1.0", "end")
    response_textbox.insert("1.0", response['message']['content'])

root = tk.Tk()
root.title("Ollama KI CHAT")

# Menüleiste erstellen
menu_var = tk.StringVar()
menu_var.set("Auswahl")  # Standardwert

menu = tk.OptionMenu(root, menu_var, "codellama:13b", "llava:13b", "llama2-uncensored:7b-chat-fp16", "llama-pro:8b-instruct-fp16" )
menu.config(font=("Helvetica", 16))
menu.pack()


# Textfeld für Benutzereingabe
user_label = tk.Label(root, text="Frage:", fg="red", font=("Helvetica", 24))
user_label.pack()

user_textbox = tk.Text(root, height=8, width=80, bg="black", fg="white", font=("Helvetica", 24))
user_textbox.pack()

# Button zum Ausführen des ausgewählten Codes
submit_button = tk.Button(root, text="Jetzt Fragen", command=get_response, bg="red", fg="black", font=("Helvetica", 24))
submit_button.pack()

# Textfeld für die Antwort
response_label = tk.Label(root, text="Antwort:", fg="red", font=("Helvetica", 24))
response_label.pack()

response_textbox = tk.Text(root, height=8, width=80, bg="black", fg="white", font=("Helvetica", 24))
response_textbox.pack()

root.mainloop()


