# json_repository.py
import json
import os
import shutil
from datetime import datetime
import pytz
from src.config import cargar_configuracion

class JSONMemoryRepository:
    def __init__(self):
        config = cargar_configuracion()
        self.base_path = config["repositorio"]["json"]["ruta"]
        try:
            os.makedirs(self.base_path, exist_ok=True)
            if not os.path.exists(self.base_path):
                raise Exception(f"No se pudo crear el directorio: {self.base_path}")
        except OSError as e:
            raise Exception(f"Error al crear el directorio: {e}")

    def guardar_memoria(self, npc_id, memoria):
        file_path = os.path.join(self.base_path, f"memoria_{npc_id:04d}.json")
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                timestamp = datetime.now(pytz.UTC).isoformat()  # Usar zona horaria UTC
                json.dump({
                    "npc_id": npc_id,
                    "memoria": memoria,
                    "timestamp": timestamp
                }, file)
        except IOError as e:
            raise Exception(f"Error al guardar la memoria: {e}")

    def cargar_memoria(self, npc_id):
        file_path = os.path.join(self.base_path, f"memoria_{npc_id:04d}.json")
        if not os.path.exists(file_path):
            return None
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error al cargar la memoria: {e}")

    def eliminar_memoria(self, npc_id):
        file_path = os.path.join(self.base_path, f"memoria_{npc_id:04d}.json")
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except OSError as e:
                raise Exception(f"Error al eliminar la memoria: {e}")

    def backup_memorias(self, backup_path="data/backup"):
        timestamp = datetime.now(pytz.UTC).strftime("%Y%m%d_%H%M%S")  # Timestamp con zona horaria UTC
        backup_path = os.path.join(backup_path, f"backup_{timestamp}")
        try:
            os.makedirs(backup_path, exist_ok=True)
            for file_name in os.listdir(self.base_path):
                shutil.copy(os.path.join(self.base_path, file_name), backup_path)
        except (OSError, shutil.Error) as e:
            raise Exception(f"Error al realizar el backup: {e}")
