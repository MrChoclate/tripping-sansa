from rest_framework import serializers

from api.models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'product_relationship', 'categories')


class Product_relationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_relationship
        fields = ('id', 'relation_type', 'description',
                  'relating_product', 'related_product')


class Product_versionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_version
        fields = ('id', 'description', 'relationship')


class Product_version_relationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_version_relationship
        fields = ('id', 'description', 'related_version', 'relating_version')


class Product_categorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_category
        fields = ('id', 'name', 'description', 'assigment')


class Product_category_assignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_category_assignment
        fields = ('id', 'products')


class Product_category_hierarchySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_category_hierarchy
        fields = ('id',)


class Product_view_definitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_view_definition
        fields = ('id', 'name', 'additionnal_characterization')


class View_definition_contextSerializer(serializers.ModelSerializer):

    class Meta:
        model = View_definition_context
        fields = (
            'id', 'application_domain', 'life_cycle_stage', 'description')


class Product_property_assignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_property_assignment
        fields = ('id',)


class View_definition_relationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = View_definition_relationship
        fields = ('id', 'relation_type', 'description')


class View_definition_usageSerializer(serializers.ModelSerializer):

    class Meta:
        model = View_definition_usage
        fields = ('id',)


class Assembly_component_relationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assembly_component_relationship
        fields = ('id', 'location_indicator')


class Next_assembly_usageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Next_assembly_usage
        fields = ('id',)


class Component_upper_level_identificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Component_upper_level_identification
        fields = ('id',)


class Promissory_usageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promissory_usage
        fields = ('id',)


class Value_with_unitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Value_with_unit
        fields = ('id',)


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ('id', 'name', 'si_unit')


class Measure_valueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measure_value
        fields = ('id',)


class any_number_valueSerializer(serializers.ModelSerializer):

    class Meta:
        model = any_number_value
        fields = ('id', 'any_number_value')
