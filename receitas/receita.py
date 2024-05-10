class ReceitasManager:
    def salvar_receita(self):
        nome = input("Digite o nome da receita: ")
        ingredientes = []
        while True:
            ingrediente = input("Digite um ingrediente (ou 'fim' para parar): ")
            if ingrediente.lower() == 'fim':
                break
            ingredientes.append(ingrediente)
        modo_preparo = input("Digite o modo de preparo: ")

        with open('receitas.txt', 'a') as arquivo:
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write("Ingredientes:\n")
            for ingrediente in ingredientes:
                arquivo.write(f"- {ingrediente}\n")
            arquivo.write("Modo de Preparo:\n")
            arquivo.write(f"{modo_preparo}\n")
            arquivo.write("\n")
        print("Receita gravada com sucesso!\n")

    def listar_receitas(self):
        try:
            with open('receitas.txt', 'r') as arquivo:
                print(arquivo.read())
        except FileNotFoundError:
            print("Ainda não existem receitas gravadas.\n")

    def procurar_receita(self):
        nome = input("Digite o nome da receita que deseja consultar: ")
        try:
            with open('receitas.txt', 'r') as arquivo:
                receitas_encontradas = []
                for linha in arquivo:
                    if nome.lower() in linha.lower():
                        receitas_encontradas.append(linha)
                        for linha in arquivo:
                            if linha.strip() == '':
                                break
                            receitas_encontradas.append(linha)
                        break
                if not receitas_encontradas:
                    print("Receita não encontrada.\n")
                else:
                    for receita in receitas_encontradas:
                        print(receita, end='')
        except FileNotFoundError:
            print("Ainda não existem receitas gravadas.\n")

    def apagar_receita(self):
        with open('receitas.txt', 'w') as arquivo:
            arquivo.write("")
        print("Arquivo de receitas limpo.\n")

    def run(self):
        while True:
            print("1 - Salvar Receita")
            print("2 - Procurar Receita")
            print("3 - Listar Receitas")
            print("4 - Apagar Receita")
            print("5 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.salvar_receita()
            elif opcao == '2':
                self.procurar_receita()
            elif opcao == '3':
                self.listar_receitas()
            elif opcao == '4':
                self.apagar_receita()
            elif opcao == '5':
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    manager = ReceitasManager()
    manager.run()
