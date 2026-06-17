from optimization.index_recommender import IndexRecommender

sql = """
SELECT
    c.customer_id,
    c.customer_name
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
"""

engine = IndexRecommender()

for item in engine.recommend(sql):
    print(item)
