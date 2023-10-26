import tkinter as tk
from PIL import Image, ImageTk

from UI import settings
from UI.run import create_order, show_text_entry_window, check_is_empty, show_error
from tkinter import PhotoImage

root = tk.Tk()
root.title(settings.TITTLE)
root.geometry(settings.GEOMETRY)

check_var_sauce = tk.BooleanVar()
check_var_size = tk.StringVar()
check_var_cola = tk.BooleanVar()
check_var_pay = tk.StringVar()

image = PhotoImage(file='templates/settings.png')


def settings_info():
    show_text_entry_window(tk=tk, root=root, geometry=settings.GEOMETRY_TOP_LEVEL)


settings_button = tk.Button(root, image=image, height=40, width=40, highlightthickness=0, command=settings_info)
settings_button.pack(anchor='e')

sauce_button = tk.Checkbutton(root, text="Соус сырный", variable=check_var_sauce)
sauce_button.pack(side="top", pady=10)

cola_button = tk.Checkbutton(root, text="Кола", variable=check_var_cola)
cola_button.pack(side="top", pady=10)

frame_grid_size = tk.Frame(root)
frame_grid_size.pack(pady=10)

size_button_1 = tk.Radiobutton(frame_grid_size, text='Большая', variable=check_var_size, value='1')
size_button_1.grid(row=1, column=0)

size_button_2 = tk.Radiobutton(frame_grid_size, text='Маленькая', variable=check_var_size, value='2')
size_button_2.grid(row=1, column=1, padx=1)

frame_grid_paymethod = tk.Frame(root)
frame_grid_paymethod.pack(pady=10)

pay_method_button_1 = tk.Radiobutton(frame_grid_paymethod, text='Картой', variable=check_var_pay, value='1')
pay_method_button_1.grid(row=1, column=0)

pay_method_button_2 = tk.Radiobutton(frame_grid_paymethod, text='Наличные', variable=check_var_pay, value='2')
pay_method_button_2.grid(row=1, column=1, padx=1)


def order():
    if not check_is_empty(settings.LABELS):
        show_error(tk=tk, root=root, geometry=settings.GEOMETRY_TOP_LEVEL)
    else:
        create_order(settings=settings,
                     check_var_cola=check_var_cola.get(),
                     check_var_sauce=check_var_sauce.get(),
                     check_var_paymethod=check_var_pay.get(),
                     check_var_size=check_var_size.get())


button_pizza = tk.Button(root, text="Заказать пиццу", height=2, command=order)
button_pizza.place(x=250, y=250, anchor='center')

root.mainloop()
