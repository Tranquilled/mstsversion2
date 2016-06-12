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

resource_url = base_url + '/' + 'resources'

class ResourceTest(unittest.TestCase):
    def setUp(self,):
        # Test to see if connected to site. If not an error is thrown right
        # away
        r = requests.get(base_url)
        self.assertEqual(r.status_code,200)

    def step_get_resources(self,):
        r = requests.get(resource_url)
        print(r.text)

    def step_get_resource(self,resourceid):
        resource_url_num = resource_url + "/" + str(resourceid)
        r = requests.get(resource_url_num)
        self.assertEqual(200,r.status_code)

    def step_create_resource(self,):
        data = {"data":{"attributes":{"url":"http://google.com",
                       "title":"Google",
                       "category":"1",
                       "description":"A great search engine."},
                       "headers":'text/json',
                       "type":"resource"}}
        r = requests.post(resource_url,json=data)
        print(r.text)
        self.assertEqual(r.status_code,201)
        return r.text

    def step_modify_resource(self,resourceid):
        resource_url_num = resource_url + "/" + str(resourceid)
        data = {"data":{"attributes":{"url":"http://www.bing.com",
                       "title":"Bing",
                       "category":"1",
                       "description":"A great search engine too."},
                       "headers":'text/json',
                       "type":"resource"}}

        r = requests.put(resource_url_num,json=data)
        print(r.text)
        self.assertEqual(200,r.status_code)

    def step_delete_resource(self,resourceid):
        resource_url_num = resource_url + "/" + str(resourceid)

        r = requests.delete(resource_url_num)

        self.assertEqual(204,r.status_code)





    def test_resources(self,):
        self.step_get_resources()
        resource = json.loads(self.step_create_resource())
        resource_id = resource["data"]["id"]


        resource = self.step_get_resource(resource_id)
        self.step_modify_resource(resource_id)
        self.step_delete_resource(resource_id)



if __name__=='__main__':
    unittest.main()
