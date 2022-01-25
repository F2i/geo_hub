from django.db import models
from django.contrib.contenttypes.models import ContentType


class ActionType(models.Model):
    function_name = models.CharField(max_length=255, unique=True, null=False)
    description = models.CharField(max_length=255, unique=True, null=False)


class ActionPath(models.Model):
    path = models.CharField(max_length=255, unique=True, null=False)


class ObjectInfo(models.Model):
    model = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField(null=True)


class ActionData(models.Model):
    key = models.CharField(max_length=255, null=False)
    value = models.CharField(max_length=255, null=False)


class Action(models.Model):
    action_type = models.ForeignKey(ActionType, on_delete=models.PROTECT)
    path = models.ForeignKey(ActionPath, on_delete=models.PROTECT)
    object_info = models.ForeignKey(ObjectInfo, on_delete=models.PROTECT)
    data = models.ManyToManyField(ActionData, blank=True)
    action_time = models.DateTimeField(auto_now_add=True)
