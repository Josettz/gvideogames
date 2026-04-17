# 🎮 Game Library Manager (POO)

Este repositorio contiene un sistema básico de gestión de biblioteca de videojuegos desarrollado en **Python**. El proyecto está diseñado para demostrar el dominio de conceptos fundamentales de la **Programación Orientada a Objetos (POO)**.

## 🚀 Características

- **Gestión de Usuarios:** Creación de perfiles con bibliotecas de juegos independientes.
- **Encapsulamiento:** Uso de atributos privados (`__biblioteca`) para asegurar la integridad de los datos.
- **Lógica de Juego:** Sistema para buscar títulos en la biblioteca y actualizar las horas de juego acumuladas.
- **Reporte de Actividad:** Generación automática de un **Top 3** basado en el tiempo de juego utilizando funciones `lambda` y algoritmos de ordenamiento.

## 🛠️ Tecnologías y Conceptos Aplicados

* **Lenguaje:** Python 3.x
* **POO:** Clases, métodos de instancia, constructores (`__init__`) y manejo de estados.
* **Data Handling:** Uso de listas, iteraciones con validación de existencia y ordenamiento avanzado de colecciones de objetos.

## 📂 Estructura del Proyecto

El código se divide en dos clases principales:

1.  **`usuario`**: Encargada de la lógica de negocio, manejo de la biblioteca privada y visualización de estadísticas.
2.  **`videojuego`**: Clase modelo que define las propiedades esenciales de cada título (Título, Género, Horas Jugadas).

## 💻 Ejemplo de Ejecución

```python
# Crear una instancia de usuario
mi_usuario = usuario("Jose")

# Crear instancias de videojuegos
mi_juego1 = videojuego("Valorant", "Shooter", 500)
mi_juego2 = videojuego("Minecraft", "Mundo abierto", 1000)

# Interactuar con el sistema
mi_usuario.agregar_juego(mi_juego1)
mi_usuario.jugar("Valorant", 200)
mi_usuario.top_3_mas_jugados()
