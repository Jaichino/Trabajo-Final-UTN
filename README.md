# Trabajo final de curso
 Realizó: Aichino, Juan Ignacio

## Introducción

En el presente repositorio se desarrolla el trabajo final de la diplomatura de Python de la Universidad Tecnológica Nacional (UTN).
La aplicación consiste en un sistema básico de gestión para un supermercado, el cual permite administrar un inventario de productos, facilitando la ejecución de diversas acciones, como el filtrado, el ingreso, la modificación y la eliminación de productos. Además, incluye un módulo de ventas que posibilita realizar nuevas transacciones, la consulta de ventas previamente efectuadas y el registro de clientes para su incorporación como miembros, lo que les otorga acceso a descuentos exclusivos.

## Herramientas y metodologías utilizadas

Para el desarrollo de la aplicación se utilizó el lenguaje de programación Python, siguiendo el patrón de programación MVC (Modelo, Vista, Controlador) y aplicando Programación Orientada a Objetos (POO).

Para construir la interfaz gráfica se utilizó la librería Tkinter y Sqlite3 para el almacenamiento de datos.

Para el manejo de consultas a la base de datos se utilizó el ORM SQLModel.

Para la validación de ciertos campos de ingreso de datos, se utilizaron expresiones regulares (Regex).

Se desarrolló un control de logging utilizando tanto decoradores como el patrón observador.

El código de la aplicación se organiza siguiendo las convenciones estilísticas de la PEP8.

## Estructura de la aplicación

La aplicación se divide en dos módulos: Módulo de Inventario y Módulo de Ventas

#### 1) Módulo de inventario
Este módulo permite la visualización del stock de productos del negocio, como así también una sección de búsqueda para filtrar dichos productos según su codigo exacto o por aproximación
de su nombre, también permite el filtrado de productos donde su stock es cero.
Por otro lado, también se pueden ingresar nuevos productos o modificar y eliminar los ya existentes.

#### 2) Módulo de ventas
Este módulo se divide en dos partes, una en la que se pueden realizar nuevas transacciones y otra en la que se pueden consultar ventas realizadas con anterioridad, filtrando entre una
fecha inicial y una fecha final.
Dicho módulo también cuenta con un registro de clientes como "miembros del supermercado", en el cuál, si estos se encuentran registrados, podrán acceder a un determinado descuento
dependiendo del monto de venta a abonar (dicho registro se podrá hacer luego de una compra, y solo si el cliente acepta ser miembro, por lo tanto, los descuentos se aplicarían en las
siguientes compras que realicen estos clientes).



