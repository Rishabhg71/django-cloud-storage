from django import forms 


class uploadform(forms.Form):  
    file_to_upload = forms.FileField()  