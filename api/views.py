from rest_framework import viewsets

from api.serializers import *
from api.models import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product_relationshipViewSet(viewsets.ModelViewSet):
    queryset = Product_relationship.objects.all()
    serializer_class = Product_relationshipSerializer


class Product_versionViewSet(viewsets.ModelViewSet):
    queryset = Product_version.objects.all()
    serializer_class = Product_versionSerializer


class Product_version_relationshipViewSet(viewsets.ModelViewSet):
    queryset = Product_version_relationship.objects.all()
    serializer_class = Product_version_relationshipSerializer


class Product_categoryViewSet(viewsets.ModelViewSet):
    queryset = Product_category.objects.all()
    serializer_class = Product_categorySerializer


class Product_category_assignmentViewSet(viewsets.ModelViewSet):
    queryset = Product_category_assignment.objects.all()
    serializer_class = Product_category_assignmentSerializer


class Product_category_hierarchyViewSet(viewsets.ModelViewSet):
    queryset = Product_category_hierarchy.objects.all()
    serializer_class = Product_category_hierarchySerializer


class Product_view_definitionViewSet(viewsets.ModelViewSet):
    queryset = Product_view_definition.objects.all()
    serializer_class = Product_view_definitionSerializer


class View_definition_contextViewSet(viewsets.ModelViewSet):
    queryset = View_definition_context.objects.all()
    serializer_class = View_definition_contextSerializer


class Product_property_assignmentViewSet(viewsets.ModelViewSet):
    queryset = Product_property_assignment.objects.all()
    serializer_class = Product_property_assignmentSerializer


class View_definition_relationshipViewSet(viewsets.ModelViewSet):
    queryset = View_definition_relationship.objects.all()
    serializer_class = View_definition_relationshipSerializer


class View_definition_usageViewSet(viewsets.ModelViewSet):
    queryset = View_definition_usage.objects.all()
    serializer_class = View_definition_usageSerializer


class Assembly_component_relationshipViewSet(viewsets.ModelViewSet):
    queryset = Assembly_component_relationship.objects.all()
    serializer_class = Assembly_component_relationshipSerializer


class Next_assembly_usageViewSet(viewsets.ModelViewSet):
    queryset = Next_assembly_usage.objects.all()
    serializer_class = Next_assembly_usageSerializer


class Component_upper_level_identificationViewSet(viewsets.ModelViewSet):
    queryset = Component_upper_level_identification.objects.all()
    serializer_class = Component_upper_level_identificationSerializer


class Promissory_usageViewSet(viewsets.ModelViewSet):
    queryset = Promissory_usage.objects.all()
    serializer_class = Promissory_usageSerializer


class Value_with_unitViewSet(viewsets.ModelViewSet):
    queryset = Value_with_unit.objects.all()
    serializer_class = Value_with_unitSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class Measure_valueViewSet(viewsets.ModelViewSet):
    queryset = Measure_value.objects.all()
    serializer_class = Measure_valueSerializer


class any_number_valueViewSet(viewsets.ModelViewSet):
    queryset = any_number_value.objects.all()
    serializer_class = any_number_valueSerializer
