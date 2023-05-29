from django import forms


class BioGenForm(forms.Form):
    professional_title = forms.CharField(label="Professional Title")
    personalized_fact = forms.CharField(label="Personalized Fact")
    background = forms.CharField(label="Background")
    current_role = forms.CharField(label="Current role")
    relevant_skills = forms.CharField(label="Relevant Skills or Talents")
