from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.template.response import TemplateResponse
from django.contrib.admin import helpers
from .models import (User)


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
             ('User Profile', {'fields': (
                 ('name'),
                 ('matricula'),
                 ('gender'),
                 ('birthday'),
                 ('cpf'),
                 ('endereco')
                )}),
    ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'name', 'is_superuser', 'birthday', 'cpf')
    search_fields = ['name']
