🏗️ Guía para Desarrolladores
📌 Introducción

Bienvenido al desarrollo del Simulador Medieval. Este documento proporciona información clave para contribuir al proyecto, incluyendo la estructura del código, guías de desarrollo y buenas prácticas.
📂 Estructura del Proyecto

/simulador-medieval
│
├── /data                  # Datos del simulador (memorias de NPCs, backups, entrenamientos)
│├── /config                # Configuración del simulador e IA
│
├── /docs                  # Documentación
│
├── /src                   # Código fuente
│   ├── /ia                # IA de los NPCs (aprendizaje, emociones, etc.)
│   ├── /simulacion        # Sistema de turnos y eventos
│   ├── /repositorio       # Gestión de almacenamiento de datos (JSON, SQLite)
│   ├── /tests             # Pruebas unitarias e integración
│   ├── main.py            # Punto de entrada del simulador
│   └── config.py          # Configuración central
│
├── /scripts               # Scripts auxiliares
└── requirements.txt       # Dependencias del proyecto

🛠️ Entorno de Desarrollo
1️⃣ Requisitos previos

    Python 3.10

    pip instalado

    PyCharm (opcional, recomendado)

2️⃣ Clonar el repositorio

git clone https://github.com/tu_usuario/simulador-medieval.git
cd simulador-medieval

3️⃣ Crear un entorno virtual

python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows

4️⃣ Instalar dependencias

pip install -r requirements.txt

🖥️ Desarrollo y Contribución
📌 Normas de Código

    Usa PEP8 como estándar de codificación.

    Mantén el código modular y documentado con docstrings.

    Realiza pruebas unitarias para cada nueva funcionalidad.

    Sigue la estructura de carpetas establecida.

📌 Flujo de Trabajo

    Crea una rama para tu nueva funcionalidad o corrección:

git checkout -b feature/nombre-funcionalidad

Desarrolla y prueba el código antes de hacer commit.

Asegúrate de que los tests pasan antes de subir cambios:

pytest src/tests/

Haz commit siguiendo buenas prácticas:

    git commit -m "Añadida funcionalidad X a la IA de los NPCs"

    Sube la rama y abre un Pull Request.

🔍 Pruebas y Debugging
🔹 Ejecutar pruebas unitarias

pytest src/tests/

🔹 Activar logs para debugging

Modifica el archivo config/logging.yaml para cambiar el nivel de logs:

log_level: DEBUG  # INFO, WARNING, ERROR, CRITICAL

🏗️ Implementaciones Futuras

    Optimización del sistema de memoria de los NPCs.

    Soporte para almacenamiento en SQLite.

    Mejora del sistema de emociones y relaciones sociales.

📩 Contacto y Soporte

Si tienes dudas, abre un issue en el repositorio o contacta con el equipo de desarrollo.