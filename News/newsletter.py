from django import forms


class RegisterNewsletter(forms.Form):
    nome = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class':'form-control',
                                                             'placeholder':'Qual é seu nome ?'}))
    emailnews = forms.CharField(max_length=100,
                               widget=forms.EmailInput(attrs={'class':'form-control',
                                                             'placeholder':'Digite seu melhor E-Mail'}))
