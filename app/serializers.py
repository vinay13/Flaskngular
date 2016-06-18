from marshmallow import Serializer, fields

class UserSerializer(Serializer):
    class Meta:
        fields = ("id", "email")

class PostSerializer(Serializer):
    author = fields.Nested(UserSerializer)

    class Meta:
        fields = ("id", "title", "content")