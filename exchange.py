import json

import requests
from requests.auth import HTTPBasicAuth


class Exchange:

    def __init__(self, option, barcode):
        self.barcode = barcode
        self.option = option


    def get_barcode(self):
        url = f'http://{self.option.get('ip')}/{self.option.get('api')}'
        params = {'barcode': self.barcode}
        user_name = self.option.get('login')
        password = self.option.get('password')
        user_name_utf8 = user_name.encode('utf-8')

        auth = HTTPBasicAuth(username=user_name_utf8, password=password)

        try:
            answer = requests.get(url, params=params, auth=auth,
                                  headers={'Content-Type': 'application/json; charset=utf-8'})
            answer.encoding = 'utf-8'

            if answer.status_code == 200:
                json_data = json.loads(answer.content,)
                return json_data


        except requests.exceptions.RequestException as e:
            print(f'Произошла ошибка при отправке запроса: {e}')
            return None
