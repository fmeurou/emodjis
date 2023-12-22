"""Emoticons serializer."""

from django.utils.translation import gettext_lazy as _
from .models import Emoji
from rest_framework import serializers


class EmojiFilterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label=_("Search by name"), required=False)
    team = serializers.CharField(
        label=_("Search by team name"), required=False
    )
    nsfw = serializers.BooleanField(
        label=_("Show NSFW emoticons"), required=False
    )
    private = serializers.BooleanField(
        label=_("Show private emoticons only"), required=False
    )

    class Meta:
        model = Emoji
        fields = ["name", "team", "nsfw", "private"]


class EmojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoji
        fields = "__all__"


class EmojiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoji
        fields = ["name"]


class EmojiDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoji
        fields = []


class EmojiCreateSerializer(serializers.ModelSerializer):
    image = serializers.FileField(label=_("File"), required=False)

    class Meta:
        model = Emoji
        fields = ["image", "private", "nsfw", "team"]
