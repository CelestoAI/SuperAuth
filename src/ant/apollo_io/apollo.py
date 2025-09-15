from typing import Optional
from ant.config import config
import requests
from ant.utils import join_url

class _Base:
    def __init__(self, parent_cls: "Apollo"):
        self._parent_cls = parent_cls
    
    @property
    def base_url(self) -> str:
        return self._parent_cls.BASE_URL


class Contact(_Base):

    def search(self, q_keywords: str, per_page: int = 4, page: int = 10) -> dict:
        """
        Search for contacts by keywords.

        Args:
            q_keywords: Keywords to search for.

        Ref: https://docs.apollo.io/reference/search-for-contacts
        """
        url = join_url(self.base_url, "contacts/search")
        response = requests.get(url, headers=self._parent_cls.headers, params={"q_keywords": q_keywords})
        return response.json()




class Apollo:
    BASE_URL = "https://api.apollo.io/api/v1/"

    def __init__(self, api_key: Optional[str] = None): 
        self.api_key = api_key or config.apollo_api_key.get_secret_value()
        self.headers = {
            "accept": "application/json",
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "x-api-key": self.api_key
        }

        self.contact = Contact(self)
