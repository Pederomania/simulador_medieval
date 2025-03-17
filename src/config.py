import yaml
import os


def cargar_configuracion():
    """
    Carga la configuración desde los archivos YAML en la carpeta 'config'.
    """
    config = {}
    try:
        config_files = ["ia.yaml", "logging.yaml", "simulador.yaml"]
        for file_name in config_files:
            file_path = os.path.join(os.path.dirname(__file__), "../config", file_name)
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    config[file_name] = yaml.safe_load(file)
            else:
                raise FileNotFoundError(f"El archivo {file_name} no se encontró.")
    except Exception as e:
        raise Exception(f"Error al cargar la configuración: {e}")

    return config
