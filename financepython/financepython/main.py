import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount,get_category,get_date ,get_description
import matplotlib.pyplot as plt



class CSV:
    CSV_FILE = 'finance_data.csv'
    FORMAT = "%d-%m-%Y"
    COLUMS = ['date', 'amount', 'category', 'description']
    @classmethod
    def initialialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_transaction(cls, date, amount, category, description):
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMS)
            writer.writerow(new_entry)
            print(f"Transaction added: {new_entry}")
            print(f"Entry added Successfully ")

    @classmethod
    def get_transactions(cls,start_date,end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format = CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        mask= (df['date']>= start_date) & (df['date']<=end_date)
        filter_df= df.loc[mask]

        if filter_df.empty:
            print('No Transactions found')
        else:
            print(f"Transaction found from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(
                filter_df.to_string(index=False,formatters={"date":lambda x: x.strftime(CSV.FORMAT)}
                )
            )
            total_income =filter_df[filter_df["category"] == 'Income']['amount'].sum()
            total_expense =filter_df[filter_df["category"] == 'Expense']['amount'].sum()
            print("\nSummary")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings ${(total_income-total_expense):.2f}")

        return filter_df



def add():
    CSV.initialialize_csv()
    date = get_date("Enter Date of transaction (dd-mm-yyyy) or Enter for todays date:",allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_transaction(date,amount,category,description)


def plot_transaction(df):
    df.set_index('date',inplace =True)
    income_df= df[df['category']=='Income'].resample("D").sum().reindex(df.index,fill_value=0)
    expense_df= df[df['category']=='Expense'].resample("D").sum().reindex(df.index,fill_value=0)

    plt.figure(figsize=(10,5))
    plt.plot(income_df.index,income_df['amount'], label='Income',color='green')
    plt.plot(expense_df.index,expense_df['amount'], label='Expense',color='red')
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses over time")
    plt.legend()
    plt.grid(True)
    plt.show()



def main():
    while True:
        print("\n 1. Add new transaction")
        print("2. View all transactions with summary and data ranges")
        print("3. Exit")
        choice = input("Enter your Choice (1-3):")
        if choice == "1":
            add()
        elif choice == "2":
            start_date=get_date("Enter start Date (dd-mm-yyyy): ")
            end_date =get_date("Enter End Date (dd-mm-yyyy): ")
            df=CSV.get_transactions(start_date,end_date)
            if input("Do you wanna see the plot?(y/n)").lower()=='y':
                plot_transaction(df)
        elif choice == '3':
            print("Exiting----")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3")


if __name__ == "__main__":
    main()