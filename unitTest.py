import json
import requests
import unittest
from urllib.request import urlopen
#from bs4 import BeautifulSoup

class FlaskTestCase(unittest.TestCase):
    URL1 = "http://127.0.0.1:5000/getall"
    URL2 = "http://127.0.0.1:5000/postdata"
    URL3 = "http://127.0.0.1:5000/deletedata"
    URL4 = "http://127.0.0.1:5000/updatedata"
    #data for the post method
    dataTest = {
        "level_0" : 755,
        "index" : 705,
        "Player" : "Ernest Renan",
        "Position" : "C",
        "Age" : 24,
        "Teams" : "CHI"
    }
    #data for the update method   
    updated_data = {
        "level_0" : 3,
        "index" : 3,
        "Player" : "Steven Azar",
        "Position" : "C",
        "Age" : 23,
        "Teams" : "MIA"
    }
    #vérifier si le statut de la réponse est 200
    #retouner toutes les datas

    def test_getall_data(self):
        response = requests.get(self.URL1)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(len(response.json()), 1)
        print("test 1 completed")
    
    def test2_post_data(self):
        response = requests.post(self.URL2, json=self.dataTest)
        self.assertEqual(response.status_code, 200)
        print("test 2 completed")

    #test qui permet de vérifier si l'on peut trouver un data spécifique
    def test_get_specific_data(self):
        response = requests.get(self.URL1 + '/Jaylen Adams')
        self.assertEqual(response.status_code, 200)
        print("test 3 is completed") 
    #test qui permet de vérifier si l'api peut delete une data

    def test_delete_data(self):
        response = requests.delete(self.URL3 + '/Mac Mclungs')
        self.assertEqual(response.status_code, 200)
        print("test 4 completed") 

    #test qui permet de vérifier si l'on peut modifier une donnée
    def test_update_data(self):
        response = requests.put(self.URL4 + '/Bam Adebayo', json=self.updated_data)
        print(response.json())

        self.assertEqual(response.json()['Player'], self.updated_data['Player'])
        print("test 5 completed")
#condition pour dire que le server est lancé
if __name__ == "__main__":
    unittest.main()