from typing import Optional
import httpx
from ant.celesto.base import CelestoSDKBase

class CelestoCRMContacts(CelestoSDKBase):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_contacts(self):
        response = httpx.get(f"{self.base_url}/crm/contacts", headers=self.headers)
        return response.json()
    
    def create_contact(self, name: str, email: str, client_id: str, linkedin_url: Optional[str]=None):
        headers = self.headers
        # headers["x-current-organization"] = client_id
        response = httpx.post(f"{self.base_url}/crm/contacts", headers=headers, json={
            "name": name,
            "email": email
        })
        return response.json()

