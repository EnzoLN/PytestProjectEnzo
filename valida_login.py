import re
def validaUser(user):
    if user[0].isupper():
        if not re.search('[^a-zA-Z0-9\s]', user):
            if not (' ' in user):
                if len(user) <= 30:
                    return True
                else:
                    print('O usuário não deve conter mais que 30 caracteres. ')
                    return False
            else:
                print('O usuário não deve conter espaços. ')
                return False
        else: 
            print('O usuário não deve conter caracteres especiais. ')
            return False
    else:
        print('A primeira letra deve ser maiúscula. ')
        return False

def validaSenha(senha):
    if len(senha) >= 10:
        if re.search('[^a-zA-Z0-9\s]', senha):
            if re.search('\d', senha):
                if re.search('[A-Z]', senha):
                    if re.search('[a-z]', senha):
                        return True
                    else:
                        print('A senha deve conter uma letra minúscula. ')
                    return False
                else:
                    print('A senha deve conter uma letra maiúscula. ')
                    return False
            else:
                print('A senha deve conter um número. ')
                return False
        else: 
            print('A senha deve conter um caracter especial. ')
            return False
    else: 
        print('A senha deve conter mais que 10 caracteres. ')
        return False
    
def validaMsg(msg):
    if len(msg) <=70:
        return True
    else:
        print('A mensagem não pode conter mais que 70 caracteres. ')
        return False