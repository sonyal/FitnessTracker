from frontend.tutorialsearch import TestLinkProxy
import unittest
import os


class SearchTests(unittest.TestCase):
    def test_incorret_inputs(self):
        test_link = TestLinkProxy()
        test1 = test_link.test_link("fsdlsdjfklsd")
        self.assertEqual(test1, -1)
        test2 = test_link.test_link(("",""))
        self.assertEqual(test2, -1)
        test3 = test_link.test_link(5)
        self.assertEqual(test3, -1)
        test4 = test_link.test_link(["happy"])
        self.assertEqual(test4, -1)

    def test_flexibility(self):
        test_link = TestLinkProxy()
        test1 = test_link.test_link("flexibility")
        self.assertEqual(test1, 1)
        test1 = test_link.test_link("Flexibility")
        self.assertEqual(test1, 1)

    def test_cardio(self):
        test_link = TestLinkProxy()
        test1 = test_link.test_link("cardiovascular")
        self.assertEqual(test1, 0)
        test1 = test_link.test_link("Cardiovascular")
        self.assertEqual(test1, 0)

    def test_strength(self):
        test_link = TestLinkProxy()
        test1 = test_link.test_link("Strength")
        self.assertEqual(test1, 2)
        test1 = test_link.test_link("strength")
        self.assertEqual(test1, 2)
