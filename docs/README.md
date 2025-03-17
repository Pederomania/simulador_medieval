Simulador Medieval
📜 Descripción

Simulador Medieval es un mundo dinámico donde los NPCs evolucionan de manera independiente, tomando decisiones basadas en su aprendizaje, emociones y relaciones sociales. La simulación transcurre en un entorno escalable que comienza con un pueblo y puede expandirse a regiones más grandes con el tiempo.
🏰 Características Principales

✅ NPCs con IA independiente: Memoria a largo plazo, aprendizaje progresivo y toma de decisiones autónoma.
✅ Mundo vivo y dinámico: Cambios de estaciones, clima, enfermedades y evolución social.
✅ Registro detallado: Simulación basada en logs de texto con sistema de turnos (30 min - 1 hora en el juego).
✅ Sin límites predefinidos: Expansión de asentamientos sin restricciones en el número de NPCs.
✅ Eventos naturales: Impacto del clima y estaciones en la vida cotidiana de los NPCs.
📂 Estructura del Proyecto

/simulador-medieval
│
├── /data                  # Datos del simulador
│   ├── /memorias          # Memorias de los NPCs
│   ├── /backup            # Copias de seguridad de memorias
│   └── /gym               # Datos de entrenamiento de IA
│
├── /config                # Configuración del simulador e IA
│
├── /docs                  # Documentación
│
├── /src                   # Código fuente
│   ├── /ia                # IA de los NPCs
│   ├── /simulacion        # Sistema de turnos y eventos
│   ├── /repositorio       # Gestión de memoria y datos
│   ├── /tests             # Pruebas unitarias e integración
│   ├── main.py            # Punto de entrada del simulador
│   └── config.py          # Configuración central
│
├── /scripts               # Scripts auxiliares
└── requirements.txt       # Dependencias del proyecto

🚀 Instalación y Ejecución
1️⃣ Requisitos previos

    Python 3.10

    pip instalado

2️⃣ Clonar el repositorio

git clone https://github.com/tu_usuario/simulador-medieval.git
cd simulador-medieval

3️⃣ Instalar dependencias

pip install -r requirements.txt

4️⃣ Ejecutar la simulación

python src/main.py

🛠️ Tecnologías utilizadas

    Python 3.10: Lenguaje principal del simulador.

    YAML: Configuración modular del simulador.

    JSON: Almacenamiento de memorias de NPCs.

    Pytest: Pruebas unitarias y de integración.

👥 Contribuciones

Si deseas contribuir al proyecto, revisa la Guía de Desarrolladores en /docs/Guía_Desarrolladores.md.
📩 Contacto

Si tienes dudas o sugerencias, puedes abrir un issue en el repositorio o contactarme directamente.