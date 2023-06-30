import unittest

def select_item(items, item_name):
    if item_name not in items:
        raise ValueError("Invalid item selected.")
    return items[item_name]

def purchase_item(customer_balance, item_price):
    if item_price <= customer_balance:
        customer_balance -= item_price
        return customer_balance
    else:
        raise ValueError("Insufficient funds for the selected item.")

class ShopTest(unittest.TestCase):
    def setUp(self):
        self.items = {
            'Item 1': 50,
            'Item 2': 75,
            'Item 3': 150
        }
        self.customer_balance = 100

    def test_select_item_valid(self):
        item_name = 'Item 1'
        item_price = select_item(self.items, item_name)
        self.assertEqual(item_price, 50)

    def test_select_item_invalid(self):
        item_name = 'Item 4'
        with self.assertRaises(ValueError):
            select_item(self.items, item_name)

    def test_purchase_item_sufficient_funds(self):
        item_price = 50
        new_balance = purchase_item(self.customer_balance, item_price)
        self.assertEqual(new_balance, 50)

    def test_purchase_item_insufficient_funds(self):
        item_price = 200
        with self.assertRaises(ValueError):
            purchase_item(self.customer_balance, item_price)

    def test_purchase_item_additional_funds(self):
        item_price = 200
        additional_funds = 150
        self.customer_balance += additional_funds
        new_balance = purchase_item(self.customer_balance, item_price)
        self.assertEqual(new_balance, 50)

if __name__ == '__main__':
    unittest.main()
