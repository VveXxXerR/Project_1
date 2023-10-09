import tkinter as tk
from tkinter import filedialog
import shutil
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def encrypt_folder(): #функция шифрования папки
    folder_path = filedialog.askdirectory()#путь к папке
    if folder_path:
        shutil.make_archive(folder_path, 'zip', folder_path)#папка превращается в архив
        messagebox.showinfo("Шифрование", "Папка успешно зашифрована!")

def decrypt_folder():#функция расшифровки папки
    zip_path = filedialog.askopenfilename(filetypes=[("Zip Files", "*.zip")])#путь к архиву
    if zip_path:
        shutil.unpack_archive(zip_path, './decrypted_folder', 'zip')#распаковка архива в папку
        messagebox.showinfo("Дешифрование", "Папка успешно дешифрована!")

root = tk.Tk() #создаём визуальную оболочку 
root.title("Шифрование/дешифрование папок")#Добавляем название на рамке окна 
root.geometry('900x500') # указываем размер окна 

label = Label(text = 'Шифрование/дешифрование папок', font = '40', background = 'orange') # предустановки для заголовка  
label.pack(anchor = 'n')# добавление заголовка 

encrypt_button = tk.Button(root, text="Зашифровать папку", command=encrypt_folder)# предустановки для кнопок
decrypt_button = tk.Button(root, text="Расшифровать папку", command=decrypt_folder)
encrypt_button.configure(width = 40, height = 4, font = 'timesnewroman 12', foreground = 'black', background = 'orange')# добавление кнопки 
decrypt_button.pack(pady = 100, anchor = NW)
decrypt_button.configure(width = 40, height = 4, font = 'timesnewroman 12', foreground = 'black', background = 'orange')
encrypt_button.pack(anchor = NW)

canvas = Canvas(bg = 'white', width = '300', height = '400')# предустановки для  холста 
canvas.pack(anchor = 'e')# добавление холста в правый нижний угол 

canvas.create_text(200, 60, text = 'Decrypting and encrypting machine', fill = '#f0b111', anchor = 'ne')# создание текста на холсте

canvas.create_text(150, 50, text = 'Frontend developed by Kudrya Yuriy ', fill = '#f0b111', anchor = 'center')#

canvas.create_text(110, 40, text = 'Backend developed by Guty Bogdan ', fill = '#f0b111', anchor = 's')#

root.mainloop()# запуск визуальной оболочки



'''
Developed by Потные ребята
'''
