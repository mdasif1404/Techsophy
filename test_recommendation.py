import unittest
from src import data_loader, customer_profiling, needs_analysis, product_matching, recommendation_engine

class TestRecommendation(unittest.TestCase):
    def test_recommendation_flow(self):
        customers = data_loader.load_customers()
        products = data_loader.load_products()
        profile = customer_profiling.profile_customer(customers.iloc[0])
        needs = needs_analysis.assess_needs(profile)
        matches = product_matching.match_products(products, needs)
        recs = recommendation_engine.recommend_products(profile, matches)
        self.assertGreater(len(recs), 0)

if __name__ == '__main__':
    unittest.main()
