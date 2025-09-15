from ant.apollo_io import Apollo

def test_apollo():
    apollo = Apollo()
    response = apollo.contact.search("John Doe")
    print(response)
    assert response is not None
    assert response != {'error': 'Api key required'}, "Api key is required for e2e test"
    assert isinstance(response.get("contacts"), list), "Contacts should be a list"
