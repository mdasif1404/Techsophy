def score_product(product, profile):
    affordability = max(0, 1 - product['monthly_premium'] / profile['income'])
    return 0.7 * affordability + 0.3  # risk alignment is placeholder


def recommend_products(profile, products):
    scored = []
    for _, product in products.iterrows():
        score = score_product(product, profile)
        scored.append((product['name'], score))
    return sorted(scored, key=lambda x: x[1], reverse=True)

