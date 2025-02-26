from PIL import Image, ImageTk

class ConfiguracionVista:
    
    ''' 
    En esta clase se definen todas las propiedades que se encargaran de
    configurar las vistas, a modo de facilitar los cambios a medida que 
    la aplicacion crece
    '''
    
    # Resolucion de pantalla (coordenada en x e y)
    res_x = 1920
    res_y = 1080

    # Fuentes utilizadas
    fuentes =   {'titulo': ('Arial', 20, 'bold'),
                'boton': ('Arial', 14, 'bold'),
                'texto': ('Arial', 14),
                'texto-bold': ('Arial',14,'bold'),
                'treeview-heading':('Arial',12,'bold'),
                'treeview':('Arial',10)
                }
    
    # Colores utilizados
    colores = {'background': '#719ef2',
                'divisor':'#126fbb'}


    # Imagenes
    imagenes = {

        'carrito':'imagenes/carrito.png',
        'eliminar':'imagenes/eliminar.png',
        'filtrar':'imagenes/filtrar.png',
        'guardar':'imagenes/guardar.png',
        'astock':'imagenes/ingresar_stock.png',
        'inventario':'imagenes/inventario.png',
        'listo':'imagenes/listo.png',
        'ventas':'imagenes/ventas.png',
        'sinstock':'imagenes/sin_stock.png',
        'editar':'imagenes/modificar.png',
        'buscar':'imagenes/buscar.png'

    }

    @staticmethod
    def formato_imagen(imagen,tipo=None):
        im = Image.open(imagen)

        if tipo is not None:
            im_res = im.resize((50,50))
        else:
            im_res = im.resize((30,30))

        im_tk = ImageTk.PhotoImage(im_res)
        return im_tk

