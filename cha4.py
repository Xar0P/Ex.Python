# Receba um endereço de e-mail, e faça um sistema que receba os dados do usuário.

email = input('Digite um endereço de e-mail: ')
email_raiz = email
email = email.split('@')

user_email = email[0]
email.pop(0)

email = email[0].split('.')
dom_email = email[0]
email.pop(0)

compl_email = '.'.join(email) 

print(f'Email recebido: {email_raiz}\nNome usuário: {user_email}\nDomínio/Provedor: {dom_email}\nDomínio superior/Extensão: {compl_email}')