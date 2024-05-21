# measurement_converter_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from measurement_converter import MeasurementConverter

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Measurement Converter")

        # Styling
        style = ttk.Style()
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TLabel', background='#e0f7fa', font=('Arial', 10))
        style.configure('TButton', background='#4caf50', foreground='white', font=('Arial', 10, 'bold'))
        style.map('TButton', background=[('active', '#388e3c')])

        # App Title
        self.title_label = ttk.Label(root, text="ConversionEase", font=('Helvetica', 20, 'bold'), background='#4caf50', foreground='white')
        self.title_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # Main Frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.converter = MeasurementConverter()

        self.category_label = ttk.Label(self.main_frame, text="Category")
        self.category_label.grid(column=0, row=0, padx=10, pady=10)

        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(self.main_frame, textvariable=self.category_var)
        self.category_combobox['values'] = list(self.converter.units.keys())
        self.category_combobox.grid(column=1, row=0, padx=10, pady=10)
        self.category_combobox.bind("<<ComboboxSelected>>", self.update_units)

        self.value_label = ttk.Label(self.main_frame, text="Value")
        self.value_label.grid(column=0, row=1, padx=10, pady=10)

        self.value_entry = ttk.Entry(self.main_frame)
        self.value_entry.grid(column=1, row=1, padx=10, pady=10)

        self.from_unit_label = ttk.Label(self.main_frame, text="From Unit")
        self.from_unit_label.grid(column=0, row=2, padx=10, pady=10)

        self.from_unit_var = tk.StringVar()
        self.from_unit_combobox = ttk.Combobox(self.main_frame, textvariable=self.from_unit_var)
        self.from_unit_combobox.grid(column=1, row=2, padx=10, pady=10)

        self.to_unit_label = ttk.Label(self.main_frame, text="To Unit")
        self.to_unit_label.grid(column=0, row=3, padx=10, pady=10)

        self.to_unit_var = tk.StringVar()
        self.to_unit_combobox = ttk.Combobox(self.main_frame, textvariable=self.to_unit_var)
        self.to_unit_combobox.grid(column=1, row=3, padx=10, pady=10)

        self.convert_button = ttk.Button(self.main_frame, text="Convert", command=self.convert)
        self.convert_button.grid(column=0, row=4, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.main_frame, text="Result:")
        self.result_label.grid(column=0, row=5, padx=10, pady=10)

        self.result_var = tk.StringVar()
        self.result_entry = ttk.Entry(self.main_frame, textvariable=self.result_var, state='readonly')
        self.result_entry.grid(column=1, row=5, padx=10, pady=10)

    def update_units(self, event):
        category = self.category_var.get()
        units = list(self.converter.units.get(category, {}).keys())
        self.from_unit_combobox['values'] = units
        self.to_unit_combobox['values'] = units

    def convert(self):
        try:
            category = self.category_var.get()
            value = float(self.value_entry.get())
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()
            result = self.converter.convert(category, value, from_unit, to_unit)
            self.result_var.set(result)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
