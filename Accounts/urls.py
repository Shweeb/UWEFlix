from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    # Accounts Index
    path('', views.index, name='index'),
    # User Details
    path('<int:userID>/', views.manageUser, name="ManageUser"),
    # All Users
    path('allUsers', views.allUsers, name='allUsers'),
    # Update SQL fields
    path('update/<int:userID>', views.updateUser, name='updateUser')
]

