from django.db import models

# Create your models here.

class warehouse(models.Model):
    crop_type = {
        #grains
        "Wheat": "Wheat",
        "Rice" : "Rice",
        "Corn": "Corn",
        "Barely":"Barely",
        "Oats":"Oats",
        #fruits
        "Apple":"Apple",
        "Oranges":"Oranges",
        "Bananas":"Bananas",
        "Grapes":"Grapes",
        "Strawberries":"Strawberries",
        #vegtables
        "Tomatoes":"Tomatoes",
        "Carrots":"Carrots",
        "Okra":"Okra",
        "Onions":"Onions"
    }  
    storage_c = {
        "Standard":"Plan",
        "Premium" :"Plan",
        "Climate":"Climate",
    }
    location = {
        "A1":"A1",
        "A2":"A2",
        "A3":"A3",
        "B1":"B1",
        "B2":"B2",
        "B3":"B3",
        "C1":"C1",
        "C2":"C2",
        "C3":"C3",
    }
    
    email = models.EmailField()  
    date = models.DateField(auto_now=False, auto_now_add=False)
    crop = models.CharField(choices=crop_type, max_length=255, default="Wheat")
    quantity = models.IntegerField(default=1)
    storage_condition = models.CharField(choices=storage_c,max_length=255, default="climate" )
    storage_location = models.CharField(choices=location,max_length=255, default="A1" )
    batch = models.TextField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return self.email+"_"+self.crop