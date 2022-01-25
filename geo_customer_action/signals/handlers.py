from geo_customer_action import models
from django.contrib.contenttypes.models import ContentType

DESCIPTION_DICTIONARY = {
    'list': 'View a list of objects',
    'retrieve': 'View detail of an object'
}


def create_customer_action_data(sender, **kwargs):
    request = kwargs['request']
    function_name = kwargs['function_name']
    query_params = dict(request.query_params)
    model_class = sender.serializer_class.Meta.model
    path = request.build_absolute_uri(request.path)

    path_instance, status = models.ActionPath.objects.get_or_create(path=path)
    model = ContentType.objects.get_for_model(model_class)
    action_type_instance, status = models.ActionType.objects.get_or_create(
        function_name=function_name,
        description=DESCIPTION_DICTIONARY[function_name]
    )

    object_id = kwargs.get('pk')
    object_info_instance, status = models.ObjectInfo.objects.get_or_create(
        model=model,
        object_id=object_id
    )

    action_instance = models.Action.objects.create(
        action_type=action_type_instance,
        object_info=object_info_instance,
        path=path_instance
    )

    for key in query_params:
        value_list = query_params[key]
        if value_list.count('') < len(value_list):
            for value in value_list:
                if value != '':
                    action_data_instance, status = models.ActionData.objects.get_or_create(
                        key=key,
                        value=value
                    )
                    action_instance.data.add(action_data_instance)
