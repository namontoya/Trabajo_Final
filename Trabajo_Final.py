import tkinter as tk
from tkinter import messagebox
import os

CONTACT_FILE = "contacts.txt"

def read_contacts():
    contacts = []
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            for line in file:
                name, number = line.strip().split("!")
                contacts.append((name, number))
    return contacts

def create_contact():
    name = entry_name.get()
    number = entry_number.get()

    if name == "" or number == "":
        messagebox.showwarning("Error", "Los campos no pueden estar vacíos.")
        return

    contacts = read_contacts()

    for contact in contacts:
        if contact[0] == name or contact[1] == number:
            messagebox.showwarning("Error", "El contacto ya existe.")
            return

    
    with open(CONTACT_FILE, "a") as file:
        file.write(f"{name}!{number}\n")
    
    messagebox.showinfo("Éxito", "Contacto agregado.")
    clear_fields()
    read_contact_list()

def read_contact_list():
    contacts = read_contacts()
    listbox_contacts.delete(0, tk.END)  # Limpiar la lista
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact[0]} - {contact[1]}")

def update_contact():
    name = entry_name.get()
    number = entry_number.get()

    if name == "" or number == "":
        messagebox.showwarning("Error", "Los campos no pueden estar vacíos.")
        return

    contacts = read_contacts()

    updated = False
    with open(CONTACT_FILE, "w") as file:
        for contact in contacts:
            if contact[0] == name:
                file.write(f"{name}!{number}\n")
                updated = True
            else:
                file.write(f"{contact[0]}!{contact[1]}\n")

    if updated:
        messagebox.showinfo("Éxito", "Contacto actualizado.")
    else:
        messagebox.showwarning("Error", "El contacto no existe.")
    
    clear_fields()
    read_contact_list()

def delete_contact():
    name = entry_name.get()

    if name == "":
        messagebox.showwarning("Error", "El nombre no puede estar vacío.")
        return

    contacts = read_contacts()

    deleted = False
    with open(CONTACT_FILE, "w") as file:
        for contact in contacts:
            if contact[0] == name:
                deleted = True
            else:
                file.write(f"{contact[0]}!{contact[1]}\n")

    if deleted:
        messagebox.showinfo("Éxito", "Contacto eliminado.")
    else:
        messagebox.showwarning("Error", "El contacto no existe.")
    
    clear_fields()
    read_contact_list()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_number.delete(0, tk.END)

root = tk.Tk()
root.title("Agenda de Contactos")

label_name = tk.Label(root, text="Nombre:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_number = tk.Label(root, text="Número:")
label_number.grid(row=1, column=0, padx=10, pady=10)

entry_number = tk.Entry(root)
entry_number.grid(row=1, column=1, padx=10, pady=10)

button_create = tk.Button(root, text="Crear", command=create_contact)
button_create.grid(row=2, column=0, padx=10, pady=10)

button_read = tk.Button(root, text="Mostrar", command=read_contact_list)
button_read.grid(row=2, column=1, padx=10, pady=10)

button_update = tk.Button(root, text="Actualizar", command=update_contact)
button_update.grid(row=3, column=0, padx=10, pady=10)

button_delete = tk.Button(root, text="Eliminar", command=delete_contact)
button_delete.grid(row=3, column=1, padx=10, pady=10)

listbox_contacts = tk.Listbox(root, width=40)
listbox_contacts.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

read_contact_list()

root.mainloop()
