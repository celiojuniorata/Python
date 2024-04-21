import os
import time

sintomas_apresentados = []
doencas_existentes = []

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        while True:

            print('Sistema de ajuda a diagnóstico da covid-19 (SAD COVID)')

            try:
                nome_paciente = input('Informe o seu nome: ')

                if nome_paciente != '':
                    nome_paciente_upper = nome_paciente.upper()
                else:
                    print('Nome vazio.')
                    time.sleep(1)
                    limpar()
                    continue
                
                idade_paciente = input('Informe a sua idade: ')
                
                if idade_paciente.isdigit():
                    idade_paciente = int(idade_paciente)
                    if idade_paciente < 0 or idade_paciente > 100:
                        idade_paciente = float(idade_paciente)
                        print('Idade inválida')
                        break
                    else:
                        pass
                else:
                    print('Valor incorreto')
                    time.sleep(1)
                    limpar()
                    continue

                fumante = input('Você é fumante? [S]im ou [N]ão: ').lower()

                resultado_fumante = ''

                if fumante != '':
                    if fumante == 's' or fumante == 'sim':
                        resultado_fumante = 'Você é fumante. Cuidado! Isso pode agravar seu quadro respiratório'
                    elif fumante == 'n' or fumante == 'nao' or fumante == 'não':
                        resultado_fumante = 'Você não é fumante. Parabéns! Isso pode não agravar seu quadro respiratório'
                else:
                    print('Valor errado')
                    time.sleep(1)
                    limpar()
                    continue

                limpar()
                break

            except Exception:
                print('Informação incorreta.')
                time.sleep(1)
                limpar()
                continue

        print('------------------------------------')
        print('DOENÇAS PRÉ EXISTENTES')
        print('------------------------------------')


        while True:
            hipertenso = input('Você é hipertenso? [S]im ou [N]ão: ').strip().lower()

            if hipertenso == 's' or hipertenso == 'sim' and hipertenso.isalpha():
                doencas_existentes.append('hipertenso')
            elif hipertenso == 'n' or hipertenso == 'nao' or hipertenso == 'não':
                pass #Siga o while
            else:
                print('Opção inválida.')
                time.sleep(1)
                limpar()
                continue
            

            asmatico = input('Você é asmatico? [S]im ou [N]ão: ').strip().lower()

            if asmatico == 's' or asmatico == 'sim' and asmatico.isalpha():
                doencas_existentes.append('asmatico')
            elif asmatico == 'n' or asmatico == 'nao' or asmatico == 'não':
                pass #Siga o while
            else:
                print('Opção inválida.')
                time.sleep(1)
                limpar()
                continue
            

            diabetico = input('Você é diabetico? [S]im ou [N]ão: ').strip().lower()

            if diabetico == 's' or diabetico == 'sim' and diabetico.isalpha():
                doencas_existentes.append('diabetico')
            elif diabetico == 'n' or diabetico == 'nao' or diabetico == 'não':
                pass #Siga o while
            else:
                print('Opção inválida.')
                time.sleep(1)
                limpar()
                continue
            
            limpar()
            break

        while True:
            print('SINTOMAS APRESENTADOS')

            tosse_seca = input('Você está com tosse seca? [S]im ou [N]ão: ').strip().lower()

            if tosse_seca == 's' or tosse_seca == 'sim':
                sintomas_apresentados.append('Tosse seca')
            elif tosse_seca == 'n' or tosse_seca == 'nao' or tosse_seca == 'não':
                pass
            else:
                print('Valor incorreto')
                time.sleep(1)
                limpar()
                continue
            
            exausto = input('Você está exausto? [S]im ou [N]ão: ').strip().lower()

            if exausto == 's' or exausto == 'sim':
                sintomas_apresentados.append('Exausto')
            elif exausto == 'n' or exausto == 'nao' or exausto == 'não':
                pass
            else:
                print('Valor incorreto')
                time.sleep(1)
                limpar()
                continue

            febre = input('Você está com febre? [S]im ou [N]ão: ').strip().lower()

            if febre == 's' or febre == 'sim':
                sintomas_apresentados.append('Febre')
            elif febre == 'n' or febre == 'nao' or febre == 'não':
                pass
            else:
                print('Valor incorreto')
                time.sleep(1)
                limpar()
                continue

            respirar = input('Você está com falta Respirar? [S]im ou [N]ão: ').strip().lower()

            if respirar == 's' or respirar == 'sim':
                sintomas_apresentados.append('Falta de Respirar')
            elif respirar == 'n' or respirar == 'nao' or respirar == 'não':
                pass
            else:
                print('Valor incorreto')
                time.sleep(1)
                limpar()
                continue
                            
            limpar()
            break

        
        print('Segue relatório conforme as suas informações coletadas:')
        print(f'Seu nome é: {nome_paciente}')

        print(f'Sua idade é de: {idade_paciente}')

        if idade_paciente >= 65:
            print('Aproveitando você tem acima de 65 anos, é caso de risco.')


        if len(doencas_existentes) > 0:
            print('Você as tem seguinte doenças que pode agravar caso tenha a doença:')
            for doenca in doencas_existentes:
                print(doenca)
        else:
            print('Não tem nenhuma doenças pré-existentes.')
            pass
        
        if len(sintomas_apresentados) > 0:
            print('Você tem sintomas da COVID-19 procure URGENTE um posto médico:')
            for sintomas in sintomas_apresentados:
                print(sintomas)
        else:
            print('Você não possui nenhum sintoma de COVID-19, continue uusando mascaras.')
        
        if fumante == 's' or fumante == 'sim':
                print(resultado_fumante)
        
    except Exception:
        print('\nErro desconhecido.')
        time.sleep(1)
        limpar()
        continue

    except KeyboardInterrupt:
        print('\nInterropido pelo usuário, saindo do sistema.')
        time.sleep(1)
        limpar()
        break
