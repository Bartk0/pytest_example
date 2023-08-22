import requests
from re import findall


class ApiConsts:
    DATA = 'data'
    ID = 'id'
    MSG = 'message'


class DataConsts:
    JSON_DEFAULT = {"status": True, "data": {"id": "FEFE", "some_field": "some_field_data"}}
    XML_DEFAULT = '<?xml version="1.0" encoding="utf-8"?>' \
                  '<status>True</status>' \
                  '<data>' \
                  '<id>FEFE</id>' \
                  '<some_field>some_field_data</some_field>' \
                  '</data>'
    RESPONSE_UNKNOWN_PATH = '''Hello there. This is a default server response. 
    Try valid URLs: ['/health', '/json', '/xml']'''


class XML:
    def __init__(self, host, port, DataConsts=DataConsts, ApiConsts=ApiConsts):
        self.host = host if "http://" in host else f"http://{host}"
        self.port = port
        self.base_url = f"{self.host}:{self.port}/xml"
        self.DataConsts = DataConsts
        self.ApiConsts = ApiConsts

    def reset_data(self):
        response = requests.post(url=self.base_url, data=self.DataConsts.XML_DEFAULT)
        assert response.status_code == 200
        return response.json()

    def send_data(self, xml_data):
        response = requests.post(url=self.base_url, data=xml_data)
        assert response.status_code == 200
        return response.content.decode()

    def read_data(self):
        response = requests.get(url=self.base_url)
        assert response.status_code == 200
        return response.content.decode()


class JSON:
    def __init__(self, host, port, DataConsts=DataConsts, ApiConsts=ApiConsts):
        self.host = host if "http://" in host else f"http://{host}"
        self.port = port
        self.base_url = f"{self.host}:{self.port}/json"
        self.DataConsts = DataConsts
        self.ApiConsts = ApiConsts

    def reset_data(self):
        response = requests.post(url=self.base_url, json=self.DataConsts.JSON_DEFAULT)
        assert response.status_code == 200
        return response.json()

    def send_data(self, json_data):
        response = requests.post(url=self.base_url, json=json_data)
        assert response.status_code == 200
        return response.json()

    def read_data(self):
        response = requests.get(url=self.base_url)
        assert response.status_code == 200
        return response.json()

    def get_data_id(self):
        return self.read_data()[ApiConsts.DATA][ApiConsts.ID]


class CommonMethods:
    def __init__(self, host, port, DataConsts=DataConsts, ApiConsts=ApiConsts):
        self.host = host if "http://" in host else f"http://{host}"
        self.port = port
        self.base_url = f"{self.host}:{self.port}/"
        self.DataConsts = DataConsts
        self.ApiConsts = ApiConsts

    def get_invalid_path(self):
        response = requests.get(url=f'{self.base_url}/some_bad_path')
        assert response.status_code == 200
        return response.json()

    def get_valid_paths_list(self):
        return findall(r'/[a-z]*', self.get_invalid_path()[ApiConsts.MSG])
