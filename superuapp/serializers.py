from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from superuapp.models import Profile


class ProfileAPiSerilizer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=Profile.objects.all())])
    class Meta:
        model = Profile
        fields = '__all__'
    
    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        if validated_data.get('name'):
            instance.name = validated_data['name']
        if validated_data.get('bio'):
            instance.bio = validated_data['bio']
        if validated_data.get('profile_picture'):
            instance.profile_picture = validated_data['profile_picture']
        instance.save()
        return instance

