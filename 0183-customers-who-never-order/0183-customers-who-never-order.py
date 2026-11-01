import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    no_orders_df = merged_df.query("customerId.isnull()")
    no_orders_df = no_orders_df.rename(columns={'name': 'Customers'})
    return no_orders_df[['Customers']]
