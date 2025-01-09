from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from newspapers.models import Newspaper, Redactor


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperTitleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title"}
        )
    )


class TopicNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class RedactorUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
            "email"
        )

    def clean_years_of_experience(self) -> int:
        return int(
            validate_years_of_experience(
                self.cleaned_data["years_of_experience"]
            )
        )


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name"
        )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ("username", "first_name", "last_name", "years_of_experience", "email",)

    def clean_years_of_experience(self) -> int:
        return int(
            validate_years_of_experience(
                self.cleaned_data["years_of_experience"]
            )
        )


def validate_years_of_experience(
    years_of_experience: int | float
) -> int | float:
    if not isinstance(years_of_experience, (int, float)):
        raise ValidationError("Years of experience must be a number.")
    if not (years_of_experience >= 0):
        raise ValidationError(
            "Years of experience must be a non-negative number."
        )
    return years_of_experience
