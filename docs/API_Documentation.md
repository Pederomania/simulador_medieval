📖 Documentación de la API
📌 Introducción

Este documento describe la API interna del Simulador Medieval, incluyendo las clases y funciones principales del sistema de IA, la simulación y el repositorio de datos.
📂 Módulos Principales
📍 src/ia/ – Inteligencia Artificial

Maneja el aprendizaje, emociones y evolución de los NPCs.
🔹 aprendizaje.py

class Aprendizaje:
    """Gestiona el aprendizaje de los NPCs a través de la experiencia."""
    
    def entrenar(self, habilidad: str, tiempo: int) -> None:
        """
        Entrena una habilidad específica del NPC.
        
        :param habilidad: Nombre de la habilidad a entrenar.
        :param tiempo: Cantidad de tiempo invertido en el entrenamiento.
        """
        pass

🔹 emociones.py

class Emociones:
    """Modelo de emociones de los NPCs que afecta su comportamiento."""
    
    def ajustar_emocion(self, tipo: str, intensidad: float) -> None:
        """
        Modifica la emoción del NPC según eventos ocurridos.
        
        :param tipo: Tipo de emoción (ej. 'alegría', 'miedo').
        :param intensidad: Valor de la emoción entre 0 y 1.
        """
        pass

📍 src/simulacion/ – Sistema de Simulación

Gestiona turnos, eventos y evolución del mundo.
🔹 turno.py

class Turno:
    """Controla la gestión del tiempo en la simulación."""

    def avanzar(self) -> None:
        """Avanza la simulación un turno (30 min - 1 hora en el juego)."""
        pass

🔹 eventos.py

class Eventos:
    """Maneja los eventos naturales y sociales dentro del simulador."""
    
    def generar_evento(self) -> dict:
        """
        Genera un evento aleatorio en el mundo del simulador.
        
        :return: Diccionario con los detalles del evento generado.
        """
        pass

📍 src/repositorio/ – Almacenamiento de Datos

Maneja las memorias de los NPCs y la persistencia de datos.
🔹 json_repository.py

class JSONMemoryRepository:
    """Repositorio que gestiona la memoria de los NPCs en archivos JSON."""

    def guardar_memoria(self, npc_id: str, datos: dict) -> None:
        """
        Guarda la memoria de un NPC en un archivo JSON.
        
        :param npc_id: Identificador único del NPC.
        :param datos: Información de la memoria a almacenar.
        """
        pass

    def cargar_memoria(self, npc_id: str) -> dict:
        """
        Carga la memoria de un NPC desde un archivo JSON.
        
        :param npc_id: Identificador único del NPC.
        :return: Diccionario con la memoria del NPC.
        """
        pass

⚙️ Ejemplo de Uso

from src.ia.aprendizaje import Aprendizaje
from src.simulacion.turno import Turno

# Crear una instancia del sistema de aprendizaje
ia_npc = Aprendizaje()
ia_npc.entrenar("caza", 3)

# Avanzar un turno en la simulación
sim_turno = Turno()
sim_turno.avanzar()

📩 Contacto y Contribución

Si encuentras errores o deseas contribuir, abre un issue en el repositorio.