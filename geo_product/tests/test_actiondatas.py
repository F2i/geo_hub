from rest_framework import status
import pytest
from model_bakery import baker
from geo_product.models import GeoProduct


@pytest.fixture
def get_data_from_endpoint(api_client):
    def perform_get_data_from_endpoint(path, data=None):
        return api_client.get(path, data=data, format='json')
    return perform_get_data_from_endpoint


@pytest.mark.django_db
class TestGetGeoProduct:
    def test_get_geo_product_list(self, get_data_from_endpoint):
        path = '/geo-hub/geo-products/'
        quantity = 3

        baker.make(GeoProduct, _quantity=quantity)
        response = get_data_from_endpoint(path=path)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == quantity

    def test_get_geo_product_detail(self, get_data_from_endpoint):
        pk = 12
        path = f'/geo-hub/geo-products/{pk}/'

        baker.make(GeoProduct, pk=12)
        response = get_data_from_endpoint(path=path)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == pk
