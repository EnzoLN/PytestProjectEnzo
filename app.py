from cryptographyFramework import *
from valida_login import *
a = False
while not a:
    user = input('Digite seu usuário: ')
    a = validaUser(user)
a = False
while not a:
    senha = input('Digite sua senha: ')
    a = validaSenha(senha)