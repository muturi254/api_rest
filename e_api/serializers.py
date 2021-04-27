from rest_framework import serializers

from e_api.models import Category, Product, Book
# serializers 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_tag', 'name', 'price', 'stock', 'description', 'imageUrl', 'status', 'date_created', 'category']


class BookSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'pages', 'price', 'stock', 'description', 'imageUrl', 'status', 'date_created', 'category']