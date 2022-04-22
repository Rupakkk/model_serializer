from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)  # We can do this way too
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name','age']
        # extra_kwargs = {'name':{'read_only' :True}}  #  We can do  it this way too

    def validate_name(self,value):
        if value != 'Ram'.lower():
            raise serializers.ValidationError('Name must be only Ram')
        return value

    def validate(self,data):
        nm = data.get('name')
        ag = data.get('age')
        if nm.lower() == 'hari' and ag != 25:
            raise serializers.ValidationError('Age should be 25')
        return data

    def start_with(value):
        if value[0].lower != 'r':
            raise serializers.ValidationError('Must start with r')

    name = serializers.CharField(validators = [start_with])
        