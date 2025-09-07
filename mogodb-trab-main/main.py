import os
from pymongo import MongoClient

MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
MONGO_USER = os.getenv('MONGO_USER', 'root')
MONGO_PASS = os.getenv('MONGO_PASS', 'root')

class EstudanteCRUD:
    def __init__(self):
        try:
            self.client = MongoClient(
                f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin'
            )
            self.db = self.client['estudantes_db']
            self.colecao = self.db['estudantes']
            print("Conectado ao MongoDB com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")
            exit(1)

    def criar(self, nome, email, idade, curso):
        if self.colecao.find_one({"email": email}):
            print(f"O estudante com email '{email}' já existe no banco.")
            return
        estudante = {
            "nome": nome.strip().title(),
            "email": email.strip().lower(),
            "idade": idade,
            "curso": curso.strip().capitalize()
        }
        resultado = self.colecao.insert_one(estudante)
        print(f"Estudante '{nome}' criado com id: {resultado.inserted_id}")

    def listar(self):
        print("\nEstudantes cadastrados:")
        estudantes = list(self.colecao.find())
        if not estudantes:
            print("Nenhum estudante cadastrado ainda.")
        else:
            for doc in estudantes:
                print(f"- Nome: {doc.get('nome')}, Email: {doc.get('email')}, "
                      f"Idade: {doc.get('idade')}, Curso: {doc.get('curso')}")

    def atualizar(self, email, nova_idade=None, novo_curso=None):
        update_fields = {}
        if nova_idade is not None:
            update_fields['idade'] = nova_idade
        if novo_curso is not None:
            update_fields['curso'] = novo_curso.strip().capitalize()

        if not update_fields:
            print("Nenhum campo para atualizar.")
            return

        resultado = self.colecao.update_one({"email": email.strip().lower()}, {"$set": update_fields})
        if resultado.matched_count == 0:
            print(f"Estudante com email '{email}' não encontrado.")
        else:
            print(f"Estudante com email '{email}' atualizado com sucesso!")

    def deletar(self, email):
        resultado = self.colecao.delete_one({"email": email.strip().lower()})
        if resultado.deleted_count == 0:
            print(f"Estudante com email '{email}' não encontrado.")
        else:
            print(f"Estudante com email '{email}' removido com sucesso!")

    def fechar_conexao(self):
        self.client.close()
        print("Conexão com o MongoDB encerrada.")


def menu():
    crud = EstudanteCRUD()
    try:
        while True:
            print("\n==== MENU CRUD ESTUDANTES ====")
            print("1 - Cadastrar Estudante")
            print("2 - Listar Estudantes")
            print("3 - Atualizar Estudante")
            print("4 - Remover Estudante")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                nome = input("Nome: ")
                email = input("Email: ")
                while True:
                    idade_str = input("Idade (número inteiro): ")
                    try:
                        idade = int(idade_str)
                        break
                    except ValueError:
                        print("Por favor, digite um número inteiro para a idade.")
                curso = input("Curso: ")
                crud.criar(nome, email, idade, curso)

            elif opcao == '2':
                crud.listar()

            elif opcao == '3':
                email = input("Email do estudante a atualizar: ")
                nova_idade = input("Nova idade (deixe vazio para não alterar): ")
                novo_curso = input("Novo curso (deixe vazio para não alterar): ")
                crud.atualizar(
                    email,
                    int(nova_idade) if nova_idade.strip() else None,
                    novo_curso if novo_curso.strip() else None
                )

            elif opcao == '4':
                email = input("Email do estudante a remover: ")
                crud.deletar(email)

            elif opcao == '0':
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida! Tente novamente.")
    finally:
        crud.fechar_conexao()


if __name__ == "__main__":
    menu()
