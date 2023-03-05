import tkinter as tk
from tkinter import filedialog
import docx

root = tk.Tk()
root.title("Leitor de Arquivos DOCX")
root.attributes('-topmost', True)

file_path_label = tk.Label(root, text="Caminho do arquivo:")
file_path_label.pack()

file_path_entry = tk.Entry(root, width=50)
file_path_entry.pack()

def select_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Selecione um arquivo", filetypes=[("Arquivos DOCX", "*.docx")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

select_file_button = tk.Button(root, text="Selecionar arquivo", command=select_file)
select_file_button.pack()

def read_file():
    file_path = file_path_entry.get()
    doc = docx.Document(file_path)
    for para in doc.paragraphs:
        listbox.insert(tk.END, para.text)


read_file_button = tk.Button(root, text="Ler arquivo", command=read_file)
read_file_button.pack()

lines_label = tk.Label(root, text="Linhas de texto::")
lines_label.pack()

listbox = tk.Listbox(root, height=20, width=50)
listbox.pack()
root.lift()
root.mainloop()