import tkinter as tk
from tkinter import ttk

def button_click(button_text_var, button_name):
    print(f"Button {button_name} wurde geklickt")
    button_text_var.set(f"Aktuell gedrückter Button: {button_name}")

def connect_button_click(button_text_var):
    print("Connect-Button wurde geklickt")
    button_text_var.set("Aktuell gedrückter Button: Connect")

def upload_button_click(button_text_var):
    print("Upload-Button wurde geklickt")
    button_text_var.set("Aktuell gedrückter Button: Upload")

def save_shortcut(shortcut_var, entry_widget):
    shortcut = entry_widget.get()
    shortcut_var.set(f"Short-Cut wurde gespeichert: {shortcut}")
    entry_widget.delete(0, tk.END)

# Erstelle Hauptfenster
root = tk.Tk()
root.title("Macro-Keyboard")

# Erstelle gemeinsamen Elternframe
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

# Erstelle StringVar für die Anzeige des gedrückten Buttons
button_text_var = tk.StringVar()
button_text_var.set("Aktuell gedrückter Button: Keiner")

# Erstelle Label für die Anzeige des gedrückten Buttons
label = ttk.Label(main_frame, textvariable=button_text_var)
label.grid(row=1, column=0, pady=10, columnspan=3)

# Erstelle Frame für Connect und Upload Tasten
action_frame = ttk.Frame(main_frame)
action_frame.grid(row=0, column=0, pady=10)

# Erstelle Connect-Button
connect_button = ttk.Button(action_frame, text="Connect", command=lambda: connect_button_click(button_text_var))
connect_button.grid(row=0, column=0, padx=5, pady=3)

# Erstelle Upload-Button
upload_button = ttk.Button(action_frame, text="Upload", command=lambda: upload_button_click(button_text_var))
upload_button.grid(row=1, column=0, padx=5, pady=3)

# Erstelle Frame für die Tasten
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=0, column=1, pady=(20, 0), sticky="ns") 

# Erstelle Tastenfeld (3x3)
for i in range(3):
    for j in range(3):
        button_name = f"Button {i+1}-{j+1}"
        button = ttk.Button(button_frame, text=button_name, command=lambda btn=button_name: button_click(button_text_var, btn))
        button.grid(row=i, column=j, padx=5, pady=5)

# Erstelle Frame für die Eingabe und den "Speichern"-Button
input_frame = ttk.Frame(main_frame)
input_frame.grid(row=0, column=2, padx=(10, 10), pady=(50, 0), sticky="nsew") 

# Erstelle Eingabefeld
entry = ttk.Entry(input_frame)
entry.grid(row=0, column=0, padx=5, pady=5)

# Erstelle "Speichern"-Button
save_button = ttk.Button(input_frame, text="Speichern", command=lambda: save_shortcut(button_text_var, entry))
save_button.grid(row=1, column=0, padx=5, pady=5)

# Erstelle StringVar für die Anzeige des gespeicherten Shortcuts
shortcut_var = tk.StringVar()
shortcut_label = ttk.Label(input_frame, textvariable=shortcut_var)
shortcut_label.grid(row=2, column=0, pady=10)

# Setze das Gewicht für die Zeilen und Spalten, um die Zentrierung zu erreichen
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

# Starte die Tkinter-Schleife
root.mainloop()
