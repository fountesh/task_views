from django import forms

class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'All Statuses'),
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    PRIORITY_CHOICES = [
        ('', 'All Priorities'),
        ('high', 'High'),
        ('mid', 'Medium'),
        ('low', 'Low'),
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