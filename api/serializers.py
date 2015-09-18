from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin

from api.models import *


class ProductSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Product
        fields = (
            'id', 'name', 'description', 'product_relationship', 'categories')
        list_serializer_class = BulkListSerializer


class Product_relationshipSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Product_relationship
        fields = ('id', 'relation_type', 'description',
                  'relating_product', 'related_product')
        list_serializer_class = BulkListSerializer


class Product_versionSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Product_version
        fields = ('id', 'description', 'relationship')
        list_serializer_class = BulkListSerializer


class Product_version_relationshipSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Product_version_relationship
        fields = ('id', 'description', 'related_version', 'relating_version')
        list_serializer_class = BulkListSerializer


class Product_categorySerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Product_category
        fields = ('id', 'name', 'description', 'assigment')
        list_serializer_class = BulkListSerializer


class Product_category_assignmentSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Product_category_assignment
        fields = ('id', 'products')
        list_serializer_class = BulkListSerializer


class Product_category_hierarchySerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Product_category_hierarchy
        fields = ('id',)
        list_serializer_class = BulkListSerializer


class Product_view_definitionSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Product_view_definition
        fields = ('id', 'name', 'additionnal_characterization')
        list_serializer_class = BulkListSerializer


class View_definition_contextSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = View_definition_context
        fields = (
            'id', 'application_domain', 'life_cycle_stage', 'description')
        list_serializer_class = BulkListSerializer


class Product_property_assignmentSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Product_property_assignment
        fields = ('id',)
        list_serializer_class = BulkListSerializer


class View_definition_relationshipSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = View_definition_relationship
        fields = ('id', 'relation_type', 'description')
        list_serializer_class = BulkListSerializer


class View_definition_usageSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = View_definition_usage
        fields = ('id',)
        list_serializer_class = BulkListSerializer


class Assembly_component_relationshipSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Assembly_component_relationship
        fields = ('id', 'location_indicator')
        list_serializer_class = BulkListSerializer


class Next_assembly_usageSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Next_assembly_usage
        fields = ('id',)
        list_serializer_class = BulkListSerializer


class Component_upper_level_identificationSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Component_upper_level_identification
        fields = ('id',)
        list_serializer_class = BulkListSerializer


class Promissory_usageSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Promissory_usage
        fields = ('id',)
        list_serializer_class = BulkListSerializer


class Value_with_unitSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Value_with_unit
        fields = ('id',)
        list_serializer_class = BulkListSerializer


class UnitSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Unit
        fields = ('id', 'name', 'si_unit')
        list_serializer_class = BulkListSerializer


class Measure_valueSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Measure_value
        fields = ('id',)
        list_serializer_class = BulkListSerializer


class any_number_valueSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta(object):
        model = any_number_value
        fields = ('id', 'any_number_value')
        list_serializer_class = BulkListSerializer
