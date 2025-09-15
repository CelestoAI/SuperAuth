from ant.apollo_io import Apollo
from unittest.mock import patch



@patch("ant.apollo_io.apollo.requests.get")
def test_apollo(mock_get):
    apollo = Apollo()
    assert apollo is not None
    assert apollo.contact is not None
