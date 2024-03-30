# fields.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class VideoField(models.FileField):
    default_validators = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value:
            content_type = value.file.content_type
            if 'video' not in content_type:
                raise ValidationError(_('File is not a video.'), code='invalid')

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs
