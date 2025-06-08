# Calculadora de Raíces de Polinomios

Este proyecto es una aplicación web desarrollada con Django que permite calcular raíces de polinomios utilizando métodos numéricos como Bisección, Newton-Raphson y Newton-Raphson Modificado. El usuario puede ingresar un polinomio y seleccionar el método deseado, así como los parámetros necesarios para cada método. La aplicación muestra la raíz aproximada, una tabla de iteraciones y una gráfica del polinomio.

---

## Requisitos

- Python 3.10 o superior
- Git (opcional, para clonar el repositorio)

---

## Instalación

1. **Clona el repositorio o descarga el código:**

   ```bash
   git clone https://github.com/tu-usuario/Calculadora.git
   cd Calculadora
   ```

2. **Crea y activa un entorno virtual (recomendado):**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r venv/requirements.txt
   ```

---

## Uso

1. **Realiza las migraciones de la base de datos:**

   ```bash
   python manage.py migrate
   ```

2. **Inicia el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

3. **Abre tu navegador y accede a:**

   ```
   http://127.0.0.1:8000/
   ```

---

## Estructura del Proyecto

- **views.py**: Lógica principal de la vista, procesamiento del formulario, ejecución de los métodos numéricos y generación de la gráfica.
- **forms.py**: Definición del formulario para ingresar el polinomio, método y parámetros.
- **utils.py**: Implementación de los métodos numéricos y utilidades para evaluar polinomios.
- **index.html**: Plantilla HTML para la interfaz de usuario.
- **settings.py**: Configuración principal del proyecto Django.
- **requirements.txt**: Lista de dependencias del proyecto.

---

## Dependencias Principales

- Django
- sympy
- numpy
- matplotlib
- plotly

---

## Notas

- Si tienes problemas con la instalación de algún paquete, asegúrate de tener actualizado `pip` con `python -m pip install --upgrade pip`.
- Puedes modificar el archivo `requirements.txt` si necesitas agregar o quitar dependencias.

---

## Licencia

Este proyecto es de uso académico y libre para modificar.