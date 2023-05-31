from django import forms


class BioGenForm(forms.Form):
    professional_experience = forms.CharField(label="Professional Experience")
    personalized_fact = forms.CharField(label="Personalized Fact")
    skills = forms.CharField(label="Skills")
