# usuario_simples.py
# Versão refatorada aplicando o princípio YAGNI: mantém-se apenas o
# necessário para cadastrar, fazer login e listar usuários.
import hashlib
from typing import List, Optional


class Usuario:
    """Representa um usuário com os dados exigidos pelos requisitos atuais"""

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)

    def _hash_senha(self, senha: str) -> str:
        """Gera o hash da senha (segurança básica)"""
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha: str) -> bool:
        """Valida a senha do usuário"""
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    """Gerencia a coleção de usuários: cadastro, login e listagem"""

    def __init__(self):
        self.usuarios: List[Usuario] = []

    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        """Cadastra novo usuário, rejeitando email duplicado"""
        if any(u.email == email for u in self.usuarios):
            raise ValueError("Email já cadastrado")

        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        return usuario

    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        """Realiza login validando email e senha"""
        for usuario in self.usuarios:
            if usuario.email == email and usuario.validar_senha(senha):
                return usuario
        return None

    def listar_todos(self) -> List[Usuario]:
        """Lista todos os usuários"""
        return self.usuarios
