import random
                                           
vagas = {"carro": 5, "moto": 3}                                                                     # Definição das variáveis.
estacionamento = {}                                                                                 # Dicionário que armazena os veículos estacionados.

precos = {"carro": 5.00, "moto": 3.00}                                     

def estacionar_veiculo():                                                                           # Função para registrar a entrada de um veículo no estacionamento.
    placa = input("Digite a placa do veículo: ").strip().upper()                                    # Converte a placa para maiúsculas.
    tipo = input("Digite o tipo do veículo (carro/moto): ").strip().lower()                         # Converte o tipo para minúsculas.
    
                                                                            
    if tipo not in ["carro", "moto"]:                                                               # Estrutura condicional.
        return
    
                                                                                                    # Verifica se há vagas disponíveis.
    if vagas[tipo] > 0:
        estacionamento[placa] = {"tipo": tipo}                             
        vagas[tipo] -= 1                                                    
        print("Veículo estacionado com sucesso!!")
    else:
        print("Não há vagas disponíveis para este tipo de veículo!.")

def remover_veiculo():                                                                              # Função para remover um veículo.
    placa = input("Digite a placa do veículo: ").strip().upper()                                    # Converte a placa para maiúsculas.
    
                                                   
    if placa in estacionamento:                                             
        tipo = estacionamento[placa]["tipo"]                                
        tempo_permanencia = random.randint(1, 5)                            
        total_pagar = tempo_permanencia * precos[tipo]                      
        
        
        vagas[tipo] += 1                                                                            # Libera a vaga removendo o veículo do dicionário e aumentando o número de vagas disponíveis
        del estacionamento[placa]
        
        print(f"Veículo permaneceu por {tempo_permanencia} horas. Total a pagar: R$ {total_pagar:.2f}")
        print("Veículo removido com sucesso!")
    else:
        print("Veículo não encontrado no estacionamento!")

def listar_veiculos():                                                                              # Função para listar os veículo.
    if estacionamento:
        print("Veículos estacionados:")
                                                                            
        for placa, dados in estacionamento.items():                                                 # Loop que percorre o dicionário de veículos estacionados para listá-los
            print(f"Placa: {placa} | Tipo: {dados['tipo'].capitalize()}")                           # Exibe a placa e o tipo do veículo formatado corretamente.
    else:
        print("Nenhum veículo estacionado no momento.")

def main():                                                                                         # Função principal que exibe o menu e gerencia as opções do usuário.                           
    while True:                                                                                     # Loop infinito para manter o programa em execução até que o usuário escolha sair
        print("\nBem-vindo ao Gerenciamento de estacionamento!")
        print("1. Estacionar veículo")
        print("2. Remover veículo")
        print("3. Listar veículos estacionados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")                               
        
                                                                                                    # Estruturas condicionais para decidir qual função chamar com base na opção informada
        if opcao == "1":
            estacionar_veiculo()
        elif opcao == "2":
            remover_veiculo()
        elif opcao == "3":
            listar_veiculos()
        elif opcao == "4":
            print("Saindo do sistema...")
            break                                                                                   # Finaliza o loop.
        else:
            print("Inválido! Tente novamente.")

if __name__ == "__main__":
    main()                                                                                          # Inicia chamando a função principal.
