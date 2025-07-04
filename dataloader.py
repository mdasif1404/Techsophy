import pandas as pd

def load_customers():
    return pd.read_csv('data/customers.csv')

def load_products():
    return pd.read_csv('data/insurance_products.csv')

 