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
a = False
while not a:
    msg = input('Digite a mensagem a criptografar: ')
    a = validaMsg(msg)
encryptedText = encryptMessage(user, senha, msg)
saveNewLine(encryptedText)