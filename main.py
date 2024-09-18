import tkinter as tk
from tkinter import messagebox
import json
import os

def load_contacts():
    if os.path.exists('contacts.json'):
        with open('contacts.json', 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    if not name or not phone:
        messagebox.showerror("Erro", "Nome e telefone são obrigatórios.")
        return
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    update_contact_list()
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def remove_contact():
    selected_contact = listbox_contacts.curselection()
    if not selected_contact:
        messagebox.showerror("Erro", "Selecione um contato para remover.")
        return
    contacts = load_contacts()
    del contacts[selected_contact[0]]
    save_contacts(contacts)
    update_contact_list()

def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    contacts = load_contacts()
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

root = tk.Tk()
root.title("Gerenciador de Contatos")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Telefone:").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame, text="Adicionar Contato", command=add_contact).grid(row=2, columnspan=2, pady=5)

listbox_contacts = tk.Listbox(root, width=50)
listbox_contacts.pack(padx=10, pady=10)

tk.Button(root, text="Remover Contato", command=remove_contact).pack(pady=5)

update_contact_list()

root.mainloop()