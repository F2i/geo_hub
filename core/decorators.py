from functools import wraps
from .signals import request_coming
from geo_customer_action.signals.handlers import create_customer_action_data


def request_coming_decorator(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        request_coming.connect(create_customer_action_data)
        request_coming.send_robust(
            sender=request.parser_context['view'].__class__,
            request=request,
            function_name=func.__name__,
            **kwargs
        )
        return func(request, *args, **kwargs)
    return wrap
