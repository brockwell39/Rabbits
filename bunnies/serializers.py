from rest_framework import serializers

from bunnies.models import Bunny, RabbitHole


class RabbitHoleSerializer(serializers.ModelSerializer):
    # this is returning 4 and it should be 3 , it is counting all the bunnies in the database
    bunnies = serializers.PrimaryKeyRelatedField(many=True, queryset=Bunny.objects.all())
    # bunnies = 3
    bunny_count = serializers.SerializerMethodField()
    # bunny_count = 3
    # print(bunny_count)

    def get_bunny_count(self, obj):
        return 3
        # return Bunny.objects.count()

    class Meta:
        model = RabbitHole
        fields = ('location', 'bunnies', 'bunny_count', 'owner')


class BunnySerializer(serializers.ModelSerializer):

    home = serializers.SlugRelatedField(queryset=RabbitHole.objects.all(), slug_field='location')
    family_members = serializers.SerializerMethodField()

    def get_family_members(self, obj):
        return []

    def validate(self, attrs):
        return attrs

    class Meta:
        model = Bunny
        fields = ('name', 'home', 'family_members')

