from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    # Accounts Index
    path('', views.index, name='index'),

    # User Creation Page
    path('user/create/', views.createUser, name="createUser"),

    # User Manage page
    path('user/<int:userID>/', views.manageUser, name="manageUser"),

    # Club Creation Page
    path('club/create/', views.createClub, name="createClub"),

    # Club Manage page
    path('club/<int:clubID>', views.manageClub, name="manageClub"),

    # Assign a rep for a club
    path('rep/create', views.createRep, name="createRep"),

    # Manage Rep page
    path('rep/<int:repID>', views.manageRep, name="manageRep"),

    # Select payment History page
    path('statement/', views.selectStatement, name="selectStatement"),

    # See selected payment history
    path('statement/user/<int:userID>/', views.seeUserStatement, name="seeUserStatement"), # For user statements
    path('statement/club/<int:clubID>/', views.seeClubStatment, name="seeClubStatment"), # For club statements

    # See and edit all account details
    path('all/<int:userID>', views.manageAccounts, name="manageAccounts"), # Unselected
    # path('all/<int:userID>', views.manageSelectedAccounts, name="manageSelectedAccounts"), # Selected
]

