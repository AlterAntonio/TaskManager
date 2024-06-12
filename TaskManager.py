import random
import tkinter as tk

colors = ["AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond",
    "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue",
    "Cornsilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGreen", "DarkKhaki", "DarkMagenta",
    "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue",
    "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DodgerBlue", "FireBrick", "FloralWhite", "ForestGreen",
    "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "Green", "GreenYellow", "HoneyDew", "HotPink",
    "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue",
    "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen",
    "LightSkyBlue", "LightSlateBlue", "LightSteelBlue", "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta",
    "Maroon", "MediumAquaMarine", "MediumBlue", "MediumOrchid", "MediumPurple", "MediumSeaGreen",
    "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream",
    "MistyRose", "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid",
    "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum",
    "PowderBlue", "Purple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown", "SeaGreen",
    "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal",
    "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen"]

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def del_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, bg="green")

root = tk.Tk()
root.title("Task List")
root.configure(bg="DeepSkyBlue")

text1 = tk.Label(root, text="Введите задачу:", bg="DeepSkyBlue")
text1.pack()
task_entry = tk.Entry(root, width=30, bg="gainsboro")
task_entry.pack()

task_button = tk.Button(root, text="Добавить", command=add_task)
task_button.pack(pady=5)
del_button = tk.Button(root, text="Удалить", command=del_task)
del_button.pack(pady=5)
mark_button = tk.Button(root, text="Сделано!", command=mark_task)
mark_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:", bg="DeepSkyBlue")
text2.pack()
task_listbox = tk.Listbox(root, height=10, width=50, bg="gold")
task_listbox.pack(pady=5, padx=5)

def colored():
    root.configure(bg=random.choice(colors))
    text1.configure(bg=random.choice(colors))
    task_entry.configure(bg=random.choice(colors))
    task_button.configure(bg=random.choice(colors))
    del_button.configure(bg=random.choice(colors))
    mark_button.configure(bg=random.choice(colors))
    text2.configure(bg=random.choice(colors))
    task_listbox.configure(bg=random.choice(colors))
    color_button.configure(bg=random.choice(colors))
color_button = tk.Button(root, text='Рандомайзер цветов элементов', command=colored)
color_button.pack()

root.mainloop()