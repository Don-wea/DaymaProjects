import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()
        
    def create_tables(self):

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Producto (
            id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio INTEGER NOT NULL,
            categoria TEXT,
            descripcion TEXT
        )''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inventario (
            id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
            cantidad INTEGER NOT NULL,
            id_producto INTEGER,
            FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
        )''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Venta (
            id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
            medio VARCHAR(20) NOT NULL,
            valor_final INTEGER NOT NULL
        )''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Producto_Venta(
            id_producto INTEGER,
            id_venta INTEGER,
            cantidad INTEGER NOT NULL,
            FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
            FOREIGN KEY (id_venta) REFERENCES Venta(id_venta)
            PRIMARY KEY (id_producto, id_venta)
        )''')
        
        self.conn.commit()
        
    def insert_product(self, nombre, precio, categoria, descripcion):
        self.cursor.execute('INSERT INTO Producto(nombre, precio, categoria, descripcion) VALUES (?,?,?,?)', (nombre, precio, categoria, descripcion))
        self.conn.commit()
        
    def close(self):
        self.conn.close()
        
    
if __name__ == '__main__':
    db = Database('inventario.db')
    db.create_tables()
    nombre = 'atun'
    precio = 5
    categoria = 'pescado'
    descripcion = 'pescado rico con mercurio'
    db.insert_product(nombre, precio, categoria, descripcion)
    db.close()