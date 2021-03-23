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

#User Form - Have not incorporated in views yet, wanted to have it ready
class UserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()


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

    

    

    

