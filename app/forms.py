from django import forms


class BioGenForm(forms.Form):
    professional_title = forms.CharField(label="Professional Title")
    personalized_fact = forms.CharField(label="Personalized Fact")
    value_creation = forms.CharField(label="Value Creation")
    passion_motivation = forms.CharField(label="Passion and Motivation")
