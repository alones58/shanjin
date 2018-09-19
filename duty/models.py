# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DutyUser(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=30, null=True)
    dept = models.CharField(max_length=30)
    mphone = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Dept(models.Model):
    dept_name = models.CharField(unique=True, max_length=30, null=True)
    dept_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.dept_name