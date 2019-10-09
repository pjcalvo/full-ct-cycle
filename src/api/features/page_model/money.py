import requests
from src.api.features.page_model.api_base import ApiBase

class Money(ApiBase):
    MONEY_BASE_URL = '/money'

    def formatMoney(self,money):
        response = requests.get(f"{self.url}{self.MONEY_BASE_URL}?value={money}", verify=False)
        return response