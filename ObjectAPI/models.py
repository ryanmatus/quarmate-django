from django.db import models

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=60)
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

    # def __str__(self):
    #     return self.name

class Guest(Person):
    guest_id = models.AutoField(primary_key=True)

class Housemate(Person):
    housemate_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=60)
    guests = models.ManyToManyField(Guest, blank=True)

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=60)

class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    housemate = models.OneToOneField(Housemate, on_delete=models.CASCADE,)
    rooms = models.ManyToManyField(Room)
    guests = models.ManyToManyField(Guest)

class Residence(models.Model):
    residence_id = models.AutoField(primary_key=True)
    residence_name = models.CharField(max_length=60)
    address = models.CharField(max_length=500)
    rooms = models.ManyToManyField(Room, blank=True)
    housemates = models.ManyToManyField(Housemate, blank=True)
    visits = models.ManyToManyField(Visit, blank=True)

Visit.residence = models.OneToOneField(Residence, on_delete=models.CASCADE,)
    




