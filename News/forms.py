from django import forms


class RegisterForms(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class':'form-control',
                                                             'placeholder':'Digite seu Usuário'}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={'class':'form-control',
                                                             'placeholder':'Digite sua Senha'}))
    email = forms.CharField(max_length=100,
                               widget=forms.EmailInput(attrs={'class':'form-control',
                                                             'placeholder':'Digite seu E-Mail'}))
    tel = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class':'form-control',
                                                             'placeholder':'Digite seu Telefone'}))
