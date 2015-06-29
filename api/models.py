from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Product_version_relationship(models.Model):
    relation_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class Product_version(models.Model):
    description = models.TextField(blank=True, null=True)
    product = models.OneToOneField('Product', blank=True, null=True)


class Product_version_relationship(models.Model):
    description = models.TextField(blank=True, null=True)


class Product_category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Product_category_assignment(models.Model):
    pass


class Product_category_hierarchy(models.Model):
    pass


class Product_view_definition(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    additionnal_characterization = models.TextField(blank=True, null=True)


class View_definition_context(models.Model):
    application_domain = models.CharField(max_length=100)
    life_cycle_stage = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class Product_property_assignment(models.Model):
    pass


class View_definition_relationship(models.Model):
    relation_type = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class View_definition_usage(View_definition_relationship):
    pass


class Assembly_component_relationship(View_definition_usage):
    location_indicator = models.TextField(blank=True, null=True)


class Next_assembly_usage(Assembly_component_relationship):
    pass


class Component_upper_level_identification(Assembly_component_relationship):
    pass


class Promissory_usage(Assembly_component_relationship):
    pass


class Value_with_unit(models.Model):
    pass


class Unit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    si_unit = models.CharField(max_length=100, blank=True, null=True)


class Measure_value(models.Model):
    pass


class any_number_value(Measure_value):
    any_number_value = models.IntegerField()
