import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # API setup
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.currencies = self.fetch_currencies()

        # Create and place widgets
        self.create_widgets()

    def fetch_currencies(self):
        try:
            response = requests.get(self.api_url)
            data = response.json()
            return list(data['rates'].keys())
        except Exception as e:
            print(f"Error fetching currencies: {e}")
            return []

    def create_widgets(self):
        # Source currency
        tk.Label(self.root, text="From Currency").grid(row=0, column=0, padx=10, pady=10)
        self.from_currency = ttk.Combobox(self.root, values=self.currencies)
        self.from_currency.grid(row=0, column=1, padx=10, pady=10)

        # Target currency
        tk.Label(self.root, text="To Currency").grid(row=1, column=0, padx=10, pady=10)
        self.to_currency = ttk.Combobox(self.root, values=self.currencies)
        self.to_currency.grid(row=1, column=1, padx=10, pady=10)

        # Amount
        tk.Label(self.root, text="Amount").grid(row=2, column=0, padx=10, pady=10)
        self.amount = tk.Entry(self.root)
        self.amount.grid(row=2, column=1, padx=10, pady=10)

        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        try:
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()
            amount = float(self.amount.get())
            if from_currency == to_currency:
                result = amount
            else:
                conversion_rate = self.get_conversion_rate(from_currency, to_currency)
                result = amount * conversion_rate
            self.result_label.config(text=f"Result: {result:.2f} {to_currency}")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def get_conversion_rate(self, from_currency, to_currency):
        try:
            response = requests.get(self.api_url)
            data = response.json()
            rates = data['rates']
            if from_currency == 'USD':
                return rates[to_currency]
            elif to_currency == 'USD':  
                return 1 / rates[from_currency]
            else:
                return rates[to_currency] / rates[from_currency]
        except Exception as e:
            print(f"Error fetching conversion rate: {e}")
            return 1

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
