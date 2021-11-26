from rest_framework import serializers
from .models import DefaultSubscription, Subscription, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" # 빼고 만들 콜룸은 없음

class DefaultSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultSubscription
        fields = "__all__" # 빼고 만들 콜룸은 없음

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__" # 빼고 만들 콜룸은 없음

