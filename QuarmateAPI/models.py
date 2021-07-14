from django.db import models

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    test = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)

    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'
    PENDING = 'Pending'
    NA = 'NA'
    STATUS_CHOICES = [
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
        (PENDING, 'Pending'),
        (NA, 'NA'),
    ]

    status = models.TextField(choices=STATUS_CHOICES, default = 'NA')

    def __str__(self):
        return self.name

class Guest(Person):
    guest_id = models.AutoField(primary_key=True)

class Housemate(Person):
    housemate_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=60)
    guests = models.ManyToManyField(Guest)
