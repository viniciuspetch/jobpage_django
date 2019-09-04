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
        }
