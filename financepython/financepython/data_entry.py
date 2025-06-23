from datetime import datetime


date_format = '%d-%m-%Y'
CATEGORIES={'I':'Income' ,'E': 'Expense'}


def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str.strip():
        return datetime.now().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date date_format. Please use 'dd-mm-yyyy'.")
        return get_date(prompt, allow_default)



def get_amount():
    try:
        amount = float(input("Enter the amount"))
        if amount <= 0:
            raise ValueError("Amount cannot be negative.")
        return amount
    except ValueError as e:
        print(f"Invalid amount: {e}. Please enter a valid positive number.")
        return get_amount()



def get_category():
    category = input("Enter the Category('I' for Income and 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid Category. Use 'I' for Income and 'E' for Expense")
    return get_category()



def get_description():
    return input("Enter a description")

