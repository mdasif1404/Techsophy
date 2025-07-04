from flask import Flask, request, jsonify
import pandas as pd
from src import data_loader, customer_profiling, needs_analysis, product_matching, recommendation_engine, utils

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    profile = customer_profiling.profile_customer(pd.Series(data))
    needs = needs_analysis.assess_needs(profile)
    products = data_loader.load_products()
    matched = product_matching.match_products(products, needs)
    recommendations = recommendation_engine.recommend_products(profile, matched)
    explanations = [utils.explain_recommendation(name, profile) for name, _ in recommendations]
    return jsonify({"recommendations": recommendations, "explanations": explanations})

if __name__ == '__main__':
    app.run(debug=True)
