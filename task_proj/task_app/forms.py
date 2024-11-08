# forms.py
from django import forms

class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'All Statuses'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ]
    
    PRIORITY_CHOICES = [
        ('', 'All Priorities'),
        ('low', 'Low'),
        ('mid', 'Mid'),
        ('high', 'High')
    ]
    
    status = forms.ChoiceField(
        choices=STATUS_CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )