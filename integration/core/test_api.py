import pytest
import cattle
import requests


@pytest.fixture
def client():
    url = 'http://localhost:8088/v1-catalog/schemas'
    return cattle.from_env(url=url)


def test_catalog_list(client):
    catalogs = client.list_catalog()
    assert len(catalogs) > 0


def test_catalog_state_uri_present(client):
    catalogs = client.list_catalog()
    assert len(catalogs) > 0

    for i in range(len(catalogs)):
        assert catalogs[i].state is not None
        assert catalogs[i].uri is not None


def test_template_list(client):
    templates = client.list_template()
    assert len(templates) > 0


def test_refresh_catalog(client):
    url = 'http://localhost:8088/v1-catalog/templates?action=refresh'
    response = requests.post(url)
    assert response.status_code == 200
