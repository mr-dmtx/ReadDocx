import tkinter as tk
from tkinter import filedialog
import docx
import pypdf
import sys, fitz

root = tk.Tk()
root.title("Leitor de Arquivos DOCX")
root.attributes('-topmost', True)

file_path_label = tk.Label(root, text="Caminho do arquivo:")
file_path_label.pack()

file_path_entry = tk.Entry(root, width=50)
file_path_entry.pack()

def select_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Selecione um arquivo", filetypes=[("Arquivos DOCX ou PDF", ".docx .pdf")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

select_file_button = tk.Button(root, text="Selecionar arquivo", command=select_file)
select_file_button.pack()

def read_file():
    if(file_path_entry.get().find(".pdf") > 0):
        read_file_pdf()
    else:
        read_file_docx()

def read_file_docx():
    file_path = file_path_entry.get()
    doc = docx.Document(file_path)
    for para in doc.paragraphs:
        listbox.insert(tk.END, para.text)

def read_file_pdf():
    doc = fitz.open(file_path_entry.get())
    for page in doc:
        text = page.get_text()
        lines = text.split('\n')
        for line in lines:
            listbox.insert(tk.END, line)

read_file_button = tk.Button(root, text="Ler arquivo", command=read_file)
read_file_button.pack()

lines_label = tk.Label(root, text="Linhas de texto::")
lines_label.pack()

listbox = tk.Listbox(root, height=20, width=50)
listbox.pack()
root.lift()
root.mainloop()