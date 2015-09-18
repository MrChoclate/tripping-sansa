from rest_framework_bulk import BulkModelViewSet

from api.serializers import *
from api.models import *


class ProductViewSet(BulkModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product_relationshipViewSet(BulkModelViewSet):
    queryset = Product_relationship.objects.all()
    serializer_class = Product_relationshipSerializer


class Product_versionViewSet(BulkModelViewSet):
    queryset = Product_version.objects.all()
    serializer_class = Product_versionSerializer


class Product_version_relationshipViewSet(BulkModelViewSet):
    queryset = Product_version_relationship.objects.all()
    serializer_class = Product_version_relationshipSerializer


class Product_categoryViewSet(BulkModelViewSet):
    queryset = Product_category.objects.all()
    serializer_class = Product_categorySerializer


class Product_category_assignmentViewSet(BulkModelViewSet):
    queryset = Product_category_assignment.objects.all()
    serializer_class = Product_category_assignmentSerializer


class Product_category_hierarchyViewSet(BulkModelViewSet):
    queryset = Product_category_hierarchy.objects.all()
    serializer_class = Product_category_hierarchySerializer


class Product_view_definitionViewSet(BulkModelViewSet):
    queryset = Product_view_definition.objects.all()
    serializer_class = Product_view_definitionSerializer


class View_definition_contextViewSet(BulkModelViewSet):
    queryset = View_definition_context.objects.all()
    serializer_class = View_definition_contextSerializer


class Product_property_assignmentViewSet(BulkModelViewSet):
    queryset = Product_property_assignment.objects.all()
    serializer_class = Product_property_assignmentSerializer


class View_definition_relationshipViewSet(BulkModelViewSet):
    queryset = View_definition_relationship.objects.all()
    serializer_class = View_definition_relationshipSerializer


class View_definition_usageViewSet(BulkModelViewSet):
    queryset = View_definition_usage.objects.all()
    serializer_class = View_definition_usageSerializer


class Assembly_component_relationshipViewSet(BulkModelViewSet):
    queryset = Assembly_component_relationship.objects.all()
    serializer_class = Assembly_component_relationshipSerializer


class Next_assembly_usageViewSet(BulkModelViewSet):
    queryset = Next_assembly_usage.objects.all()
    serializer_class = Next_assembly_usageSerializer


class Component_upper_level_identificationViewSet(BulkModelViewSet):
    queryset = Component_upper_level_identification.objects.all()
    serializer_class = Component_upper_level_identificationSerializer


class Promissory_usageViewSet(BulkModelViewSet):
    queryset = Promissory_usage.objects.all()
    serializer_class = Promissory_usageSerializer


class Value_with_unitViewSet(BulkModelViewSet):
    queryset = Value_with_unit.objects.all()
    serializer_class = Value_with_unitSerializer


class UnitViewSet(BulkModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class Measure_valueViewSet(BulkModelViewSet):
    queryset = Measure_value.objects.all()
    serializer_class = Measure_valueSerializer


class any_number_valueViewSet(BulkModelViewSet):
    queryset = any_number_value.objects.all()
    serializer_class = any_number_valueSerializer
