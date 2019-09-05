from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        error_messages = {
            'full_name': {'required': "Digite o seu nome completo",},
            'email': {'required': "Digite o seu e-mail",},
            'phone': {'required': "Digite o seu número de telefone",},
            'linkedin_link': {'required': "Digite a URL do seu perfil do Linkedin",},
            'github_link': {'required': "Digite a URL da sua conta do GitHub",},
            'eng_level': {'required': "Selecione o seu nível de inglês",},
            'salary': {'required': "Digite a sua pretensão salarial",},
            'curriculum': {'required': "Selecione o seu currículo",},
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'José Maria'}),
            'email': forms.TextInput(attrs={'placeholder': 'josemaria@email.com'}),
            'pres_letter': forms.Textarea(attrs={'placeholder': 'Eu sou uma pessoa...'}),
            'linkedin_link': forms.Textarea(attrs={'placeholder': 'https://www.linkedin.com/x'}),
            'github_link': forms.Textarea(attrs={'placeholder': 'https://www.github.com/x'}),
            'salary': forms.Textarea(attrs={'placeholder': '0000,00'}),
        }
