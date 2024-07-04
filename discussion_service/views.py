from rest_framework import viewsets
from .models import Discussion
from .serializers import DiscussionSerializer

class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
