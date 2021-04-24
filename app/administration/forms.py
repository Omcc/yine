from django.forms import ModelForm, ModelChoiceField
from administration.models import City
from administration.models import Country

class AddressAdminForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(AddressAdminForm,self).__init__(*args,**kwargs)

        if self.instance:
            country_id = self.instance.country_id
            cities = City.objects.filter(country_id=country_id)
            self.fields['city'] = ModelChoiceField(queryset=cities)
