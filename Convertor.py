import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import ffmpeg
import pathlib

def convertUsingFfmpeg(input_file, output_file):
    (
        ffmpeg
        .input(input_file)
        .output(output_file)
        .run()
    )

class DragDropConverter:
    def __init__(self, root):
        self.root = root
        self.input_path = pathlib.Path("")

        self.root.title('Konwerter plików - przeciągnij i upuść')
        self.root.geometry('500x300')  # Zwiększono rozmiar okna
        
        self.label = tk.Label(root, text='Przeciągnij plik tutaj', pady=20, font=('Times 14'))
        self.label.pack(expand=True, fill=tk.BOTH)
        
        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind('<<Drop>>', self.on_drop)

        # Ramka na przyciski i pole tekstowe
        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.BOTTOM, pady=20)

        self.extension_label = tk.Label(self.frame, text="Konwersja na:")
        self.extension_label.pack(side=tk.LEFT)

        self.extension_entry = tk.Entry(self.frame, width=5)
        self.extension_entry.pack(side=tk.LEFT)
        self.extension_entry.insert(0, ".mp4")  # Domyślne rozszerzenie

        self.convert_button = tk.Button(self.frame, text='Konwertuj', command=self.convert, state=tk.DISABLED)
        self.convert_button.pack(side=tk.LEFT, padx=10)

    def on_drop(self, event):
        self.input_path = pathlib.Path(event.data)
        string_input_path = f"{self.input_path}".removeprefix('{').removesuffix('}')
        self.label.config(text=f"Wybrany: {self.input_path.name.removeprefix('{').removesuffix('}')}\nKonwertuj lub załaduj inny plik.")
        print(f"Ścieżka przeciągniętego pliku: {string_input_path}")
        self.convert_button['state'] = tk.NORMAL

    def convert(self):
        extension = self.extension_entry.get()
        string_input_path = f"{self.input_path}".removeprefix('{').removesuffix('}')
        string_output_file = f"{self.input_path.with_suffix(extension)}".removeprefix('{')
        print(f"Zaczynam Konwersje pliku:\n{string_input_path}\nna plik\n {string_output_file}")
        convertUsingFfmpeg(string_input_path,string_output_file)
        print("Konwersja zakończona pomyślnie!")

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = DragDropConverter(root)
    root.mainloop()

    

   