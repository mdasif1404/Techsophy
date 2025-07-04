def match_products(products, needed_types):
    return products[products['type'].isin(needed_types)]
