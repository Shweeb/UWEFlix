from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Index for the accounts management subsection
def index(request):
    userList = User.objects.all()

    context = {
        'userList': userList,
    }

    return render(request, 'accounts/index.html', context)

# def userDetails(request, userID, firstName, lastName):
#     return HttpResponse(f"The User ID for {firstName, lastName} is {userID}")

def manageUser(request, userID):
    user = User.objects.get(pk=userID)

    context = {
        'user': user,
    }

    return render(request, 'accounts/manageUser.html', context)

def allUsers(request):
    response = ""
    for i in User.objects.all():
        response += str(i) + ", "

    return HttpResponse(f"All the users are<br>{response}")

def updateUser(request, userID):
    # TODO Take the inputs and update the database with them
    print("THIS IS A TEST"+ request.POST["fname"])

    return HttpResponse("Success")