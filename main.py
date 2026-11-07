import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Твоя уникальная база данных: Концерты и Крипта/Арбитраж
events_db = [
    {"название": "Концерт 3umph - Live Tour", "тип": "Концерт", "участники": 850, "билет_руб": 1500},
    {"название": "Королевский XVII - Большое шоу", "тип": "Концерт", "участники": 1200, "билет_руб": 2000},
    {"название": "Crypto Summit: Инвестиции и Web3", "тип": "Бизнес-встреча", "участники": 150, "билет_руб": 5000},
    {"название": "CPA Mafia: Арбитраж трафика 2026", "тип": "Бизнес-встреча", "участники": 90, "билет_руб": 4500}
]

def calculate_budget():
    """Вычислительный эксперимент: Расчет финансового оборота мероприятия"""
    try:
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Внимание", "Выберите мероприятие из списка!")
            return
            
        values = tree.item(selected_item)['values']
        event_name = values[0]       # Название мероприятия
        visitors_count = int(values[2])  # Количество участников
        ticket_price = float(values[3]) # Цена входного билета
        
        # Формула вычислительного эксперимента
        total_revenue = visitors_count * ticket_price
        
        lbl_result.config(text=f"Итог расчета: Прогноз выручки для '{event_name}' — {total_revenue:,} руб.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при расчете: {e}")

# Настройка главного окна
root = tk.Tk()
root.title("EventService Premium - Концерты & Crypto/CPA Meetups")
root.geometry("700x420")

# Заголовок
tk.Label(root, text="Панель организатора: Учет масштабных мероприятий", font=("Arial", 12, "bold")).pack(pady=10)

# Таблица
columns = ("title", "type", "visitors", "price")
tree = ttk.Treeview(root, columns=columns, show="headings", height=6)
tree.heading("title", text="Название ивента")
tree.heading("type", text="Направление")
tree.heading("visitors", text="Продано билетов / мест")
tree.heading("price", text="Цена участия (руб.)")

# Размеры колонок
tree.column("title", width=260)
tree.column("type", width=110)
tree.column("visitors", width=150)
tree.column("price", width=140)

# Загрузка твоих кастомных данных в таблицу
for event in events_db:
    tree.insert("", tk.END, values=(event["название"], event["тип"], event["участники"], event["билет_руб"]))
tree.pack(pady=10, fill=tk.X, padx=15)

# Кнопка для старта эксперимента
btn_calc = tk.Button(root, text="Запустить расчет финансового оборота", command=calculate_budget, bg="#20B2AA", fg="white", font=("Arial", 10, "bold"))
btn_calc.pack(pady=15)

# Вывод результатов
lbl_result = tk.Label(root, text="Результат: Выберите мероприятие в таблице и нажмите кнопку", font=("Arial", 10, "italic"), fg="#333333")
lbl_result.pack(pady=5)

root.mainloop()
