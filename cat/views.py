from .models import Cat, Breed
from .serializers import CatSerializer, BreedSerializer, RatingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class CatListAPIView(generics.ListAPIView):
    """Представление для вывода списка котят и получения списка котят определенной породы по фильтру"""
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Cat.objects.all()
        breed_id = self.request.query_params.get('breed', None)
        if breed_id is not None:
            queryset = queryset.filter(breed_id=breed_id)
        return queryset


class CatCreateAPIView(generics.CreateAPIView):
    """Представление для создания котенка"""
    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CatRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для получения подробной информации о котенке"""
    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)


class CatUpdateAPIView(generics.UpdateAPIView):
    """Представление для добавления и изменения информации о котенке"""
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)


class CatDestroyAPIView(generics.DestroyAPIView):
    """Представление для удаления информации о котенке"""
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)


class BreedListAPIView(generics.ListAPIView):
    """Представление для получения списка пород"""
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
    permission_classes = [IsAuthenticated]


class BreedCreateAPIView(generics.CreateAPIView):
    """Представление для создания породы"""
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
    permission_classes = [IsAuthenticated]


class RatingCreateAPIView(generics.CreateAPIView):
    """Представление для оценивания котят"""
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        rating = serializer.save(user=self.request.user)
        cat = rating.cat
        cat.ratings_count += 1
        cat.ratings_score = (cat.ratings_score * (cat.ratings_count - 1) + int(rating.score)) / cat.ratings_count
        cat.save()
