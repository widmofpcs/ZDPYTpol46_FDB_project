from django.forms import inlineformset_factory
from .models import CustomUser, CustomUserProfile
from .forms import CustomUserProfileChangeForm, CustomUserProfileCreationForm

CustomUserProfileFormSet = inlineformset_factory(CustomUser, CustomUserProfile, form=CustomUserProfileCreationForm , extra=1, can_delete = False)