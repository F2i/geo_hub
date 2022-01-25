from rest_framework import status
import pytest
from model_bakery import baker
from geo_customer_action.models import Action
from geo_customer_action.serializers import ActionSerializer
from django.contrib.contenttypes.models import ContentType
from geo_product.models import GeoProduct


@pytest.fixture
def get_data_from_endpoint(api_client):
    def perform_get_data_from_endpoint(path, data=None):
        return api_client.get(path, data=data, format='json')
    return perform_get_data_from_endpoint


@pytest.mark.django_db
class TestCreateActionData:
    def test_if_request_to_geo_products_list_endpoint_then_action_data_created(self, get_data_from_endpoint):
        contentype_instace = ContentType.objects.get_for_model(GeoProduct)
        model = contentype_instace.model
        path = '/geo-hub/geo-products/'
        query_params = {
            "os_platform": [
                "Window",
                "MacOS"
            ],
            "min_price": "12"
        }

        response = get_data_from_endpoint(path=path, data=query_params)
        latest_action = Action.objects.latest('action_time')
        serializer = ActionSerializer(latest_action)
        data = serializer.data

        assert response.status_code == status.HTTP_200_OK
        assert data['data'] == query_params
        assert data['object_info']['model']['model'] == model
        assert data['object_info']['object_id'] is None
        assert path in data['path']

    def test_if_request_to_geo_products_detail_endpoint_then_action_data_created(self, get_data_from_endpoint):
        contentype_instace = ContentType.objects.get_for_model(GeoProduct)
        model = contentype_instace.model
        pk = 12
        baker.make(GeoProduct, pk=pk)
        path = f'/geo-hub/geo-products/{pk}/'

        response = get_data_from_endpoint(path=path)
        latest_action = Action.objects.latest('action_time')
        serializer = ActionSerializer(latest_action)
        data = serializer.data

        assert response.status_code == status.HTTP_200_OK
        assert data['object_info']['model']['model'] == model
        assert data['object_info']['object_id'] == pk
        assert path in data['path']
