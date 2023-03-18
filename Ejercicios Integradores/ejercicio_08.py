from ejercicio_06 import Persona
from ejercicio_07 import Cuenta
from exepciones import PersonaDatoInvalidoError, CuentaJovenTitularInvalidoError


class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def mostrar(self):
        print(
            f"<-CUENTA JOVEN-> \n- Titular {self.titular.mostrar()}, \n- Cantidad: {self.cantidad}, \n- Bonificación: {self.bonificacion}%")

    def es_titular_valido(self):
        return self.titular.edad < 25 and self.titular.es_mayor_de_edad()

    def retirar(self, cantidad):
        if not self.es_titular_valido():
            mensaje = f"El titular {self.titular} no puede retirar dinero porque es inválido"
            print(mensaje)
            raise excepciones.CuentaJovenTitularInvalidoError(
                mensaje)
        elif cantidad > 0:
            super().retirar(cantidad)


esteban = Persona("Esteban", 20, 29950189)
cuenta_esteban = CuentaJoven(esteban, 50.5, 25)
cuenta_esteban.ingresar(107.2)
cuenta_esteban.retirar(25)
cuenta_esteban.mostrar()
