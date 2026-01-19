customers = ['Sagar', 'Sansar', 'Bharat', 'Samar', 'Sristi']

customer_order_details = [
    ('Sagar', 'DartBoard', 130, 'Sports'),
    ('Sagar', 'Tennis Racket', 250, 'Sports'),
    ('Sansar', 'Laptop', 550, 'Electronics'),
    ('Sansar', 'USB Cable', 50, 'Electronics'),
    ('Bharat', 'Cricket Bat', 250, 'Sports'),
    ('Bharat', 'Football', 80, 'Sports'),
    ('Samar', 'Coffee Maker', 320, 'Kitchen'),
    ('Samar', 'Knife Set', 120, 'Kitchen'),
    ('Sristi', 'Headphones', 450, 'Electronics'),
    ('Sristi', 'Phone Charger', 150, 'Electronics')
]


customer_orders = {
    'Sagar': ['DartBoard', 'Tennis Racket'],
    'Sansar': ['Laptop', 'USB Cable'],
    'Bharat': ['Cricket Bat', 'Football'],
    'Samar': ['Coffee Maker', 'Knife Set'],
    'Sristi': ['Headphones', 'Phone Charger']
}


product_by_category = {
    'Sports': ['DartBoard', 'Tennis Racket', 'Cricket Bat', 'Football'],
    'Electronics': ['Laptop', 'USB Cable', 'Headphones', 'Phone Charger'],
    'Kitchen': ['Coffee Maker', 'Knife Set']
}

unique_product_category = set(['Sports', 'Electronics', 'Kitchen'])

print(list(product_by_category.keys()))

cutomer_spending = {}
for order in customer_order_details:
    if order[0] not in cutomer_spending:
        cutomer_spending[order[0]] = [0, 'low-value buyer']
    cutomer_spending[order[0]][0] += order[2]
    if 50 <= cutomer_spending[order[0]][0] <= 100:
        cutomer_spending[order[0]][1] = 'moderate buyer'
    if cutomer_spending[order[0]][0] > 100:
        cutomer_spending[order[0]][1] = 'high-value buyer'

print(cutomer_spending)