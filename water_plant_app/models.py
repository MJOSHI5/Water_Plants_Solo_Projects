from django.db import models
import re


class UserManager(models.Manager):
    def user_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['first_name']) < 5:
            errors['last_name'] = "First and last name should be at least 5 characters."
        if len(postData['email']) < 8:
            errors['email'] = "Email needs to be longer."
        if len(postData['password']) <8:
            errors['password'] = "Password must be at least be atleast 8 characters."
        if postData['password'] != postData['confirm_pw']:
            errors['password_conf'] = "Password and confirm password need to match."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid Email address.")
        check_email = self.filter(email=postData['email'])
        if check_email:
            errors['email'] = "Email already exsists, please use a diffrent one."
        return errors
    
    def password_validator(self, postData):
        errors = {}
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if len(postData['password']or postData['confirm_pw']) == 0:
            errors['password'] = 'Fill out password information'
        elif postData['password'] != postData['confirm_pw']:
            errors['password'] = 'Password and Confirm Password must match'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    img = models.ImageField(upload_to = "img/", null = True, blank = True)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
    

class PlantManager(models.Manager):
    def plant_validator(self, postData):
        errors = {}

        DATE_REGEX = re.compile(r'^(19|20)\d\d[- / .](0[1-9]|1[012])[- / .](0[1-9]|[12][0-9]|3[01])$')
        
        if len(postData['plant']) == 0:
            errors["plant"] = "Plant name is required !"


        if not DATE_REGEX.match(postData['date']):    # test whether a field matches the pattern            
            errors['date'] = "Fill out the date inputs !"
        
        return errors

    

class Plant(models.Model):
    plants = models.CharField(max_length = 255)
    day = models.CharField(max_length = 140)
    time = models.CharField(max_length = 140)
    quantity = models.CharField(max_length = 14)
    start_date = models.DateTimeField(null = True)
    end_date = models.DateTimeField(null = True)
    description = models.TextField()
    finished = models.CharField(max_length = 5, null = True)
    user_likes = models.ManyToManyField(User, related_name='liked_plant')  # ManyUsersLikeManyPlants and ManyPlantsAreLikedbyManyUsers
    favorites = models.ManyToManyField(User, related_name = 'user_favorite')
    owner = models.ForeignKey(User, related_name = 'plant_owner', on_delete = models.CASCADE)
    img = models.ImageField(upload_to = "img/", null = True, blank = True)
    room = models.CharField(max_length = 140, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = PlantManager()





    
