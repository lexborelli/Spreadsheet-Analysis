# Required Tasks
# These are the required tasks for this project. You should aim to complete these tasks before
# adding your own ideas to the project.
# 1. Read the data from the spreadsheet
# 2. Collect all of the sales from each month into a single list
# 3. Output the total sales across all months

import pandas as pd
df = pd.read_csv(r"C:\Users\alexa\PycharmProjects\cfg-python\sales.csv")
print(df)
df.columns
df.to_csv("new_csv", columns=['sales'])
total = sum(df.sales)
print("The total of all the sales is $ {:,.2f}.".format(total))

df.to_csv("salesOverview_csv", columns=['month', 'sales'])

# Who will do what:

# Alexas: DONE!
# - Create new spreadsheet, save it
# - highest and lowest sales
# - * average sales
df.to_csv("salesOverview_csv", columns=['month', 'sales'])


def lowest_sale():
    min_sale = df['sales'].idxmin()
    return min_sale
print("The month with the lowest sales was {}.".format(df['month'][1]))


def highest_sale():
    max_sale = df['sales'].idxmax()
    return max_sale
print("The month with the highest sales was {}.".format(df['month'][6]))

# - average sales
average_of_sales = df['sales'].mean()
print("The average in sales for 2018 was ${:,.2f}.".format(average_of_sales))

# Gabi > DONE
# - create a function that takes in a csv and outputs the total sales
# - * error handling - that's a csv, fool
# - create a function - monthly sales as a percentage

import pandas as pd


def monthly_sales_pct(csv_file, column_name, sort_column):
    try:
        # Read the CSV file
        df = pd.read_csv(r"C:\Users\alexa\PycharmProjects\cfg-python\sales.csv")

        # Error Handling: Ensure the specified columns exist
        if column_name not in df.columns:
            print(f"No '{column_name}' column found in the CSV.")
            return

        if sort_column not in df.columns:
            print(f"No '{sort_column}' column found in the CSV.")
            return

        # Sort the DataFrame by the specified column
        df = df.sort_values(by=sort_column)

        # Calculate the percentage change for the specified column
        df['Percent Change'] = df[column_name].pct_change() * 100

        # Calculate the mean percentage change
        mean_sales_percent_change = df['Percent Change'].mean()

        print(df)
        print(f"Mean change in {column_name}, after sorting by {sort_column}: {mean_sales_percent_change:.2f}%")

    # Error Handling:
    except FileNotFoundError:
        print("File not found. Please make sure the file path is correct.")
    except pd.errors.EmptyDataError:
        print("The file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the file. Please make sure the file is a valid CSV.")


# Example usage
monthly_sales_pct("sales.csv", "sales", "year")