from django.forms import widgets
from rest_framework import serializers
from weather.models import Weather
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    weather = serializers.PrimaryKeyRelatedField(many=True, queryset=Weather.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'weather')

class WeatherSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    pk = serializers.IntegerField(read_only=True)
    comment = serializers.CharField(required=False, allow_blank=True, max_length=100)

    stantion_date = serializers.DateTimeField()

    bmp180temp = serializers.FloatField(max_value=None, min_value=None)
    bmp180pres = serializers.FloatField(max_value=None, min_value=None)
    v_bat = serializers.FloatField(max_value=None, min_value=None)
    v_ref = serializers.FloatField(max_value=None, min_value=None)
    v_sun = serializers.FloatField(max_value=None, min_value=None)
    humid = serializers.FloatField(max_value=None, min_value=None)

    class Meta:
        model = Weather
        fields = ('id', 'owner', 'comment', 'bmp180temp', 'bmp180pres', 'v_bat', 'v_sun')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Weather.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        
	instance.comment = validated_data.get('comment', instance.comment)     
	instance.stantion_date = validated_data.get('stantion_date', instance.stantion_date)
	instance.bmp180temp = validated_data.get('bmp180temp', instance.bmp180temp)


        instance.save()
        return instance
