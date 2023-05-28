from django import forms


class BioGenForm(forms.Form):
    professional_title = forms.CharField(label="Professional Title")
    years_of_experience = forms.IntegerField(label="Years of Experience")
    professional_values = forms.CharField(label="Professional Values")
    problem_solving = forms.CharField(label="Approach to Problem Solving")
    emotional_intelligence = forms.CharField(label="Emotional Intelligence")
    personal_growth_mindset = forms.CharField(label="Personal Growth Mindset")
    teamwork_collaboration = forms.CharField(label="Teamwork and Collaboration")
    communication_skills = forms.CharField(label="Communication Skills")
    initiative_proactivity = forms.CharField(label="Initiative and Proactivity")
    adaptability_resilience = forms.CharField(label="Adaptability and Resilience")
    value_creation = forms.CharField(label="Value Creation")
    passion_motivation = forms.CharField(label="Passion and Motivation")
