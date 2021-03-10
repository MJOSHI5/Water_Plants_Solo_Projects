from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #<form action="/register" method="POST">
    path('register', views.register),
    #<form action="/login" method="POST">
    path('login', views.login),
    #<a class="no-account" href="/create">Create an account</a>
    path('create', views.create_account),
    #Plants list html page
    path('plants', views.plants),
    #<a class="block" href="/plant/like/plant/{{plant.id}}">Like</a>
    path('plant/like/plant/<int:plant_id>', views.like),
    #<a href="/plant/{{plants.id}}/favorite">Favorite</a>
    path('plant/<int:plants_id>/favorite', views.favorite),
    # <a href="/plant/{{plants.id}}/un-favorite"><img class="fav" src="{% static 'img/heart-solid.svg' %}"></a>
    path('plant/<int:plants_id>/un-favorite', views.un_favorite),
    #<a href="/plant/{{favorites.id}}/un-fav"><img class="fav" src="{% static 'img/heart-solid.svg' %}"></a>
    path('plant/<int:favorites_id>/un-fav', views.un_fav),
    #<a href="/user/profile">My Profile</a>
    path('user/profile', views.profile),
    path('user/update/profile', views.update_profile),
    #<a class="block" href="/plant/un_like/plant/{{plant.id}}">Un_Like</a>
    path('plant/un_like/plant/<int:plant_id>', views.un_like),
    #<form action="/plants/add" method="post">
    path('plants/add', views.add_plants),
    #<a href="/plant/edit/{{plants.id}}">Edit</a>
    path('plant/edit/<int:plants_id>', views.edit),
    #<form action="/plants/edit/form/{{plant.id}}" method="POST">
    path('plants/edit/form/<int:plant_id>', views.edit_form),
    #<a href="/plant/{{plants.id}}">View</a>
    path('plant/<int:plants_id>', views.single_plant),
    #<a href="/plant/delete/{{plants.id}}">Delete</a>
    path('plant/delete/<int:plants_id>', views.delete),
    #<a href="/logout">Logout</a>
    path('logout', views.logout),
]
