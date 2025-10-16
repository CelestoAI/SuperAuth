from superauth.celesto.crm.contacts import CelestoCRMContacts
from dotenv import load_dotenv
from superauth.config import config
load_dotenv()

def test_celesto_crm_contacts():
    celesto_crm_contacts = CelestoCRMContacts(api_key=config.celesto_api_key.get_secret_value())
    response = celesto_crm_contacts.get_contacts()
    assert len(response) > 0


def test_celesto_crm_contacts_create_contact():
    celesto_crm_contacts = CelestoCRMContacts(api_key=config.celesto_api_key.get_secret_value())
    response = celesto_crm_contacts.create_contact("John Doe", "john.doe@example.com", "1234567890")
    assert response is not None
    assert response.get("name") == "John Doe"
    assert response.get("email") == "john.doe@example.com"
