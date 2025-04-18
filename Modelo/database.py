##############################################################################
# Importaciones
##############################################################################

from sqlmodel import SQLModel, Field, Relationship, create_engine, text
from sqlmodel import Session
from sqlalchemy import event

##############################################################################
# Creación del modelo de base de datos
##############################################################################


class Cliente(SQLModel, table=True):
    documento : int | None = Field(default=None, primary_key=True)
    nombre: str
    telefono: str
    email: str

    ventas: list["Venta"] = Relationship(back_populates="cliente",
                                        cascade_delete=True)


class HistorialDescuento(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    descuento: float
    monto_minimo: float

class DetalleVenta(SQLModel, table=True):
    nro_venta: int | None = Field(
                                    default=None,
                                    foreign_key="venta.nro_venta",
                                    primary_key=True,
                                    ondelete="CASCADE"
                                )
    
    codigo_producto: int | None = Field(
                                    default=None,
                                    foreign_key="producto.codigo_producto",
                                    primary_key=True,
                                    ondelete="CASCADE"
                                    )
    cantidad: int

    venta: list["Venta"] = Relationship(back_populates="link_productos")
    producto: list["Producto"] = Relationship(back_populates="link_ventas")

class Producto(SQLModel, table=True):
    codigo_producto: int | None = Field(default=None, primary_key=True)
    descripcion: str
    precio_unitario: float
    stock: int
    estado: bool = True

    link_ventas: list[DetalleVenta] = Relationship(back_populates="producto",
                                                    cascade_delete=True)

class Venta(SQLModel, table=True):
    nro_venta: int | None = Field(default=None, primary_key=True)
    fecha: str
    monto_total: float
    descuento_miembro: float = 0

    cliente_id: int = Field(default=0, 
                        foreign_key="cliente.documento",
                        ondelete="CASCADE")
    
    cliente: "Cliente" = Relationship(back_populates="ventas")
    
    link_productos: list[DetalleVenta] = Relationship(back_populates="venta",
                                                        cascade_delete=True)


bd_name = "market_sistem.db"
bd_url = f"sqlite:///{bd_name}"
engine = create_engine(
    bd_url, 
    echo=True
)

# Creación de base de datos 
def create_bd():
    SQLModel.metadata.create_all(engine)
    with engine.connect() as connection:
        connection.execute(text("PRAGMA foreign_keys=ON"))

##############################################################################
##############################################################################
# SOLO PARA SQLite, PARA ACTIVAR LAS FOREIGN KEYS EN TODAS LAS SESIONES
@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
##############################################################################
##############################################################################

# Creación de usuario inicial (Usuario no registrado)
def creacion_usuario_inicial():
    with Session(engine) as sesion:
        usuario_cero = Cliente(
            documento=0,
            nombre="Usuario no registrado",
            telefono="-",
            email="-"
        )
        sesion.add(usuario_cero)
        sesion.commit()

##############################################################################
##############################################################################
# Ejecutar solo si no se ha creado la base de datos anteriormente

#if __name__ == '__main__':
#    create_bd()
#    creacion_usuario_inicial()

##############################################################################
##############################################################################
