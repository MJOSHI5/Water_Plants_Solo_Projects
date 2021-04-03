from django import forms

WATER_AMOUNT = [
    ('----', '----'),
    ('1 Cup', '2 Cups'),
    ('3 Cups', 'Soak'),
]

ROOM = [
    ('----', '----'),
    ('Kitchen', 'Living Room'),
    ('Bed Room', 'Family Room'),
]

STATUS = [
    ('----', '----'),
    ('Not Started', 'Started'),
    ('In Progress', 'Done'),
]

#User Form - Have not incorporated in views/html yet
class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    #image = forms.ImageField()
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password')
    confirm_password = forms.CharField(label='Confirm Password')


#Plant Form
class PlantForm(forms.Form):
    plants = forms.CharField()
    day = forms.CharField() 
    time = forms.CharField() 
    quantity = forms.CharField(label = 'Water Amount', widget = forms.Select(choices = WATER_AMOUNT)) 
    room = forms.CharField(label ='Room', widget = forms.Select(choices = ROOM))
    status = forms.CharField(label ='Status', widget = forms.Select(choices = STATUS))
    start_date = forms.DateTimeField(label= 'Start Date', widget = forms.SelectDateWidget) 
    end_date = forms.DateTimeField(label = 'End Date', widget = forms.SelectDateWidget)
    image = forms.ImageField() 
    description = forms.CharField(widget=forms.Textarea)
    
    
    #def clean(self):
        #cleaned_data = super(PlantForm, self).clean()
        #return cleaned_data

    

    

    

