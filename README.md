# Cash Caddy

Cash Caddy is a command-line financial tracker built in Python that helps users manage their finances by recording transactions, categorizing expenses, and visualizing income and expenses over time.

## Features

- **Add Transactions**: Record financial transactions with details like date, amount, category, and description.
- **View Transaction Summaries**: Retrieve and display transaction summaries within specified date ranges.
- **Visualize Finances**: Generate and display graphs to visualize income and expenses over time.

## Requirements

- Python 3.x
- Required Python libraries: `pandas`, `matplotlib`

## Installation

### Clone the Repository:
```bash
git clone https://github.com/kevinwjchoi/cash-caddy.git
cd cash-caddy
```

### Install Dependencies:
```bash
pip install pandas matplotlib
``` 

## Usage

### Run the Application:
```bash
python3 main.py
```

### Add a Transaction
Follow the prompts to input the date, amount, category (Income or Expense), and an optional description.

### View Transactions
Enter a date range to see all transactions within that period, along with a summary of total income, total expenses, and net savings.

### Generate Graphs
Optionally, visualize your income and expenses as a graph after viewing transactions.

## Commands
- `1`: Add a new transaction
- `2`: View transactions and summary within a date range
- `3`: Exit the application

## Data Storage
Transactions are stored in a CSV file named `finance_data.csv`. The application will create this file automatically if it doesn't exist.

## Contributing
Contributions are welcome! If you have suggestions for improvements or find bugs, please submit a pull request or open an issue.


