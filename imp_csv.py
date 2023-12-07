import pandas as pd
df = pd.read_csv(r"C:\Users\alexa\PycharmProjects\cfg-python\sales.csv")
df.columns
df.to_csv("new_csv", columns=['sales'])
total = sum(df.sales)
print("The total of all the sales is $ {:,.2f}.".format(total))

df.to_csv("salesOverview_csv", columns=['month', 'sales'])

def lowest_sale():
 min_sale = df['sales'].idxmin()
 return min_sale
print("The month with the lowest sales was {}".format(df['month'][1]))


def highest_sale():
    max_sale = df['sales'].idxmax()
    return max_sale
print("The month with the highest sales was {}".format(df['month'][6]))

average_of_sales = df['sales'].mean()
print("The average of the sales is {:,.2f}.".format(average_of_sales))