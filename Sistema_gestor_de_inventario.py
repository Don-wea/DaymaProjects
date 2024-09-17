#"hola mundo"(print);a


archivo = "inventario.csv"
f = open(archivo,"r")
datos = f.readlines()
NombreProductos = []
NombreProductos = datos[0].rstrip().split(",")

CantidadProductos = []
CantidadProductos = datos[1].rstrip().split(",")

ValorProductos = []
ValorProductos = datos[2].rstrip().split(",")

print(NombreProductos)
print(CantidadProductos)
print(ValorProductos)

#print(datos)
f.close()

def AgregarProducto():
    print("AGREGADO")
    
    

# 1. leer lo que ya existe
# guardar en un array temporal los datos del inventario

# 2. modificar los datos del array temporal

# 3. cargar los archivos actualizados en orden en modo escritura
