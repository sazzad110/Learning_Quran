from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Review, Telawat


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rev_details']

class TelawatForm(ModelForm):
    class Meta:
        model = Telawat
        fields = ['surah','ayat','audio']
        exclude = ['host', 'arruracy']
