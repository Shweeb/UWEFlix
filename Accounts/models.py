from django.db import models
import uuid

# Stores information about individually registered users and their account details
class User(models.Model):
    # Identifiers
    username = models.CharField(max_length=200)
    password = models.TextField()

    # Foreign Key

    # Personal Info
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dateOfBirth = models.DateField()

    def __str__(self):
        return f"{self.username} ({self.firstName} {self.lastName})"

# Used to store information about clubs
class Club(models.Model):
    # Identifiers
    clubName = models.CharField(max_length=200)
    MemberCount = models.IntegerField(default=1)

    # Location Details
    streetNo = models.TextField()
    street = models.TextField()
    city = models.TextField()
    postcode = models.TextField()

    # Contact Details
    landlineNo = models.TextField()
    mobileNo = models.TextField()
    email = models.TextField()

    def __str__(self):
        return self.clubName

# Stores the account details for the club representitive
class Representitive(models.Model):
    # Identifiers
    password = models.CharField(max_length=200)

    # Representitive Info
    clubID = models.ForeignKey(Club, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE) # The rep must have an existing acc

    # # Personal Info
    # firstName = models.CharField(max_length=200)
    # lastName = models.CharField(max_length=200)
    # DateOfBirth = models.DateField()

    def __str__(self):
        return f"{self.clubID.clubName} Representitive"

# Placeholders for potential employee and manager accounts
class Employee(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    accessLevel = models.IntegerField(default=2) # The lower the number, the higher the access privilages

    def canAccess(self, desiredAccess):
        return self.accessLevel <= desiredAccess

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Manager(models.Model):
    # Some fields for manager identification
    title = models.CharField(max_length=200) # E.G. cinema manager, accounts manager, admin

    # Cinema manager and Accounts manager will have club details access
    pass

    def __str__(self):
        return self.title