from .models import Action, ActionType, ObjectInfo
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType


class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = ['function_name', 'description']


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ['model', 'app_label']


class ObjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectInfo
        fields = ['model', 'object_id']

    model = ContentTypeSerializer()


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ['id', 'action_type', 'object_info', 'path', 'data', 'action_time']

    action_type = ActionTypeSerializer()
    object_info = ObjectInfoSerializer()
    path = serializers.SerializerMethodField(method_name='get_path')
    data = serializers.SerializerMethodField(method_name='get_data')

    def get_data(self, action: Action):
        list_key_value_tuple = action.data.values_list('key', 'value')
        result_dict = {}
        for key_value_tuple in list_key_value_tuple:
            key = key_value_tuple[0]
            value = key_value_tuple[1]
            if key not in result_dict:
                result_dict[key] = value
            else:
                if type(result_dict[key]) is not list:
                    result_dict[key] = [result_dict[key], value]
                else:
                    result_dict[key] = [*result_dict[key], value]
        return result_dict

    def get_path(self, action: Action):
        return action.path.path
