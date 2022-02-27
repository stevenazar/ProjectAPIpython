import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Test(unittest.TestCase):
    bs = None
    def setUpClass():
        url = 'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html'
        Test.bs = BeautifulSoup(urlopen(url), 'html.parser')
        print("la page à bien été trouvé")

    def test_exists(self):
        contenu = Test.bs.find('tr', {'class':'full_table'})
        self.assertIsNotNone(contenu)

    def test_Title(self):
        title = Test.bs.find('span', {'class':'header_end'}).get_text()
        self.assertEqual('Player Stats: Per Game', title)
    
if __name__ == "main":
    unittest.main()
