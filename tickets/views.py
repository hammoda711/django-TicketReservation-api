
from .models import Guest, Movie, Reservation, Post
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer, PostSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics, viewsets

'''
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
'''
# Create your views here.

#viewsets
class viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class viewsets_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backend = [filters.SearchFilter]
    search_fields = ['movie']

class viewsets_reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = Reservation
    # auth in view level
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

#Find movie
@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(
        hall = request.data['hall'],
        movie = request.data['movie'],
    )
    serializer = MovieSerializer(movies, many= True)
    return Response(serializer.data)

#create new reservation 
@api_view(['POST'])
def new_reservation(request):

    movie = Movie.objects.get(
        hall = request.data['hall'],
        movie = request.data['movie'],
    )
    guest = Guest()
    guest.name = request.data['name']
    guest.mobile = request.data['mobile']
    guest.save()

    reservation = Reservation()
    reservation.guest = guest
    reservation.movie = movie
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)

'''
#post author editor
class Post_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''