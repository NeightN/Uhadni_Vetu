import unittest
from hadanka import Hadanka

class Test(unittest.TestCase):

    def test_get_veta(self):
        """
        Metoda pro testování metody get_veta
        :return: void
        """
        hadanka = Hadanka("ahojo jako se mášo")
        self.assertEqual(hadanka.get_veta(), "ahojo jako se mášo")
        self.assertRaises(Exception, Hadanka)
        self.assertRegex(hadanka.get_veta(), "^[a-ž ]+$")

    def test_get_slovo(self):
        """
        Metoda pro testování metody get_slovo
        :return: void
        """
        hadanka = Hadanka("ahoj jak se máš")
        hadanka.get_slova()
        self.assertEqual(hadanka.get_slova(), ['ahoj', 'jak', 'se', 'máš'])

    def test_pocet_slov(self):
        """
        Metoda pro testování metody pocet_slov
        :return: void
        """
        hadanka = Hadanka("ahoj jak se máš")
        self.assertEqual(hadanka.pocet_slov(), 4)

    def test_hadej_slovo(self):
        """
        Metoda pro testování metody hadej_slovo
        :return: void
        """
        hadanka = Hadanka("ahoj jak se máš")
        self.assertEqual(hadanka.hadej_slovo("ahoj"), [0])

    def test_hadej_vetu(self):
        """
        Metoda pro testování metody hadej_vetu
        :return: void
        """
        hadanka = Hadanka("ahoj jak se máš")
        self.assertEqual(hadanka.hadej_vetu("ahoj jak se máš"), True)

if __name__ == "__main__":
    unittest.main()