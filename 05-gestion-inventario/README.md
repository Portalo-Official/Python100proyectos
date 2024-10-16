
# Gestión de Inventario - Proyecto en Python

Este proyecto implementa un sistema básico de gestión de inventario para una tienda. El objetivo es crear un sistema que permita gestionar productos, calcular el valor total del inventario, filtrar productos con bajo stock, y actualizar el inventario después de cada venta.

## Estructura del Proyecto

### 1. Clase `Producto`
Esta clase representa un producto en el inventario y contiene los siguientes atributos y métodos:

- **Atributos:**
  - `nombre`: Nombre del producto.
  - `cantidad`: Cantidad disponible en stock.
  - `precio`: Precio por unidad del producto.

- **Métodos:**
  - `realizar_venta(cantidad_vendida)`: Reduce el stock del producto tras realizar una venta.
  - `mostrar_info()`: Muestra la información del producto.

### 2. Clase `Inventario`
Esta clase maneja una lista de productos y proporciona varios métodos para gestionar el inventario.

- **Atributos:**
  - `productos`: Lista de objetos de tipo `Producto` que forman el inventario.

- **Métodos:**
  - `agregar_producto(producto)`: Añade un nuevo producto al inventario.
  - `valor_total_inventario()`: Calcula el valor total del inventario.
  - `productos_bajo_stock(umbral)`: Filtra y devuelve productos con stock por debajo de un determinado umbral.
  - `producto_mayor_valor()`: Devuelve el producto con el mayor valor total (cantidad * precio).
  - `actualizar_inventario_despues_venta(nombre_producto, cantidad_vendida)`: Actualiza el stock después de una venta.

## Datos Iniciales
El inventario se inicializa con los siguientes productos:

- Laptop: 25 unidades, 1200 USD
- Smartphone: 80 unidades, 800 USD
- Tablet: 50 unidades, 600 USD
- Monitor: 40 unidades, 300 USD
- Teclado: 100 unidades, 50 USD
- Ratón: 120 unidades, 40 USD
- Cámara: 30 unidades, 900 USD
- Impresora: 45 unidades, 150 USD

## Funcionalidades Principales

- **Calcular el valor total del inventario.**
- **Filtrar productos con bajo stock (por ejemplo, menos de 10 unidades).**
- **Actualizar la cantidad disponible después de una venta.**
- **Mostrar el producto con el valor total más alto en el inventario.**

## Cómo Ejecutar

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3 instalado.
3. Ejecuta el archivo principal del proyecto que contiene la clase `Inventario` y `Producto` para ver los resultados.
4. Modifica los datos o agrega nuevos productos al inventario según lo necesites.

## Tareas adicionales (opcional):

1. Implementar un sistema de descuentos para algunos productos.
2. Implementar una opción para agregar productos nuevos al inventario.
3. Crear un reporte del inventario mostrando productos ordenados por valor total en inventario.

## Contacto

Si tienes preguntas sobre este proyecto o sugerencias, no dudes en contactarme a través de GitHub.

¡Gracias por revisar este proyecto!

## Instrucciones para Ejecutar:

1. Clona este repositorio:

   git clone https://github.com/Portalo-Official/Python100proyectos.git

2. Navega al directorio del proyecto:

   cd yourPath/Python100proyectos/05-gestion-inventario

3. Ejecuta el script principal:

   python 05gestion_inventario.py
