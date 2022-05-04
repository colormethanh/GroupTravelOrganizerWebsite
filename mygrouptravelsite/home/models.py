from datetime import datetime
from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.forms import ModelForm
from django import forms
import datetime
from django.core.exceptions import ValidationError

def date_validator(value):
    if value < datetime.date.today():
        raise ValidationError("Date cannot be in the past!")
    else:
        return value


class Trip(models.Model):
    name = models.CharField(max_length=200, 
                            validators=[MinLengthValidator(3, "Trip title must be longer than 3 characters")]
                            )
    key = models.CharField(max_length=10,
                            validators=[MinLengthValidator(3, "Trip key must be longer than 3 characters")],
                            null=True
                            )
    start_date = models.DateField(validators=[date_validator])
    end_date = models.DateField(validators=[date_validator])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Going', related_name='members_going')

    def __str__(self):
        return self.name
    
    def ismember(self, user_id):
        member_lst = [member.id for member in self.members.all()]
        if user_id in member_lst:
            return True
        else:
            return False

    

class Event(models.Model):
    name = models.CharField(max_length=200, 
                            validators=[MinLengthValidator(3, "Event title must be longer than 3 characters")]
                            )
    location= models.CharField(max_length=200, null=True)
    cost= models.DecimalField( max_digits=4 , decimal_places=2, default = 0)
    start_date = models.DateField(validators=[date_validator], null=True)
    end_date = models.DateField(validators=[date_validator], null=True)
    confirmed = models.BooleanField(default=False)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True) 
    

    def __str__(self):
        return self.name

class Going(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return '%s is a member of %s'%(self.user.username, self.trip.name)