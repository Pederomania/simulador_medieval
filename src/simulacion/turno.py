#turno.py
import time
from src.tests.config import Configuracion  # Importa correctamente desde la ubicación de config.py

class Turno:
    def __init__(self):
        """
        Inicializa el sistema de turnos usando los valores de config.py.
        """
        self.duracion_turno = Config.DURACION_TURNO  # Usamos la duración del turno desde config.py
        self.duracion_total = Config.DURACION_TOTAL  # Usamos la duración total desde config.py
        self.turno_actual = 0
        self.tiempo_transcurrido = 0

    def avanzar_turno(self):
        """
        Avanza el tiempo en un turno. Ejecuta las acciones de los NPCs.
        """
        if self.tiempo_transcurrido >= self.duracion_total:
            print("El ciclo ha terminado.")
            return False

        # Avanzar turno
        self.turno_actual += 1
        self.tiempo_transcurrido += self.duracion_turno

        print(f"Turno {self.turno_actual} iniciado: {self.tiempo_transcurrido}/{self.duracion_total} minutos transcurridos.")

        # Aquí se pueden ejecutar las acciones de los NPCs por turno.
        self.ejecutar_acciones_npcs()

        # Esperar por la duración del turno (simulando el tiempo transcurrido).
        time.sleep(1)  # Simulación de espera, ajustar según sea necesario.

        return True

    def ejecutar_acciones_npcs(self):
        """
        Método placeholder para ejecutar las acciones de los NPCs.
        Esta parte debe integrarse con la IA de los NPCs para que
        realicen tareas específicas en cada turno.
        """
        print("Ejecutando acciones de NPCs...")
        # Aquí se podrían llamar funciones que gestionen las tareas de los NPCs, como
        # pesca, caza, construcción, etc., basadas en la IA y el estado del mundo.

    def iniciar_simulacion(self):
        """
        Inicia la simulación del ciclo de turnos.
        """
        while self.avanzar_turno():
            pass  # Continúa hasta que el ciclo termine.
        print("Simulación completada.")

# Ejemplo de uso
if __name__ == "__main__":
    simulador = Turno()  # Usamos los valores del config.py directamente
    simulador.iniciar_simulacion()
