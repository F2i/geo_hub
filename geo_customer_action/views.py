from rest_framework.viewsets import ModelViewSet
from .serializers import ActionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ActionView(ModelViewSet):
    serializer_class = ActionSerializer
    queryset = ActionSerializer.Meta.model.objects.all()

    @action(detail=False)
    def latest(self, request):
        if not self.queryset.exists():
            return Response(None)
        latest_action = self.queryset.latest('action_time')
        serializer = self.get_serializer_class()(latest_action)
        return Response(serializer.data)
