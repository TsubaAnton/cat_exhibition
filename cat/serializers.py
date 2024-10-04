from .models import Cat, Breed, Rating
from rest_framework import serializers


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['cat', 'user', 'score']
        read_only_fields = ('user',)

