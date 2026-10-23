from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = ["url", "username", "email", "password", "groups"]

    def create(self, validated_data):
        password = validated_data.pop("password", None)

        if not password:
            raise serializers.ValidationError({
                "password": "A password is required when creating a user."
            })

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]