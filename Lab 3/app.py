"""
Inventory status accounting script calculating total stock valuation.
"""

from inventory import INVENTORY_ITEMS
from utils.helpers import highest_stock_item, lowest_stock_item

def main():
    print("=== Warehouse Status Accounting & Auditing Dashboard ===")
    total_valuation = 0.0
    
    for item in INVENTORY_ITEMS:
        subtotal = item['quantity'] * item['price']
        total_valuation += subtotal
        print(f"- {item['item_name']}: Qty {item['quantity']} @ ${item['price']:.2f} = ${subtotal:.2f}")

    print("-----------------------------------------------------")
    print(f"[*] Total Inventory Asset Value: ${total_valuation:.2f}")
    
    top = highest_stock_item(INVENTORY_ITEMS)
    low = lowest_stock_item(INVENTORY_ITEMS)
    
    if top:
        print(f"[*] Highest Value Asset : {top['item_name']}")
    if low:
        print(f"[*] Lowest Value Asset  : {low['item_name']}")
    print("=====================================================")

if __name__ == "__main__":
    main()