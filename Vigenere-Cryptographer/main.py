from tkinter import *
from tkinter import messagebox as mb

def vigenere_encrypt_text():
    """Шифрование текста методом Виженера."""

    # Получаем текст и ключ шифрования
    text = text_entry.get()
    key = shift_entry.get()

    # Проверяем, что текст и ключ не пустые
    if not text or not key:
        mb.showerror('Ошибка', 'Введите текст и ключ шифрования')
        return

    # Приводим текст и ключ к верхнему регистру
    text = text.upper()
    key = key.upper()

    # Шифруем текст
    result = ''
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            case = str.isupper(char)
            char_code = ord(char) - ord('А')
            key_code = ord(key[i % len(key)]) - ord('А')
            new_code = (char_code + key_code) % 32  # 32 буквы в русском алфавите
            new_char = chr(new_code + ord('А'))
            if not case:
                new_char = new_char.lower()
            result += new_char
        else:
            result += char

    # Выводим результат
    result_entry.delete(0, END)
    result_entry.insert(0, result)


def vigenere_decrypt_text():
    """Расшифрование текста методом Виженера."""

    # Получаем текст и ключ шифрования
    text = text_entry.get()
    key = shift_entry.get()

    # Проверяем, что текст и ключ не пустые
    if not text or not key:
        mb.showerror('Ошибка', 'Введите текст и ключ шифрования')
        return

    # Приводим текст и ключ к верхнему регистру
    text = text.upper()
    key = key.upper()

    # Расшифровываем текст
    result = ''
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            case = str.isupper(char)
            char_code = ord(char) - ord('А')
            key_code = ord(key[i % len(key)]) - ord('А')
            new_code = (char_code - key_code) % 32  # 32 буквы в русском алфавите
            new_char = chr(new_code + ord('А'))
            if not case:
                new_char = new_char.lower()
            result += new_char
        else:
            result += char

    # Выводим результат
    result_entry.delete(0, END)
    result_entry.insert(0, result)


# Создаем графический интерфейс
root = Tk()
root.title('Шифр Виженера')
root.geometry('600x500')
root["bg"]="#008000"

# Создаем элементы для ввода текста и ключа
text_label = Label(root, text='Введите текст:', font='Arial 14 italic', bg='#008000', fg='white')
text_label.pack(pady=10)
text_label.config(font='Arial 14', fg='black', bg='#008000', width=40, height=1, anchor=W, wraplength=500, justify=LEFT, padx=10, pady=10)

text_entry = Entry(root, font='Arial 14', width=40)
text_entry.pack(pady=10)

shift_label = Label(root, text='Введите ключ шифрования:', font='Arial 14 italic', bg='#008000', fg='white')
shift_label.pack(pady=10)
shift_label.config(font='Arial 14', fg='black', bg='#008000', width=40, height=1, anchor=W, wraplength=500, justify=LEFT, padx=10, pady=10)

shift_entry = Entry(root, font='Arial 14', width=40)
shift_entry.pack(pady=10)

# Создаем кнопки для шифрования и расшифрования текста
encrypt_button = Button(root, text='Зашифровать текст', bg='#DAA520', font='Arial 14', command=vigenere_encrypt_text)
encrypt_button.pack(pady=10)

decrypt_button = Button(root, text='Расшифровать текст', bg='#DAA520',  font='Arial 14', command=vigenere_decrypt_text)
decrypt_button.pack(pady=10)

# Создаем виджет для вывода результата
result_label = Label(root, text='Результат:', font='Arial 14 italic', bg='#008000', fg='white')
result_label.pack(pady=10)
result_label.config(font='Arial 14', fg='black', bg='#008000', width=40, height=1, anchor=W, wraplength=500, justify=LEFT, padx=10, pady=10)

result_entry = Entry(root, font='Arial 14', width=40)
result_entry.pack(pady=10)
#Добавление меню "Справка" и вложенного меню "О программе" в основное меню
def show_info():
    mb.showinfo("О программе", "Феткулин Григорий - Шифр виженера, 2023")
main_menu = Menu()
file_menu = Menu()
about_menu = Menu()
about_menu.add_command(label="О программе", command=show_info)
main_menu.add_cascade(label="Справка", menu=about_menu)
root.config(menu=main_menu)

# Запускаем цикл обработки событий
root.mainloop()