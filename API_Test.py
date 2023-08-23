import pytest
from APIFunctions import *


class TestAPI:
    @pytest.fixture()
    def url(self):
        '''
        Get the base URL of the API.
        :return: The base URL of the API.
        '''
        return 'https://reqres.in/api/'


    def test_update_user(self,url):
        data = {"name": "morpheus",
                "job": "zion resident"}
        status_code, update_data = update_user(url,'users/2',data)
        assert status_code == 200 and update_data['name'] == data['name'] and update_data['job'] == data['job']


    def test_partial_update_user(self,url):
        data = {"name": "morpheus",
                "job": "zion resident"}
        status_code, update_data = update_user(url,'users/1',data)
        assert status_code == 200 and update_data['name'] == data['name'] and update_data['job'] == data['job']


    def test_delete_user(self,url):
        status_code = delete_user(url,'users/3')
        assert status_code == 204                       # האם להוסיף בדיקה של גייסון?


    def test_list_user(self,url):
        list_status_code, list1 = list_user(url, 'users/')
        list_status_code,list2 = list_user(url, 'users?page=2')
        lists = list1+list2
        assert list_status_code == 200  and  lists is not {}           # לוודא שקיים 12 אנשים או שמספיק לוודא שהרשימה לא ריקה


    def test_register_P(self,url):
        data = {"email": "eve.holt@reqres.in",
                "password": "pistol"}
        register_status_code , register = user_register(url,'register',data)
        assert register_status_code == 200 and register is not {}


    def test_register_N(self,url):
        data = {"email": "sydney@fife"}
        register_status_code, register = user_register(url,'register',data)
        assert register_status_code == 400
