class Producto():

    def __init__ (self, nombre, cantidad_disponible=0, precio_unidad=0):
        self._nombre = nombre
        self._cantidad_disponible = cantidad_disponible
        self._precio_unidad= precio_unidad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = value

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self, value):
        self._cantidad_disponible = value

    @property
    def precio_unidad(self):
        return self._precio_unidad

    @precio_unidad.setter
    def precio_unidad(self, value):
        self._precio_unidad = value
