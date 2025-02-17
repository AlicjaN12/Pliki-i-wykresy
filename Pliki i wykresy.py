import pandas as pd
import matplotlib.pyplot as plt
import json
import tkinter as tk
from tkinter import filedialog

# Funkcja do wyboru pliku CSV i rysowania wykresu
def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        plot_data(df)

# Funkcja do wczytania pliku JSON z opisem osi, tytułem i jednostkami
def load_json():
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "r") as file:
            return json.load(file)
    return {}

# Funkcja do wyboru rodzaju wykresu
def plot_data(df):
    plt.figure(figsize=(8, 6))
    
    # Wczytanie ustawień z JSON
    settings = load_json()
    title = settings.get("title", "Wykres danych")
    xlabel = settings.get("xlabel", "X")
    ylabel = settings.get("ylabel", "Y")
    
    chart_type = chart_var.get()
    x_column, y_column = df.columns[:2]  # Zakładamy, że dane są w dwóch pierwszych kolumnach
    
    if chart_type == "Liniowy":
        plt.plot(df[x_column], df[y_column], marker='o', linestyle='-')
    elif chart_type == "Słupkowy":
        plt.bar(df[x_column], df[y_column])
    elif chart_type == "Punktowy":
        plt.scatter(df[x_column], df[y_column])
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# GUI z wykorzystaniem Tkinter
root = tk.Tk()
root.title("Wykresy z pliku CSV")

chart_var = tk.StringVar(value="Liniowy")

tk.Label(root, text="Wybierz plik CSV i typ wykresu:").pack()

tk.Button(root, text="Wczytaj CSV", command=load_csv).pack()

# Opcje wyboru typu wykresu
tk.Radiobutton(root, text="Liniowy", variable=chart_var, value="Liniowy").pack()
tk.Radiobutton(root, text="Słupkowy", variable=chart_var, value="Słupkowy").pack()
tk.Radiobutton(root, text="Punktowy", variable=chart_var, value="Punktowy").pack()

root.mainloop()