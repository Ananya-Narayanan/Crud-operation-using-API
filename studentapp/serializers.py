from rest_framework import serializers
from studentapp.models import studentdb

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=studentdb
        fields='__all__'