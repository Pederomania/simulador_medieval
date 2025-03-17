#test_repositorio.py
import os
import pytest
from src.repositorio.sqlite_repository import SQLiteMemoryRepository

@pytest.fixture
def repositorio():
    return SQLiteMemoryRepository()

def test_guardar_y_cargar_memoria(repositorio):
    memoria = ["Evento1", "Evento2"]
    repositorio.guardar_memoria(1, memoria)
    assert repositorio.cargar_memoria(1) == memoria

def test_eliminar_memoria(repositorio):
    memoria = ["Evento1"]
    repositorio.guardar_memoria(2, memoria)
    repositorio.eliminar_memoria(2)
    assert repositorio.cargar_memoria(2) is None

def test_backup_memorias(repositorio):
    memoria = ["Evento1"]
    repositorio.guardar_memoria(3, memoria)
    repositorio.backup_memorias()
    assert os.path.exists("data/backup/backup_YYYYMMDD_HHMMSS.sql")  # Verificar backup

def test_excepcion_guardar_memoria(repositorio):
    with pytest.raises(Exception):
        repositorio.guardar_memoria(1, ["Evento1"])  # Simular error de I/O