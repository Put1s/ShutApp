from django.db import models


def get_fields(model, object):
    result = dict()
    for field in model._meta.get_fields():
        if field.name != 'logentry':
            value = getattr(object, field.name)
            result[field.name] = value
    # print(result)
    return result
