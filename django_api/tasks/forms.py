from django import forms
from .models import List

# form will automatically generate fields corresponding to the List model fields, and you’ll be able to use ListForm to create, update, and validate List model instances.
# ModelForm is a helper class in Django that allows you to create a form

class ListForm(forms.ModelForm):
    # inner class within ListForm to provide additional information or configuration
    class Meta:
        model = List
        # This list specifies which fields from the List model should be included in the form. Then form handles the validation and processing needed to save that data to the database.
        fields = ['task', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),  # Using calendar style date input
        }