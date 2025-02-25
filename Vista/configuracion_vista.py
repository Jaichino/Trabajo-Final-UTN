
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

