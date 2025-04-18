##############################################################################
# Importaciones
##############################################################################

from sqlmodel import Session, select
from database import Venta, DetalleVenta, Cliente, HistorialDescuento, engine
from sqlalchemy import func, between

##############################################################################
# Clase modelo de ventas
##############################################################################

class ModeloVentas:

    ''' La clase modelo de ventas contiene los metodos necesarios para
        interactuar con la base de datos en lo que respecta al modulo de 
        Ventas de la aplicacion.
    '''

    ##########################################################################
    # Metodos
    ##########################################################################

    @staticmethod
    def nueva_venta( 
        fecha: str, 
        cliente: int, 
        monto_total: float, 
        descuento_miembro: float,
        productos: dict
    ):
        with Session(engine) as sesion:
            # Creación de instancia en Venta
            venta = Venta(
                fecha=fecha,
                cliente_id=cliente,
                monto_total=monto_total,
                descuento_miembro=descuento_miembro
            )
            sesion.add(venta)
            sesion.commit()
            sesion.refresh(venta)

            # Creación del detalle de venta
            for prod, cant in productos.items():
                detalleventa = DetalleVenta(
                    nro_venta=venta.nro_venta,
                    codigo_producto=prod,
                    cantidad=cant
                )
                sesion.add(detalleventa)
            sesion.commit()


    @staticmethod
    def consulta_ventas(fecha_inicio: str, fecha_final: str):

        ''' Metodo que recopila la informacion de ventas entre dos fechas
            especificadas 'fecha_inicio' y 'fecha_final'.

            :param str fecha_inicio: Fecha inicial de filtrado.
            :param str fecha_final: Fecha final de filtrado.
            :return: Lista con ventas entre dos fechas determinadas.
            :rtype: list

        '''

        with Session(engine) as sesion:
            resultados = sesion.exec(
                select(Venta)
                .where(between(Venta.fecha, fecha_inicio, fecha_final))
                .order_by(Venta.nro_venta)
            ).all()

            return resultados


    @staticmethod
    def eliminar_venta(nro_venta: int):

        ''' Metodo que elimina una venta determinada de la base de datos,
            tomando como parametro 'nro_venta'.
            :param int nro_venta: Numero de venta a eliminar.
        '''
        with Session(engine) as sesion:
            venta_eliminar = sesion.exec(
                select(Venta).where(Venta.nro_venta == nro_venta)
            ).one()

            sesion.delete(venta_eliminar)
            sesion.commit()


    @staticmethod
    def registrar_cliente(nombre: str, dni: int, tel: str, email: str):
        
        ''' Metodo utilizado para registrar nuevos clientes en la base de
            datos.

            :param str nombre: Nombre del nuevo miembro.
            :param int dni: Numero de documento del miembro.
            :param str tel: Numero de telefono del miembro (eg: 351-4567545)
            :param str email: Correo electronico del miembro.
        '''
        with Session(engine) as sesion:
            nuevo_cliente = Cliente(
                documento=dni,
                nombre=nombre,
                telefono=tel,
                email=email
            )
            sesion.add(nuevo_cliente)
            sesion.commit()


    @staticmethod
    def obtener_cliente(dni: int):
        
        ''' Metodo utilizado para obtener informacion de un cliente utilizando
            su numero de documento 'dni'.

            :param int dni: Numero de documento del cliente.
            :return: Devuelve cliente.
            :rtype: Object Cliente
        '''
        with Session(engine) as sesion:
            cliente_consultado = sesion.exec(
                select(Cliente).where(Cliente.documento == dni)
            ).one()

            return cliente_consultado


    @staticmethod
    def obtener_detalle_ventas(nro_venta: int):

        ''' Metodo utilizado para obtener el detalle de productos y cantidad
            vendida en una determinada venta 'nro_venta'.

            :param int nro_venta: Numero de venta a consultar.
            :return: Lista de tuplas que contienen numero de producto
                y cantidades
            :rtype: list
        '''

        with Session(engine) as sesion:
            venta = sesion.exec(
                select(Venta).where(Venta.nro_venta == nro_venta)
            ).one()

            detalle = []
            objetos_detalleventa = venta.link_productos
            for obj in objetos_detalleventa:
                detalle.append((obj.codigo_producto, obj.cantidad))
            
            return detalle


    @staticmethod
    def descuento_y_montomin():

        ''' Metodo utilizado para obtener el ultimo descuento agregado,
            siempre que se modifique el valor de descuento aplicado se
            creara un nuevo registro. Este metodo obtiene ese ultimo
            valor.

            :return: Tupla que contiene el ultimo descuento aplicado
            y el respectivo monto minimo para aplicar descuento.
            :rtype: tuple
        '''
        with Session(engine) as sesion:
            last_id_desc = sesion.exec(
                select(func.max(HistorialDescuento.id))
            ).one()

            desc_aplicar = sesion.exec(
                select(HistorialDescuento)
                .where(HistorialDescuento.id == last_id_desc)
            ).one()

            return (desc_aplicar.descuento, desc_aplicar.monto_minimo)


    @staticmethod
    def nuevo_descuento_monto(descuento: float, monto: int):

        ''' Metodo que introduce un nuevo registro en la tabla de
            HistorialDescuentos.

            :param float descuento: Descuento a aplicar a ventas de miembros.
            :param int monto: Monto minimo a partir del cual se aplica 
                descuento
        '''
        with Session(engine) as sesion:
            registro_descuento = HistorialDescuento(
                descuento=descuento,
                monto_minimo=monto
            )

            sesion.add(registro_descuento)
            sesion.commit()


if __name__ == "__main__":
    
    #ModeloVentas.nuevo_descuento_monto(0.45, 3000000)

    consulta = ModeloVentas.consulta_ventas("16-04-2025", "25-05-2026")
    print(consulta)
    
    
    #ModeloVentas.eliminar_venta(3)
    
    #fecha = "20-05-2025"
    #cliente = 0
    #monto_total = 2000000
    #descuento_miembro = 0.2
    #productos = {
    #            1:1,
    #            }
    #
    #ModeloVentas.nueva_venta(fecha, cliente, monto_total, descuento_miembro, productos)