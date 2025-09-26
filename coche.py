# =========================
# Clase base Vehiculo
# =========================
class Vehiculo:
  #Se define la clase Vehiculo, que servirá como modelo general para todos los vehículos.
    """
    Clase base que representa un vehículo genérico.
    
    Atributos privados:
        __marca (str): Marca del vehículo.
        __velocidad (int): Velocidad actual en km/h. 
    """
   #Esto es un docstring (documentación interna): explica para qué sirve la clase y sus atributos principales.
    def __init__(self, marca: str): #Constructor de la clase Vehiculo.
       #Recibe la marca del vehículo como parámetro.
       #Se ejecuta al crear un objeto.
        """
        Inicializa un vehículo con su marca y velocidad en 0.
        
        Args:
            marca (str): Marca del vehículo.
        """
      #Se inicializan los atributos privados:
        self.__marca = marca
        self.__velocidad = 0
      #__velocidad: siempre inicia en 0 km/h.
  
   #Método para aumentar la velocidad en cierta cantidad (incremento).  
    def acelerar(self, incremento: int):
        """
        Incrementa la velocidad del vehículo.
        
        Args:
            incremento (int): Cantidad en km/h a aumentar.
        """
        self.__velocidad += incremento
      #Suma el incremento a la velocidad actual.

  #Método para disminuir la velocidad en cierta cantidad (decremento).
    def frenar(self, decremento: int):
        """
        Reduce la velocidad del vehículo, nunca menor a 0.
        
        Args:
            decremento (int): Cantidad en km/h a disminuir.
        """
      #Resta el decremento.
        self.__velocidad -= decremento
        if self.__velocidad < 0:
            self.__velocidad = 0
          #Si el resultado es negativo, se corrige y se ajusta a 0 (nunca hay velocidad negativa).

  #Muestra en pantalla la marca y velocidad del vehículo.
    def mostrar_datos(self):
        """
        Muestra los datos básicos del vehículo.
        (Este método se sobrescribe en las subclases).
        """
        print(f"Marca: {self.__marca} | Velocidad: {self.__velocidad} km/h")
      #Este método está pensado para ser sobrescrito en las subclases.

  #Método definido pero no implementado.
    def consumo_combustible(self, distancia: float):
        """
        Calcula el consumo de combustible.
        (Se implementa de manera distinta en cada subclase).
        
        Args:
            distancia (float): Distancia recorrida en km.
        
        Returns:
            float: Consumo en litros.
        """
        raise NotImplementedError("Este método debe ser implementado en la subclase")
      #bliga a que las subclases (Coche, Moto) tengan que programar su propia versión de consumo_combustible().
    
    # Métodos getters para acceder a atributos privados
    def get_marca(self) -> str:
        """Devuelve la marca del vehículo."""
        return self.__marca
      #Método getter que devuelve la marca del vehículo (encapsulamiento).
  
  #Método getter que devuelve la velocidad del vehículo.  
    def get_velocidad(self) -> int:
        """Devuelve la velocidad actual del vehículo."""
        return self.__velocidad


# =========================
# Subclase Coche
# =========================
#Se crea la clase Coche, que hereda de Vehiculo.
class Coche(Vehiculo):
    """
    Clase que representa un coche.
    Hereda de Vehiculo.
    
    Atributos adicionales:
        puertas (int): Número de puertas del coche.
        consumo_por_km (float): Consumo promedio en litros por km.
    """
    #Llama al constructor de Vehiculo (super().__init__(marca)).
    def __init__(self, marca: str, puertas: int = 4, consumo_por_km: float = 0.08):
        """
        Inicializa un coche con marca, número de puertas y consumo por km.
        
        Args:
            marca (str): Marca del coche.
            puertas (int): Número de puertas (por defecto 4).
            consumo_por_km (float): Consumo promedio litros/km.
        """
        super().__init__(marca)
        self.puertas = puertas
        self.consumo_por_km = consumo_por_km
      #Añade atributos propios: puerta: numero de puertas. Consumo_por_km: litros de combustible empleado por kilometros.

  #Sobrescribe el método mostrar_datos() para mostrar más información (puertas).
    def mostrar_datos(self):
        """Muestra los datos específicos de un coche."""
        print(f"[Coche] Marca: {self.get_marca()} | Velocidad: {self.get_velocidad()} km/h | Puertas: {self.puertas}")
   
  #Implementa el método consumo_combustible():
    def consumo_combustible(self, distancia: float) -> float:
        """
        Calcula el consumo de combustible para un coche.
        
        Args:
            distancia (float): Distancia recorrida en km.
        
        Returns:
            float: Consumo en litros.
        """
        return distancia * self.consumo_por_km
      #Multiplica la distancia recorrida × consumo por km.


