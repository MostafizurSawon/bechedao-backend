from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    

class ProductPagination(pagination.PageNumberPagination):
    page_size = 10 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = ProductPagination
    search_fields = ['user__first_name', 'user__email', 'category__name']

    def perform_create(self, serializer):
        # Assign the current user as the owner of the Product
        serializer.save(user=self.request.user)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        # Ensure the user is the owner of the product before allowing update
        if instance.user != request.user:
            return Response({"Error": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=None):
        instance = self.get_object()
        # Ensure the user is the owner of the product before allowing deletion
        if instance.user != request.user:
            return Response({"Error": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


# @method_decorator(login_required, name='dispatch')
# class EditPostView(UpdateView):
#     model = models.Post
#     form_class = forms.PostForm
#     template_name = 'add_post.html'
#     pk_url_kwarg = 'id'
#     success_url = reverse_lazy('profile')