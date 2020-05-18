import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_and_explode(self):
        """Test stealability() and explode() methods."""
        prod = Product(name='test_product', price=5, weight=10, flammability=2.0)
        self.assertEqual(prod.stealability(), print('Kinda stealable.'))
        self.assertEqual(prod.explode(), print('...boom!'))


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
    def test_default_num_products(self):
        """Test that a list of length 30 is received and processed"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test that a generated product consists of legal naming components"""
        self.assertIn([product.name for product in generate_products()][0].split()[0], ADJECTIVES)
        self.assertIn([product.name for product in generate_products()][0].split()[1], NOUNS)
        self.assertEqual(' ' in [product.name for product in generate_products()][0], True)


if __name__ == '__main__':
    unittest.main()
