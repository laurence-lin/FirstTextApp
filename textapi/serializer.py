from .models import Book
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
import bleach

class BookSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source = 'name') # Rename model field to custom field name
    def validate_title(self, data):
        return bleach.clean(data)
    class Meta:  # Override model field
        model = Book
        fields = ['book_name', 'title', 'author', 'price']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        extra_kwargs = {'price':{'min_value':2}, # To validate data fields later
        'inventory':{'min_value':0},
        'title':{'validators': [
            UniqueValidator(
                 queryset=MenuItem.objects.all()
                 )
             ]
        }
        }
