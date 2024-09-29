from rest_framework import serializers
from my_site.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'get_article', 'get_image', 'date_posted']