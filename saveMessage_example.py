from cryptographyFramework import *

initializeWrite()
user = "Enzo"
password = "3307"
encryptedText = encryptMessage(user, password, "Minha mensagem secreta!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Minha segunda mensagem secreta!")
saveNewLine(encryptedText)

