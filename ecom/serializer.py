from rest_framework import serializers
from .models import Product,Pictures

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Pictureserializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = '__all__'

# class Imgserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pictures
#         fields = ['pic']
#
#
# class ProductWithFirstPictureSerializer(serializers.ModelSerializer):
#     first_picture = serializers.SerializerMethodField() # Define a custom field
#
#     class Meta: model = Product
#     fields = ['id', 'name', 'price','added_in','description','rcg_tag','type','first_picture']
#
#     def get_first_pic(self,obj):
#         fst_picture = obj.pictures.first()
#         return Imgserializer(fst_picture).data

