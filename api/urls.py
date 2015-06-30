from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from api.views import *

router = routers.DefaultRouter(trailing_slash=False)


router.register(r'product', ProductViewSet)
router.register(
    r'product_relationship', Product_relationshipViewSet)
router.register(r'product_version', Product_versionViewSet)
router.register(
    r'product_version_relationship', Product_version_relationshipViewSet)
router.register(r'product_category', Product_categoryViewSet)
router.register(
    r'product_category_assignment', Product_category_assignmentViewSet)
router.register(
    r'product_category_hierarchy', Product_category_hierarchyViewSet)
router.register(r'product_view_definition', Product_view_definitionViewSet)
router.register(r'view_definition_context', View_definition_contextViewSet)
router.register(
    r'product_property_assignment', Product_property_assignmentViewSet)
router.register(
    r'view_definition_relationship', View_definition_relationshipViewSet)
router.register(r'view_definition_usage', View_definition_usageViewSet)
router.register(
    r'assembly_component_relationship', Assembly_component_relationshipViewSet)
router.register(r'next_assembly_usage', Next_assembly_usageViewSet)
router.register(r'component_upper_level_identification',
                Component_upper_level_identificationViewSet)
router.register(r'promissory_usage', Promissory_usageViewSet)
router.register(r'value_with_unit', Value_with_unitViewSet)
router.register(r'unit', UnitViewSet)
router.register(r'measure_value', Measure_valueViewSet)
router.register(r'any_number_value', any_number_valueViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