# =========================
# Subclase Moto
# =========================
#Clase Moto, que también hereda de Vehiculo.
class Moto(Vehiculo):
    """
    Clase que representa una moto.
    Hereda de Vehiculo.
    
    Atributos adicionales:
        tipo_casco (str): Recomendación de casco para el conductor.
        consumo_por_km (float): Consumo promedio en litros por km.
    """

  #contructor de moto:
    def __init__(self, marca: str, tipo_casco: str = "Integral", consumo_por_km: float = 0.05):
        """
        Inicializa una moto con marca, tipo de casco y consumo por km.
        
        Args:
            marca (str): Marca de la moto.
            tipo_casco (str): Tipo de casco recomendado (por defecto "Integral").
            consumo_por_km (float): Consumo promedio litros/km.
        """
        super().__init__(marca)
        self.tipo_casco = tipo_casco
        self.consumo_por_km = consumo_por_km
      #Llama al constructor de Vehiculo.
      #Añade atributos propios: tipo_casco: casco recomendado. consumo_por_km: litros por km.

  #Se sobrescribe mostrar_datos() para mostrar la información de la moto.
    def mostrar_datos(self):
        """Muestra los datos específicos de una moto."""
        print(f"[Moto] Marca: {self.get_marca()} | Velocidad: {self.get_velocidad()} km/h | Casco recomendado: {self.tipo_casco}")

  #Calculamos el consumo de combustible para la moto.
    def consumo_combustible(self, distancia: float) -> float:
        """
        Calcula el consumo de combustible para una moto.
        
        Args:
            distancia (float): Distancia recorrida en km.
        
        Returns:
            float: Consumo en litros.
        """
        return distancia * self.consumo_por_km


# =========================
# Ejecución de prueba con información real
# =========================

#Bloque especial: solo se ejecuta si el archivo es ejecutado directamente (no si se importa como módulo).
if __name__ == "__main__":
    # Mustang Shelby clásico
  #Se crea un coche Mustang (2 puertas, consumo 0.12).
  #Lo aceleramos a 200 km/h. Se muestran sus datos. se calcula el comsumo en 100km.
    mustang_shelby = Coche("Ford Mustang Shelby 1967", puertas=2, consumo_por_km=0.12)
    mustang_shelby.acelerar(200)
    mustang_shelby.mostrar_datos()
    print(f"Consumo en 100 km: {mustang_shelby.consumo_combustible(100)} L\n")
    
    # Chevrolet Camaro clásico
  #Creamos un Camaro 1969 (2 puertas, consumo 0.11).
    camaro = Coche("Chevrolet Camaro 1969", puertas=2, consumo_por_km=0.11)
    camaro.acelerar(180)
    camaro.frenar(20)
    camaro.mostrar_datos()
    print(f"Consumo en 100 km: {camaro.consumo_combustible(100)} L\n")
  #Se acelera a 180 km/h. Se frena 20 → queda en 160 km/h. Se muestran los datos. Se calcula consumo en 100 km.
    
    # Harley-Davidson Iron 883
  #Se crea una moto Harley-Davidson.
    harley_iron = Moto("Harley-Davidson Iron 883", tipo_casco="Integral", consumo_por_km=0.05)
    harley_iron.acelerar(150)
    harley_iron.frenar(30)
    harley_iron.mostrar_datos()
    print(f"Consumo en 100 km: {harley_iron.consumo_combustible(100)} L")
  #Se acelera a 150 km/h. Se frena 30 → queda en 120 km/h. Se muestran los datos. Se calcula consumo en 100 km.
