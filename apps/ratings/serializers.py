from rest_framework import serializers

from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    def get_rater(self, obj):
        # rater foreignkey la User-> co field username
        return obj.rater.username

    def get_agent(self, obj):
        # agent co foreigkey la Profile, Profile <-> User qua field user nen username phai lay tu user.
        return obj.agent.user.username
