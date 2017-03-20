from __future__ import unicode_literals

from django.db import models
import datetime
from django.core.validators import MaxValueValidator,MinValueValidator

class User(models.Model):
	u_no = models.IntegerField(unique = True,blank = False)
	name = models.CharField(max_length=200, blank = False)
	DOB = models.DateField(blank = False)
	age = models.IntegerField(blank = False)
	address = models.CharField(max_length = 200, blank = False)
	mob_no = models.BigIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(7000000000)],unique = True)
	email = models.CharField(max_length = 20 ,unique= True)
