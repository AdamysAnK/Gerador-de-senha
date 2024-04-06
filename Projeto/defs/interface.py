def gerar_senha():
    import os as sistema
    user=sistema.getlogin()
    import string
    from random import choice
    global senha1
    print(f'Olá, {user}. Seja Bem-Vindo')
    print('*'*30)
    print(f'Gerado de senha'.center(30))
    print('*'*30)
    escolha_senha=int(input('''Escolha como vai ser a senha:
1.  \033[31mletras e numeros\033[m
2.  \033[32mnumeros e caractereres\033[m
3.  \033[33mcaracteres e letras\033[m
4.  \033[34mFull(caracteres, letras e numeros)\033[m
'''))
    # condições
    while True:
        tamanho=int(input('Qual o tamanho da senha?: 4, 6, 8'))
        if tamanho not in (4,6,8):
            print('\033[31mTamanho inválido!!\033[m')
        else:
            break
    # lista
    caracteres=list()
    # letras e numero
    if escolha_senha==1:
        caracteres+=string.ascii_letters+string.digits
    #numeros e caracteres
    if escolha_senha==2:
        caracteres+=string.digits
    # caracteres e letras
    if escolha_senha==3:
        caracteres+=string.punctuation+string.digits
    # Full
    if escolha_senha==4:
        caracteres+=string.punctuation+string.digits+string.ascii_letters
    
    senha1=''.join(choice(caracteres) for _ in range(tamanho))
    return senha1



def criar_pasta(site,senha):
    import os as sistema
    user=sistema.getlogin()
    if sistema.path.exists (f'C:/Users/{user}/OneDrive/Área de Trabalho/Senhas')==False:
        dir=f'C:/Users/{user}/OneDrive/Área de Trabalho/Senhas'
        sistema.mkdir(dir)
    if sistema.path.exists (f'C:/Users/{user}/OneDrive/Área de Trabalho/Senhas/{site}')==False:
            dir2=f'C:/Users/{user}/OneDrive/Área de Trabalho/Senhas/{site}'
            sistema.mkdir(dir2)
            
            open(f'{dir2}/{site}.txt','x')
            nome_do_arquivo=(f'C:/Users/{user}/OneDrive/Área de Trabalho/Senhas/{site}/{site}.txt')
            arquivo = open(nome_do_arquivo, 'r')
            texto = arquivo.readlines()
            texto.append(f'senha: {senha}\nBy: AnarK')
            arquivo = open(nome_do_arquivo, 'w')
            arquivo.writelines(texto)
            arquivo.close()
    
def interface():
    
    site=input('Qual app você vai usar a senha?: ')
    print(gerar_senha())
    criar_pasta(site,senha1)