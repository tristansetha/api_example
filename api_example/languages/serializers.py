from rest_framework import serializers
from .models import Language

# modelserializer
# serializers.ModelSerializer -> standard for rest. It will show you information that is relevant to models
# also has functionality to create new models/languages and update model/language
class LanguageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Language
    fields = ('id', 'name', 'paradigm')
