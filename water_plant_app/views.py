from django.shortcuts import render, redirect
from .models import *
import bcrypt
#from time import gmtime, strftime
from django.contrib import messages
from .forms import *
from datetime import datetime

#path('create', views.create_account),
def create_account(request):
    return render(request, 'register.html')

#path('register', views.register),
def register(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/create')
        else:
            safe_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = safe_pw
            )
            request.session['user_id'] = user.id
            return redirect('/plants')

    messages.error(request, "You need to login or register")
    return redirect('/')

#path('', views.index),
def index(request):
    return render(request, 'login.html')

#path('login', views.login),
def login(request):
    if request.method=="POST":
        user = User.objects.filter(email = request.POST['email'])
        if len(user) > 0:
            user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/plants') 
    messages.error(request, "Email or password is incorrect!")
    return redirect('/')

#path('user/profile', views.profile),
def profile(request):
    if 'user_id' not in request.session:
        messages.error(request, "Need to be logged in to change users password!")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'user':user,
    }   
    return render(request, 'profile.html', context) 

#path('user/update/profile', views.update_profile),
def update_profile(request):
    if request.method == "POST":
        errors = User.objects.password_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                print(errors)
                return redirect('/user/profile')
            
        else:
            safe_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.get(id=request.session['user_id'])
            user.password = safe_pw
            user.save()
        return redirect('/plants')
    
#path('plants', views.plants),
def plants(request):
    if 'user_id' not in request.session:
        messages.error(request, "Need to register or login buddy!")
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])
    plants = Plant.objects.all()

    context = {
        'user':user,
        'all_plants':plants,
    }

    return render(request, 'plants.html', context)


#path('plants/add', views.add_plants),
def add_plants(request):
    if 'user_id' not in request.session:
        messages.error(request, "Need to register or login buddy!")
        return redirect('/')
    context = {}
    if request.method == "POST":
        plant = PlantForm(data=request.POST, files=request.FILES)
        if plant.is_valid(): 
            img = plant.cleaned_data.get('image')
            plants = plant.cleaned_data.get("plants")
            day = plant.cleaned_data.get("day")
            time = plant.cleaned_data.get("time")
            quantity = plant.cleaned_data.get("quantity")
            room = plant.cleaned_data.get("room")
            start_date = plant.cleaned_data.get("start_date")
            end_date = plant.cleaned_data.get("end_date")
            description = plant.cleaned_data.get("description")
            user = User.objects.get(id=request.session['user_id'])
            status = plant.cleaned_data.get("status")
            obj = Plant.objects.create(
                img=img,
                owner=user,
                finished=status,
                plants=plants,
                day=day,
                time=time,
                quantity=quantity,
                room=room,
                start_date=start_date,
                end_date=end_date,
                description=description,
                
            )
            messages.success(request, 'Plant Added Successfully! You can continue uploading more plants or go all plants table')
        return redirect('/plants/add')
    else:
        plant = PlantForm() 
        user = User.objects.get(id=request.session['user_id'])
    context = {
        'plant_form':plant,
        'user':user,
    }
    return render(request, 'add-plant.html', context)

#path('plant/edit/<int:plants_id>', views.edit),
def edit(request, plants_id):
    if 'user_id' not in request.session:
        messages.error(request, "Need to register or login buddy!")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    plant = Plant.objects.get(id = plants_id)
    context = {
        'user':user,
        'plant':plant,
    }
    return render(request, 'edit.html', context)

#path('plants/edit/form/<int:plant_id>', views.edit_form),
def edit_form(request, plant_id):
    if request.method == "POST":
        errors = Plant.objects.plant_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/plant/edit/{plant_id}')
        else:
            to_edit = Plant.objects.get(id=plant_id)
            to_edit.plants = request.POST['plant']
            to_edit.day = request.POST['day']
            to_edit.time = request.POST['time']
            to_edit.quantity = request.POST['water']
            to_edit.start_date = request.POST['date']
            to_edit.end_date = request.POST['date']
            to_edit.description = request.POST['desc']
            to_edit.room = request.POST['room']
            to_edit.finished = request.POST['watered']
            to_edit.save()
    return redirect('/plants')

#path('plant/like/plant/<int:plant_id>', views.like),
def like(request, plant_id):
    liked_plant = Plant.objects.get(id=plant_id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_plant.user_likes.add(user_liking)
    return redirect(f'/plant/{plant_id}')
    

#path('plant/un_like/plant/<int:plant_id>', views.un_like),
def un_like(request, plant_id):
    liked_plant = Plant.objects.get(id=plant_id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_plant.user_likes.remove(user_liking)
    return redirect(f'/plant/{plant_id}')

#path('plant/<int:plants_id>/favorite', views.favorite),
def favorite(request, plants_id):
    user = User.objects.get(id=request.session['user_id'])
    plant = Plant.objects.get(id=plants_id)
    user.user_favorite.add(plant)
    print(f'I added {plant.id} to my favorites')
    return redirect('/plants')

#path('plant/<int:plants_id>/un-favorite', views.un_favorite),
def un_favorite(request, plants_id):
    user = User.objects.get(id=request.session['user_id'])
    plant = Plant.objects.get(id=plants_id)
    user.user_favorite.remove(plant)
    print(f'I removed {plant.id} plant from my favorites')
    return redirect('/plants')


#path('plant/<int:favorites_id>/un-fav', views.un_fav),
def un_fav(request, favorites_id):
    user = User.objects.get(id=request.session['user_id'])
    plant = Plant.objects.get(id=favorites_id)
    user.user_favorite.remove(plant)
    print(f'I removed {plant.id} plant from my favorites')
    return redirect('/user/profile')

#path('plant/delete/<int:plants_id>', views.delete),
def delete(request, plants_id):
    if 'user_id' not in request.session:
        messages.error(request, "Need to register or login buddy!")
        return redirect('/')
    to_delete = Plant.objects.get(id=plants_id)
    to_delete.delete()
    return redirect('/plants')

#path('plant/<int:plants_id>', views.single_plant),
def single_plant(request, plants_id):
    if 'user_id' not in request.session:
        messages.error(request, "Need to register or login buddy!")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    plant = Plant.objects.get(id=plants_id)
    context = {
        'user':user,
        'plant':plant
    } 
    return render(request, 'single_plant.html', context)
    
#path('logout', views.logout),
def logout(request):
    request.session.flush()
    return redirect('/')