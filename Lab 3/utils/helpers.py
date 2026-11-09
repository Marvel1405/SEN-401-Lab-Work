"""
Stock helper analytics functions with bounds checking.
"""

def highest_stock_item(items):
    if not items:
        return None
    return max(items, key=lambda x: x['quantity'] * x['price'])

def lowest_stock_item(items):
    if not items:
        return None
    return min(items, key=lambda x: x['quantity'] * x['price'])