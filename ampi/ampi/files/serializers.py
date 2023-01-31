from rest_framework import serializers

from ampi.ampi.files.models import File


class FileSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        owner = self.context['request'].user
        return owner

    class Meta:
        model = File
        fields = ['id', 'name', 'file', 'owner']
        read_only_fields = ('id', 'name', 'file', 'owner')
