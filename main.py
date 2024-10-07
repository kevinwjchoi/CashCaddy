import pandas as pd
import csv
from datetime import datetime

class CSV: 
    CSV_FILE = "finance_data.csv" #class variable
    COLUMNS = ["date", "amount", "category", "description"]
    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile: #this is a context manager
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

CSV.initialize_csv() 
CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")