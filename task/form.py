from django import forms

from accounts.models import CustomUser
from customer.models import Customer
from task.models import Task, RequestChangeTask, TeamTask


class TaskCreateForm(forms.ModelForm):
    title = forms.CharField()
    id_customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    description = forms.Textarea(attrs={'placeholder': 'Describe this task with more detail'})
    consumed_time = forms.DecimalField(
        max_digits=4, decimal_places=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Only one decimal place allowed'})
    )
    rate = forms.DecimalField(
        max_digits=5, decimal_places=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Only one decimal place allowed'}))

    class Meta:
        model = Task
        fields = ['title', 'id_customer', 'description', 'consumed_time', 'rate']
        labels = {
            'title': 'Type Title for your Task: ',
            'id_customer': 'Pick customer: ',
            'description': 'Description: ',
            'consumed_time': 'Time spent working(H): ',
            'rate': 'Hourly rate: '
        }


class EmployeeRequestChangeTask(forms.ModelForm):
    title = forms.CharField()
    description = forms.Textarea(attrs={'placeholder': 'Describe this task with more detail'})
    consumed_time = forms.DecimalField(
        max_digits=4, decimal_places=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Only one decimal place allowed'})
    )
    rate = forms.DecimalField(
        max_digits=5, decimal_places=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Only one decimal place allowed'}))
    is_active = forms.RadioSelect()
    description_of_change = forms.Textarea(attrs={'placeholder': 'What changes and why?'})

    class Meta:
        model = RequestChangeTask
        fields = ['description_of_change', 'consumed_time', 'rate', 'is_active', 'title', 'description']
        labels = {
            'title': 'Edit title: ',
            'description': 'Edit description: ',
            'consumed_time': 'Add(or edit) time spent working(H): ',
            'rate': 'Edit hourly rate: ',
            'is_active': 'Is still active?',
            'description_of_change': 'Describe yours changes: '
        }


class AddUserToTeam(forms.ModelForm):
    class Meta:
        model = TeamTask
        fields = ['user_id']
