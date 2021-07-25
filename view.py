import Controller
import os.path

'''
View responsável por receber e processar os inputs de usuários. 
Foi realizada de forma bastante simplista, pois o intuito era desenvolver e entender conceitos de arquitetura MVC.
Caso seja necessário implementar uma estrutura de front-end diferenciada, basta trabalhar algumas questões neste arquivo, 
onde não se perde todo o restante da estrutura desenvolvida.
'''

# Cria os arquivos-base do projeto caso não existam.
def criaArquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')

criaArquivos(
    'categoria.txt', 'clientes.txt', 'estoque.txt', 'fornecedores.txt', 'funcionarios.txt', 'venda.txt')

if __name__ == '__main__':
    while True:
        local = int(input('Digite 1 para acessar ( Categorias ) \n'
                          'Digite 2 para acessar ( Estoque )\n'
                          'Digite 3 para acessar ( Fornecedores )\n'
                          'Digite 4 para acessar ( Clientes )\n'
                          'Digite 5 para acessar ( Funcionários )\n'
                          'Digite 6 para acessar ( Vendas )\n'
                          'Digite 7 para ver os produtos mais vendidos\n'
                          'Digite 8 para sair\n'))
        
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma categoria\n'
                                    'Digite 2 para remover uma categoria\n'
                                    'Digite 3 para alterar uma categoria\n'
                                    'Digite 4 para mostrar as categorias cadastradas\n'
                                    'Digite 5 para sair\n'))
                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar\n')
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover\n')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar: \n')
                    novaCategoria = input(f'Digite o novo nome que deseja chamar a categoria {categoria}: ')
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                elif decidir == 5:
                    break

        if local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input('Digite 1 para cadastrar um produto\n'
                                    'Digite 2 para remover um produto\n'
                                    'Digite 3 para alterar um produto\n'
                                    'Digite 4 para ver o estoque\n'
                                    'Digite 5 para sair'))

                if decidir == 1:
                    nome = input('Digite o nome do produto que deseja cadastrar: \n')
                    preco = input('Digite o preço do produto: \n')
                    categoria = input('Digite a categoria do produto: \n')
                    quantidade  = input('Digite a quantidade do produto: \n')
                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input('Digite o produto que deseja remover: ')
                    cat.removerProduto(produto)
                elif decidir == 3:
                    produto = input('Digite o produto que deseja alterar: \n')
                    novoProduto = input(f'Digite como deseja chamar o produto {produto}: \n')
                    novoPreco = input('Digite o preço do produto: \n')
                    novaCategoria = input('Digite a nova categoria: \n')
                    novaQuantidade = input('Digite a nova quantidade: \n')
                    cat.alterarProduto(produto, novoProduto, novoPreco, novaCategoria, novaQuantidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                elif decidir == 5:
                    break

        if local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input('Digite 1 para cadastrar um fornecedor\n'
                                    'Digite 2 para remover um fornecedor\n'
                                    'Digite 3 para alterar um fornecedor\n'
                                    'Digite 4 para ver os fornecedores cadastrados\n'
                                    'Digite 5 para sair'))
                if decidir == 1:
                    nome = input('Digite o nome do fornecedor que deseja cadastrar: \n')
                    cnpj = input('Digite o cnpj do fornecedor: \n')
                    telefone = input('Digite o telefone do fornecedor: \n')
                    categoria  = input('Digite o ramo/categoria do fornecedor: \n')
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    nome = input('Digite o nome do fornecedor que deseja remover: ')
                    cat.removerFornecedor(nome)
                elif decidir == 3:
                    nomeAlterar = input('Digite o fornecedor que deseja alterar: \n')
                    novoNome = input(f'Digite como deseja chamar o fornecedor {nomeAlterar}: \n')
                    novoCnpj = input('Digite o CNPJ do fornecedor: \n')
                    novoTelefone = input('Digite o telefone do fornecedor: \n')
                    novaCategoria = input('Digite o ramo/categoria do fornecedor: \n')
                    cat.alterarFornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria)
                elif decidir == 4:
                    cat.mostrarFornecedores()
                elif decidir == 5:
                    break
                
        if local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = int(input('Digite 1 para cadastrar um cliente\n'
                                    'Digite 2 para remover um cliente\n'
                                    'Digite 3 para alterar um cliente\n'
                                    'Digite 4 para ver os clientes cadastrados\n'
                                    'Digite 5 para sair'))
                if decidir == 1:
                    nome = input('Digite o nome do cliente que deseja cadastrar: \n')
                    telefone = input('Digite o telefone do cliente: \n')
                    cpf = input('Digite o cpf do cliente: \n')
                    email = input('Digite o e-mail: ')
                    endereco = input('Informe o endereço: \n')
                    cat.cadastrarCliente(nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    nome = input('Digite o nome do cliente que deseja remover: ')
                    cat.removerCliente(nome)
                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do cliente que deseja alterar: \n')
                    novoNome = input(f'Digite como deseja chamar o cliente {nomeAlterar}: \n')
                    novoTelefone = input('Digite o telefone: \n')
                    novoCpf = input('Digite o CPF: \n')
                    novoEmail = input('Digite o e-mail do cliente: \n')
                    cat.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail)
                elif decidir == 4:
                    cat.mostrarClientes()
                elif decidir == 5:
                    break
        
        if local == 5:
            cat = Controller.ControllerFuncionario()
            while True:
                decidir = int(input('Digite 1 para cadastrar um funcionário\n'
                                    'Digite 2 para remover um funcionário\n'
                                    'Digite 3 para alterar um funcionário\n'
                                    'Digite 4 para ver os funcionários cadastrados\n'
                                    'Digite 5 para sair'))

                if decidir == 1:
                    clt = input('Digite a CLT do Funcionário: \n')
                    nome = input('Digite o nome do funcionário: \n')
                    telefone = input('Digite o telefone do funcionário: \n')
                    cpf = input('Digite o CPF: \n')
                    email = input('Digite o e-mail do funcionário: \n')
                    endereco = input('Digite o endereco do funcionário: \n')
                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    nome = input('Informe o nome do funcionário que deseja remover')
                    cat.removerFuncionario(nome)
                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do funcionário que deseja alterar: \n')
                    novoClt = input('Inclua o número da CLT: \n')
                    novoNome = input(f'Como será o novo nome de {nomeAlterar}? \n')
                    novoTelefone = input('Digite o novo telefone: \n')
                    novoCpf = input('Digite o CPF: \n')
                    novoEmail = input('Agora, inclua o e-mail por favor: \n')
                    novoEndereco = input('Para finalizar, informe o endereço do funcionário: \n')
                    cat.alterarFuncionario(nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cat.mostrarFuncionarios()
                elif decidir == 5:
                    break

        if local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma venda\n'
                                    'Digite 2 para mostrar as vendas de um período\n'
                                    'Digite 3 para sair\n'))
                if decidir == 1:
                    nomeProduto = input('Informe o produto que deseja vender: \n')
                    vendedor = input('Informe o vendedor: \n')
                    comprador = input('Informe o comprador: \n')
                    quantidadeVendida = input('Informe a quantidade: \n')
                    cat.cadastrarVenda(nomeProduto, vendedor, comprador, int(quantidadeVendida))
                elif decidir == 2:
                    dataInicio = input('Informe a data inicial (dd/mm/aaaa): \n')
                    dataTermino = input('Informe a data final (dd/mm/aaaa): \n')
                    cat.mostrarVenda(dataInicio, dataTermino)
                elif decidir == 3:
                    break
        
        if local == 7:
            cat = Controller.ControllerVenda()
            decidir = int(input('Digite 1 para gerar o relatório ou 2 para sair'))
            
            if decidir == 1:
                cat.relatorioProdutos()
            elif decidir == 2:
                break
        
        if local == 8:
            break

