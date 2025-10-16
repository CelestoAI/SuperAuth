from typing import Optional
from urllib.parse import urlencode

import requests

from superauth.config import config
from superauth.utils import join_url


class _Base:
    def __init__(self, parent_cls: "Apollo"):
        self._parent_cls = parent_cls

    @property
    def base_url(self) -> str:
        return self._parent_cls.BASE_URL

    @property
    def session(self) -> requests.Session:
        return self._parent_cls.session


class Contact(_Base):
    def search(self, q_keywords: str, per_page: int = 25, page: int = 1) -> dict:
        """
        Search for contacts by keywords.

        Args:
            q_keywords: Keywords to search for (name, title, company, etc.)
            per_page: Number of results per page (1-100, default: 25)
            page: Page number to retrieve (starts at 1, default: 1)
        """

        if per_page > 100 or per_page < 1:
            raise ValueError("per_page must be less than or equal to 100")
        if page > 500 or page < 1:
            raise ValueError("page must be less than or equal to 500")

        base_url = join_url(self.base_url, "contacts/search")
        query_params = urlencode(
            {"q_keywords": q_keywords, "per_page": per_page, "page": page}
        )
        url = f"{base_url}?{query_params}"

        response = self.session.post(url)
        return response.json()

    def list_all_stages(self) -> dict:
        """
        List all contact stages.

        Ref: https://docs.apollo.io/reference/list-contact-stages
        """
        url = join_url(self.base_url, "contact_stages")
        response = self.session.get(url)
        return response.json()


class Apollo:
    BASE_URL = "https://api.apollo.io/api/v1/"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or config.apollo_api_key.get_secret_value()
        headers = {
            "accept": "application/json",
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
        }
        self.session = requests.Session()
        self.session.headers.update(headers)
        self.contact = Contact(self)
