import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_behavioral_traits(file_path):
    data = pd.read_excel(file_path)

    root = tk.Tk()
    root.title("Behavioral Traits Distributions")

    tab_control = ttk.Notebook(root)

    behavioral_columns = ['Shy', 'Calm', 'Fearful', 'Intelligent', 'Vigilant',
                          'Perseverant', 'Affectionate', 'Friendly', 'Solitary', 'Brutal',
                          'Dominant', 'Aggressive', 'Impulsive', 'Predictable', 'Distracted']

    for column in behavioral_columns:
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text=column)

        fig, ax = plt.subplots(figsize=(6, 4))

        sns.countplot(data=data, x=column, palette='viridis', hue=column, ax=ax, legend=False)

        for label in ax.get_xticklabels():
            label.set_rotation(45)

        ax.set_title(f"Distribution of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')

        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    tab_control.pack(expand=1, fill="both")

    def on_close():
        root.quit()
        root.destroy()
        plt.close('all')

    root.protocol("WM_DELETE_WINDOW", on_close)

    root.mainloop()


def plot_other_traits(file_path):
    data = pd.read_excel(file_path)

    root = tk.Tk()
    root.title("Other Traits Distributions")

    tab_control = ttk.Notebook(root)

    other_columns = [col for col in data.columns if col not in ['Shy', 'Calm', 'Fearful', 'Intelligent', 'Vigilant',
                                                                'Perseverant', 'Affectionate', 'Friendly', 'Solitary',
                                                                'Brutal', 'Dominant', 'Aggressive', 'Impulsive',
                                                                'Predictable', 'Distracted']]
    for column in other_columns:
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text=column)

        fig, ax = plt.subplots(figsize=(6, 4))

        if data[column].dtype in ['int64', 'float64']:
            sns.histplot(data[column], kde=True, color='blue', bins=20, ax=ax)
        else:
            sns.countplot(data=data, x=column, palette='viridis', hue=column, ax=ax, legend=False)

        for label in ax.get_xticklabels():
            label.set_rotation(15)

        ax.set_title(f"Distribution of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')

        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    tab_control.pack(expand=1, fill="both")

    def on_close():
        root.quit()
        root.destroy()
        plt.close('all')

    root.protocol("WM_DELETE_WINDOW", on_close)

    root.mainloop()
