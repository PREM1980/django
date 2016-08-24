# from __future__ import unicode_literals

from django.db import models
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.postgres.fields import ArrayField


class PositionField(models.Field):
    def __init__(self, *args, **kwargs):
        super(PositionField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        # Type is defined as char(25)
        return 'char(25)'

    def to_python(self, value):     
        #The input value is received and split into list, For example:- mapspot = 10,20  will be converted to [10,20]
        result = value.split(',')        
        return result        

    def get_db_prep_value(self, value, connection, prepared=False):            
        # The list created above is converted into a string before saving into the database.
        # When the unique check index is executed the string is used rather than the list value as expected.
        result = ','.join([str(each) for each in value])        
        return result    

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value        
        return value        


class Map(models.Model):
    name = models.CharField(max_length=128)


class MapSpot(models.Model):
    map = models.ForeignKey('polls.Map')    
    position = PositionField()

    class Meta:
        unique_together = (('map', 'position'))







