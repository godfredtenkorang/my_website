from rest_framework.decorators import api_view
from rest_framework.response import Response
from my_site.models import Blog
from .serializers import BlogSerializer
from rest_framework import status

@api_view(['GET'])
def blog_view(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_blog(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)