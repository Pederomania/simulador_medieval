import pkg_resources

# Obtener todas las librerías instaladas en el entorno actual
installed_packages = pkg_resources.working_set

# Imprimir cada librería con su versión
for package in installed_packages:
    print(f"{package.project_name}=={package.version}")
