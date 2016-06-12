import unittest
import requests

import os
import sys
import json

path_to_settings =  os.path.dirname(
                    os.path.dirname(os.path.dirname(
                        os.path.dirname(os.path.abspath(__file__)))))

sys.path.append(path_to_settings)

from settings import HOST, PORT

base_url = 'http://%s:%s'%(HOST,PORT)

category_url = base_url + '/' + 'resources' + '/' + 'categories'

class CategoryTest(unittest.TestCase):
    def setUp(self,):
        # Test to see if connected to site. If not an error is thrown right
        # away
        r = requests.get(base_url)
        self.assertEqual(r.status_code,200)

    def step_get_categories(self,):
        r = requests.get(category_url)
        print(r.text)

    def step_get_category(self,categoryid):
        category_url_num = category_url + "/" + str(categoryid)
        r = requests.get(category_url_num)
        self.assertEqual(200,r.status_code)

    def step_create_category(self,):
        data = {"data":{"attributes":{"name":"Books"},
                       "headers":'text/json',
                       "type":"category"}}

        r = requests.post(category_url,json=data)
        print(r.text)
        self.assertEqual(r.status_code,201)
        return r.text

    def step_modify_category(self,categoryid):
        category_url_num = category_url + "/" + str(categoryid)
        data = {"data":{"attributes":{"name":"Websites"},
                       "headers":'text/json',
                       "type":"category"}}

        r = requests.put(category_url_num,json=data)
        self.assertEqual(200,r.status_code)

    def step_delete_category(self,categoryid):
        category_url_num = category_url + "/" + str(categoryid)

        r = requests.delete(category_url_num)

        self.assertEqual(204,r.status_code)





    def test_categories(self,):
        self.step_get_categories()
        category = json.loads(self.step_create_category())
        category_id = category["data"]["id"]


        category = self.step_get_category(category_id)
        self.step_modify_category(category_id)
        self.step_delete_category(category_id)



if __name__=='__main__':
    unittest.main()
