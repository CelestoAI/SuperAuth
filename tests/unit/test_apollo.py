from superauth.apollo_io import Apollo
from unittest.mock import patch
import pytest



@patch("superauth.apollo_io.apollo.requests.Session")
def test_apollo(mock_session):
    apollo = Apollo()
    assert apollo is not None
    assert apollo.contact is not None

@patch("superauth.apollo_io.apollo.requests.Session")
def test_apollo_search(mock_session):
    apollo = Apollo()
    with pytest.raises(ValueError, match="per_page must be less than or equal to 100"):
        apollo.contact.search("john", per_page=101)
    with pytest.raises(ValueError, match="page must be less than or equal to 500"):
        apollo.contact.search("john", page=501)
    response = apollo.contact.search("john")
    