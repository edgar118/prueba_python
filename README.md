## Evaluación Python

### Instalación

1. Instalar virtualenv: Si aún no tienes instalado virtualenv en tu máquina, puedes instalarlo utilizando pip:

```bash
pip install virtualenv
```
2. Clonar el repositorio: Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/proyecto-xyz.git
```
3. Crear un entorno virtual: Navega al directorio del proyecto y crea un entorno virtual:

```bash
cd proyecto-xyz
virtualenv venv
```

4. Activar el entorno virtual: Activa el entorno virtual: 

```bash
venv\Scripts\activate
```

En _macOS_ y _Linux_:
```bash
source venv/bin/activate
```

5. Instalar las dependencias: Instala las librerías requeridas que se encuentran en el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

### Ejecución

Pruebas: Para ejecutar el archivo de pruebas, utiliza el siguiente comando

```bash
python prueba.py
```

Pruebas unitarias: Para ejecutar el archivo de pruebas unitarias, utiliza el siguiente comando:

```bash
python unit_test.py
```
