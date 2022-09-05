import unittest
import scraper


class TestScraper(unittest.TestCase):
    test_products = [
        ["Drops", "Soft-Tweed-Mix"],
        ["Rico", "Creative Cotton Flecky Fleece DK"],
        ["Pink Label", "Create-it"]
    ]
    test_urls = [
        "https://www.wollplatz.de/wolle/drops/drops-soft-tweed-mix",
        "https://www.wollplatz.de/wolle/rico/rico-creative-cotton-flecky-fleece-dk",
        "https://www.wollplatz.de/wolle/pink-label/pink-label-create-it"
    ]

    def test_init_product_names(self):
        self.assertEqual(
            len(scraper.init_product_names('./product_list.csv')), 5)
        with self.assertRaises(FileNotFoundError):
            scraper.init_product_names("dieseFileGibtEsNicht.csv")

    def test_create_url(self):
        for product, url in zip(self.test_products, self.test_urls):
            self.assertEqual(scraper.create_url(*product), url)

    def test_find_products(self):
        result = scraper.find_products(self.test_products)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].price, 2.60)
        self.assertEqual(result[0].ingredients,
                         "50% Wolle, 25% Alpakawolle, 25% Viscose")
        self.assertEqual(result[0].strength, "4 mm")
        self.assertEqual(result[1].price, 8.85)
        self.assertEqual(result[1].ingredients,
                         "75% Katoen, 13% Acryl & 12% Wol")
        self.assertEqual(result[1].strength, "3.5 - 4 mm")
        self.assertEqual(result[2].price, 9.00)
        self.assertEqual(result[2].ingredients, "100% Polyester")
        self.assertEqual(result[2].strength, "7 - 8 mm")


if __name__ == '__main__':
    unittest.main()
