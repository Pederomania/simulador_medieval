# sqlite_repository.py
import sqlite3
import json
import os
from datetime import datetime
import pytz
from src.config import cargar_configuracion

class SQLiteMemoryRepository:
    def __init__(self):
        """
        Inicializa el repositorio SQLite y crea la base de datos si no existe.
        """
        config = cargar_configuracion()
        self.ruta_db = config["repositorio"]["sqlite"]["ruta"]
        self._crear_directorio_si_no_existe()
        try:
            self._inicializar_db()
        except sqlite3.Error as e:
            raise Exception(f"Error al inicializar la base de datos: {e}")

    def _crear_directorio_si_no_existe(self):
        """
        Crea el directorio para la base de datos si no existe.
        """
        directorio = os.path.dirname(self.ruta_db)
        if not os.path.exists(directorio):
            try:
                os.makedirs(directorio, exist_ok=True)
            except OSError as e:
                raise Exception(f"No se pudo crear el directorio: {e}")

    def _inicializar_db(self):
        """
        Crea la tabla 'memorias' si no existe.
        """
        try:
            with sqlite3.connect(self.ruta_db) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS memorias (
                        npc_id INTEGER PRIMARY KEY,
                        memoria TEXT,
                        timestamp TEXT
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Error al crear la tabla: {e}")

    def guardar_memoria(self, npc_id, memoria):
        """
        Guarda la memoria de un NPC en la base de datos.

        Args:
            npc_id (int): ID del NPC.
            memoria (list): Lista de eventos en la memoria del NPC.
        """
        try:
            with sqlite3.connect(self.ruta_db) as conn:
                cursor = conn.cursor()
                timestamp = datetime.now(pytz.UTC).isoformat()  # Usar zona horaria UTC
                cursor.execute("""
                    INSERT OR REPLACE INTO memorias (npc_id, memoria, timestamp)
                    VALUES (?, ?, ?)
                """, (npc_id, json.dumps(memoria), timestamp))
                conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Error al guardar la memoria: {e}")

    def cargar_memoria(self, npc_id):
        """
        Carga la memoria de un NPC desde la base de datos.

        Args:
            npc_id (int): ID del NPC.

        Returns:
            list: Lista de eventos en la memoria del NPC, o None si no existe.
        """
        try:
            with sqlite3.connect(self.ruta_db) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT memoria FROM memorias WHERE npc_id = ?", (npc_id,))
                resultado = cursor.fetchone()
                return json.loads(resultado[0]) if resultado else None
        except (sqlite3.Error, json.JSONDecodeError) as e:
            raise Exception(f"Error al cargar la memoria: {e}")

    def eliminar_memoria(self, npc_id):
        """
        Elimina la memoria de un NPC de la base de datos.

        Args:
            npc_id (int): ID del NPC.
        """
        try:
            with sqlite3.connect(self.ruta_db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM memorias WHERE npc_id = ?", (npc_id,))
                conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Error al eliminar la memoria: {e}")

    def backup_memorias(self, backup_path="data/backup"):
        """
        Realiza una copia de seguridad de la base de datos en un archivo SQL.

        Args:
            backup_path (str): Ruta donde se guardará el archivo de backup.
        """
        try:
            os.makedirs(backup_path, exist_ok=True)
            timestamp = datetime.now(pytz.UTC).strftime("%Y%m%d_%H%M%S")  # Timestamp con zona horaria UTC
            backup_file = os.path.join(backup_path, f"backup_{timestamp}.sql")
            with sqlite3.connect(self.ruta_db) as conn:
                with open(backup_file, "w") as file:
                    for linea in conn.iterdump():
                        file.write(f"{linea}\n")
        except (sqlite3.Error, IOError) as e:
            raise Exception(f"Error al realizar el backup: {e}")
