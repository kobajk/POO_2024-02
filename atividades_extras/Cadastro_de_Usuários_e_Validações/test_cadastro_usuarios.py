import pytest
from cadastro_usuario import CadastroUsuario

def test_instanciacao():
    usuario = CadastroUsuario("João Silva", "123.456.789-00", "01/01/1990", "Rua A", "(11) 1234-5678", "senha1234")
    assert usuario.nome == "João Silva"

def test_validar_nome():
    usuario = CadastroUsuario("João Silva", "123.456.789-00", "01/01/1990", "Rua A", "(11) 1234-5678", "senha1234")
    assert usuario.validar_nome() is True

def test_validar_nome_invalido():
    usuario = CadastroUsuario("João", "123.456.789-00", "01/01/1990", "Rua A", "(11) 1234-5678", "senha1234")
    with pytest.raises(ValueError):
        usuario.validar_nome()

def test_validar_cpf():
    usuario = CadastroUsuario("João Silva", "123.456.789-00", "01/01/1990", "Rua A", "(11) 1234-5678", "senha1234")
    assert usuario.validar_cpf() is True

def test_validar_telefone_invalido():
    usuario = CadastroUsuario("João Silva", "123.456.789-00", "01/01/1990", "Rua A", "1234-5678", "senha1234")
    with pytest.raises(ValueError):
        usuario.validar_telefone()

def test_mostrar_info(capsys):
    usuario = CadastroUsuario("João Silva", "123.456.789-00", "01/01/1990", "Rua A", "(11) 1234-5678", "senha1234")
    usuario.mostrar_info()
    captured = capsys.readouterr()
    assert "João Silva" in captured.out

def test_gravar_info():
    usuario = CadastroUsuario("João Silva", "123.456.789-00", "01/01/1990", "Rua A", "(11) 1234-5678", "senha1234")
    usuario.gravar_info()
    with open("cadastro_123.456.789-00.txt", 'r') as file:
        assert "João Silva" in file.read()
