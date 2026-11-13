import tkinter as tk
from tkinter import messagebox


def login():
    # База данных организаторов (Крипта, Арбитраж, Концерты)
    users_db = {
        "crypto_manager": "web3_2026",
        "cpa_owner": "mafia777",
        "concert_admin": "3umph_tour"
    }

    username = entry_user.get()
    password = entry_pass.get()

    if username in users_db and users_db[username] == password:
        messagebox.showinfo("EventService PRO", f"Доступ разрешен! Приветствуем, {username}.")
    else:
        messagebox.showerror("Ошибка доступа", "Неверный логин или ключ шифрования!")


# Окно авторизации
root = tk.Tk()
root.title("EventService Premium - Вход в панель управления")
root.geometry("350x220")

tk.Label(root, text="Логин организатора (Crypto/CPA/Concerts):", font=("Arial", 10)).pack(pady=8)
entry_user = tk.Entry(root, font=("Arial", 10))
entry_user.pack(pady=2)

tk.Label(root, text="Пароль / Ключ доступа:", font=("Arial", 10)).pack(pady=8)
entry_pass = tk.Entry(root, show="*", font=("Arial", 10))
entry_pass.pack(pady=2)

tk.Button(root, text="Пройти авторизацию", command=login, bg="#20B2AA", fg="white", font=("Arial", 10, "bold")).pack(
    pady=20)

root.mainloop()
