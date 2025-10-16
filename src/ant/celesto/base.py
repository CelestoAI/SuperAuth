class CelestoSDKBase:
    def __init__(self, api_key: str):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError(
                "API key is required. You can find it in the Celesto security settings."
            )
        self.base_url = "https://api.celesto.ai/v1"
        self._headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    @property
    def headers(self):
        return self._headers
