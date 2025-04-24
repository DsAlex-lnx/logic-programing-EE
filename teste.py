# Sistema de Gerenciamento de Reservatório de Água
nivel_atual = 0
continuar = True

# Loop principal do programa
while continuar:
    # Exibir menu
    print("\n===== SISTEMA DE GERENCIAMENTO DE RESERVATÓRIO =====")
    print("1. Registrar nível atual da água")
    print("2. Exibir status do reservatório")
    print("3. Processar enchimento")
    print("4. Encerrar programa")
    print("=====================================================")
    
    # Obter escolha do usuário
    opcao = input("\nEscolha uma opção (1-4): ")
    
    # Opção 1: Registrar nível atual
    if opcao == "1":
    
        nivel = float(input("Digite o nível atual da água (0-100%): "))
        if 0 <= nivel <= 100:
            nivel_atual = nivel
            print(f"Nível registrado com sucesso: {nivel_atual}%")
        else:
            print("Erro: O nível deve estar entre 0 e 100%.")
    
    
    # Opção 2: Exibir status do reservatório
    elif opcao == "2":
        print("\n----- STATUS DO RESERVATÓRIO -----")
        print(f"Nível atual: {nivel_atual}%")
        
        # Determinar tempo de abertura da válvula
        if nivel_atual < 20:
            tempo_abertura = 60
            status = "CRÍTICO"
        elif nivel_atual < 50:
            tempo_abertura = 30
            status = "MODERADO"
        else:
            tempo_abertura = 15
            status = "BOM"
        
        print(f"Tempo de abertura da válvula: {tempo_abertura} minutos")
        print(f"Status do nível: {status}")
    
    # Opção 3: Processar enchimento
    elif opcao == "3":
        print("\nIniciando processo de enchimento...")
        print(f"Nível atual: {nivel_atual}%")
        
        # Determinar tempo de abertura da válvula
        if nivel_atual < 20:
            tempo_abertura = 60
        elif nivel_atual < 50:
            tempo_abertura = 30
        else:
            tempo_abertura = 15
        
        print(f"Tempo de abertura da válvula: {tempo_abertura} minutos")
        
        # Simular o enchimento a cada 5 minutos
        incremento_por_5min = 5  # Incremento de 5% a cada 5 minutos
        nivel_anterior = nivel_atual
        
        # Loop para simular o enchimento
        for minuto in range(5, tempo_abertura + 1, 5):
            nivel_atual += incremento_por_5min
            if nivel_atual > 100:
                nivel_atual = 100
                print(f"Após {minuto} minutos: Nível atingiu 100% (capacidade máxima)")
                break
            print(f"Após {minuto} minutos: Nível atual {nivel_atual}%")
        
        print(f"\nProcesso de enchimento concluído.")
        print(f"Nível anterior: {nivel_anterior}%")
        print(f"Nível atual: {nivel_atual}%")
        print(f"Aumento: {nivel_atual - nivel_anterior}%")
    
    # Opção 4: Encerrar programa
    elif opcao == "4" or opcao.lower() == "sair":
        print("\nEncerrando o programa. Obrigado por utilizar o Sistema de Gerenciamento de Reservatório!")
        continuar = False
    
    # Opção inválida
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")
