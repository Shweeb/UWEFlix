from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django import forms
import uuid, re, datetime
from datetime import date, timedelta

# ----------------- Validators -----------------

# Check validity of mobile number
def isMobileNumber(value):
    # This is mainly for UK numbers just to simplify things but later on i might want to make this work for more numbers
    mobileRegex = re.compile(r'^\d{11}$')

    if not mobileRegex.match(value):
        raise forms.ValidationError("Invalid Mobile Number (Make sure it's a UK number)")

# Check validity of landline number
def isLandlineNumber(value):
    # Once again this is mainly for UK numbers
    landlineRegex = re.compile(r'^\d{5}\d{6}$')

    if not landlineRegex.match(value):
        raise forms.ValidationError("Invalid Landline Number (Make sure it's a UK number)")

# Algorithm to check the validation of a card number
def luhn_check(card_number):
    """Validate card number using the Luhn algorithm"""
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

# Checks the validity of card number
def validateCardNumber(value):
    cardNumber = re.sub("[^0-9]", "", value)
    if not re.match(r"^[0-9]{16}$", cardNumber):
        raise forms.ValidationError("Invalid card number")
    if not luhn_check(cardNumber):
        raise forms.ValidationError("Invalid card number")

# Checks the validity of the expiration date
def validateExpirationDate(value):
    if not re.match(r"^(0[1-9]|1[0-2])\/[0-9]{2}$", value):
        raise forms.ValidationError("Invalid expiration date (Must be MM/YY)")
    month, year = value.split("/")
    if int(year) < datetime.datetime.now().year % 100:
        raise forms.ValidationError("Invalid expiration date (Must be MM/YY)")
    if int(year) == datetime.datetime.now().year % 100 and int(month) < datetime.datetime.now().month:
        raise forms.ValidationError("Invalid expiration date (Must be MM/YY)")

# Checks the validity of cvv
def validate_cvv(value):
    if not re.match(r"^[0-9]{3,4}$", value):
        raise forms.ValidationError("Invalid CVV/CVC code")

# Checks the validity of card name
def validate_cardholder_name(value):
    if not value.strip():
        raise forms.ValidationError("Invalid cardholder name")

# ----------------- Managers -----------------

class MonthAgoManager(models.Manager):
    def get_queryset(self):
        today = date.today()
        monthAgo = today - timedelta(days=30)
        return super().get_queryset().filter(date__gte=monthAgo, date__lte=today)

# ----------------- Models -----------------
# Stores information about individually registered users and their account details
class User(models.Model):
    # Identifiers
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    # Foreign Key

    # Personal Info
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    dateOfBirth = models.DateField()

    # Payment Information
    cardNumber = models.CharField(max_length=16, validators=[validateCardNumber])
    expirationDate = models.CharField(max_length=5, validators=[validateExpirationDate])
    cvv = models.CharField(max_length=4, validators=[validate_cvv])
    cardHolderName = models.CharField(max_length=255, validators=[validate_cardholder_name])

    def encryptPassword(self, plainPassword):
        self.password = make_password(plainPassword)

    def checkPassword(self, plainPassword):
        if check_password(plainPassword):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.username} ({self.firstName} {self.lastName})"

class UserForm(forms.ModelForm):
    # Form for User model
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'dateOfBirth': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Enter a password',
                    'type': 'password'
                }
            )
        }

# Used to store information about clubs
class Club(models.Model):
    # Identifiers
    clubName = models.CharField(max_length=255)
    memberCount = models.IntegerField(default=1)
    discount = models.IntegerField(default=20)

    # Location Details
    streetNo = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)

    # Contact Details
    landlineNo = models.CharField(max_length=255, validators=[isLandlineNumber], null=True)
    mobileNo = models.CharField(max_length=20, validators=[isMobileNumber], null=True)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.clubName

class ClubForm(forms.ModelForm):
    # Form for Club model
    class Meta:
        model = Club
        fields = '__all__'

# Stores the account details for the club representitive
class Representitive(models.Model):
    # Identifiers
    password = models.CharField(max_length=255)

    # Representitive Info
    affiliatedClub = models.ForeignKey(Club, on_delete=models.CASCADE)
    studentRepresentitive = models.ForeignKey(User, on_delete=models.CASCADE) # The rep must have an existing acc

    # # Personal Info
    # firstName = models.CharField(max_length=255)
    # lastName = models.CharField(max_length=255)
    # DateOfBirth = models.DateField()

    def encryptPassword(self, plainPassword):
        self.password = make_password(plainPassword)

    def checkPassword(self, plainPassword):
        if check_password(plainPassword):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.affiliatedClub.clubName} Representitive"

class RepForm(forms.ModelForm):
    # Form for representitive
    class Meta:
        model = Representitive
        fields = '__all__'
        widgets = {
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Enter a password',
                    'type': 'password'
                }
            )
        }

# Placeholders for potential employee and manager accounts
class Employee(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    accessLevel = models.IntegerField(default=2) # The lower the number, the higher the access privilages

    def canAccess(self, desiredAccess):
        return self.accessLevel <= desiredAccess

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Manager(models.Model):
    # Some fields for manager identification
    title = models.CharField(max_length=255) # E.G. cinema manager, accounts manager, admin

    # Cinema manager and Accounts manager will have club details access
    pass

    def __str__(self):
        return self.title

# Stores Payments made by users
class UserPurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField() # Will only ever store purcahses made on the day therefore needs to filter between month old purchases and beyond
    objects = MonthAgoManager()

    def __str__(self):
        return f"{self.user.firstName} {self.user.lastName} spent ??{self.totalCost} on {self.quantity} tickets"

# Stores Payments made by Clubs
class ClubPurchaseHistory(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=10)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField() # Will only ever store purcahses made on the day therefore needs to filter between month old purchases and beyond
    objects = MonthAgoManager()

    def __str__(self):
        return f"{self.club.clubName} club spent ??{self.totalCost} on {self.quantity} tickets"