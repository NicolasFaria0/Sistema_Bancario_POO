class Autenticacao:
    def __init__(self):
        self.usuarios = {}

    def registrar(self,registro,nome,telefone,senha):
        if registro in self.usuarios:
            print("Registro já existente. Tente outro.")
        else:
            self.usuarios[registro] = {
                "nome":nome,
                "telefone":telefone,
                "senha":senha,
            }
            print("Registro realizado com sucesso!")

    def autenticar(self, registro, senha):
        if registro in self.usuarios and self.usuarios[registro]["senha"] == senha:
            return True
        else:
            print("Registro ou senha incorretos.")
            return False

    def obter_dados_usuario(self, registro):
        if registro in self.usuarios:
            return self.usuarios[registro]["nome"], self.usuarios[registro]["telefone"]
        else:
            print("Usuário não encontrado.")
            return None, None