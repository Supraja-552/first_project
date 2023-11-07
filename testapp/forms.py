from django.forms import ModelForm
from testapp.models import Employee
class Customerform(ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
