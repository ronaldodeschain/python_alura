from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(label="Nome do Login",required=True,
    max_length=100,
    widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex: Erasmo Carlos"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex:Erasmo Carlos"
            }           
        )
    )
    email=forms.EmailField(
        label="Email de Cadastro",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex: erasmocarlos@xpto.com"
            }
        )
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('Usuário não pode conter espaços')
            else:
                return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não são iguais")
            else:
                return senha_2

