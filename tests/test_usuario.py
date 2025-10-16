import pytest
from usuario import Usuario, usuarios_registrados

@pytest.fixture
def usuario_ejemplo():
    # Limpia la lista antes de cada test
    usuarios_registrados.clear()
    
    u = Usuario(
        id_usuario=1,
        nombre="Franco",
        usuario="franco_user",
        clave="1234",
        rol=False
    )
    u.registrar_usuario()
    return u

def test_registro_de_usuario(usuario_ejemplo):
    assert len(usuarios_registrados) == 1
    assert usuarios_registrados[0].get_usuario() == "franco_user"

def test_buscar_usuario_por_nombre(usuario_ejemplo):
    encontrado = Usuario.obtener_usuario_por_nombre("Franco")
    assert encontrado is not None
    assert encontrado.get_usuario() == "franco_user"

def test_buscar_usuario_inexistente(usuario_ejemplo):
    no_encontrado = Usuario.obtener_usuario_por_nombre("Carlos")
    assert no_encontrado is None

