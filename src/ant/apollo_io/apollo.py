from typing import Optional
from urllib.parse import urlencode
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

    def search(self, q_keywords: str, per_page: int = 25, page: int = 1) -> dict:
        """
        Search for contacts by keywords.
        
        Args:
            q_keywords: Keywords to search for (name, title, company, etc.)
            per_page: Number of results per page (1-100, default: 25)
            page: Page number to retrieve (starts at 1, default: 1)
        """

        
        base_url = join_url(self.base_url, "contacts/search")
        query_params = urlencode({
            "q_keywords": q_keywords,
            "per_page": per_page,
            "page": page
        })
        url = f"{base_url}?{query_params}"
        
        # Send POST request without params argument
        response = requests.post(url, headers=self._parent_cls.headers)
        return response.json()

    def list_all_stages(self) -> dict:
        """
        List all contact stages.

        Ref: https://docs.apollo.io/reference/list-contact-stages
        """
        url = join_url(self.base_url, "contact_stages")
        response = requests.get(url, headers=self._parent_cls.headers)
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
