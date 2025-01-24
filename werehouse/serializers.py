from rest_framework import serializers
from .models import warehouse
from rest_framework.exceptions import ValidationError

class warehouseSerializer(serializers.ModelSerializer):
    # Specify the input format for the date field
    date = serializers.DateField(
        input_formats=['%Y-%m-%d'],  # Accept DD-MM-YYYY format
        format='%Y-%m-%d'  # Ensure output is also in DD-MM-YYYY format
    )

    class Meta:
        model = warehouse
        fields = ['id','email' ,'date', 'crop', 'quantity', 'storage_condition', 'storage_location', 'batch']

    def create(self, validated_data):
        crop = validated_data.get('crop')
        condition = validated_data.get('storage_condition')
        email = validated_data.get('email')
        batch = (email.split('@')[0] + crop[:2] + condition[:1]).upper()
        validated_data['batch'] = batch

        if warehouse.objects.filter(batch=batch).exists():
            raise ValidationError({'batch': f"A warehouse entry with batch '{batch}' already exists."})
        else:
            warehouse_instanse = warehouse.objects.create(**validated_data)
            return warehouse_instanse