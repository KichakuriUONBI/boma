from django.core.exceptions import ValidationError
from django.db import models


def validate_reference(value):
    if not value.isalnum():
        raise ValidationError("Reference must be alphanumeric.")


def validate_brand(value):
    if not (7400000001 <= value <= 7490000999): # Check if the brand number is 10 digits
        raise ValidationError("Reference must be exactly 10 digits.")


class Income(models.Model):
    INCOME_CATEGORIES = [
        ('SALE', 'Sale of Cattle'),
        ('CONTRIB', 'Contributions'),
    ]
    reference=models.CharField(max_length=10, unique=True, validators=[validate_reference])
    date = models.DateField()
    payer = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=INCOME_CATEGORIES)


class Expense(models.Model):
    EXPENSE_CATEGORIES = [
        ('SALARY', 'Herdsmen Salaries'),
        ('FOOD', 'Food Rations'),
        ('FUEL', 'Motorcycle Fuel'),
        ('REPAIR', 'Repairs'),
        ('PURCHASE', 'Cattle Purchases'),
        ('VET', 'Veterinary Services'),
        ('DRUGS', 'Veterinary Drugs'),
        ('LEASE', 'Lease Rentals'),
    ]
    reference = models.CharField(max_length=10, unique=True, validators=[validate_reference])
    date = models.DateField()
    payee = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=EXPENSE_CATEGORIES)

class Cattle(models.Model):
    brand=models.IntegerField(max_length=10,unique=True,validators=[validate_brand])
    sex = models.CharField(max_length=10)
    breed = models.CharField(max_length=100)
    sire = models.CharField(max_length=100, blank=True, null=True)
    mother = models.CharField(max_length=100, blank=True, null=True)
    date_bought = models.DateField()
    date_of_birth = models.DateField()
    date_sold_or_lost = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, default='Alive')

class CattleEvent(models.Model):
    EVENT_TYPES = [
        ('PREDATION', 'Lost to predation'),
        ('VACCINATION', 'Vaccinated'),
        ('INJURY', 'Injured'),
        ('ILLNESS DEATH', 'Died of illness'),
        ('SOLD', 'Was sold'),
        ('TREATED', 'Received treatment'),
        ('EATEN', 'Eaten by family and or friends'),
        ('BOUGHT', 'Was bought'),
    ]
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100, choices=[EVENT_TYPES])
    date = models.DateField()
    details = models.TextField()