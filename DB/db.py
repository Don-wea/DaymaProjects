import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()
        
    def create_tables(self):

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Producto (
            id_producto INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio INTEGER NOT NULL,
            categoria TEXT,
            descripcion TEXT
        )''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inventario (
            id_inventario INTEGER PRIMARY KEY,
            cantidad INTEGER NOT NULL,
            id_producto INTEGER,
            FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
        )''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Venta (
            id_venta INTEGER PRIMARY KEY,
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
            FOREIGN KEY (id_venta) REFERENCES Venta(id_venta),
            PRIMARY KEY (id_producto, id_venta)
        )''')
        
        self.conn.commit()
        
    def insert_product(self, nombre, precio, categoria, descripcion):
        self.cursor.execute('INSERT INTO Producto(nombre, precio, categoria, descripcion) VALUES (?,?,?,?)', (nombre, precio, categoria, descripcion))
        self.conn.commit()
        
    def get_products(self):
        self.cursor.execute('SELECT * FROM Producto')
        return self.cursor.fetchall()
    
    def insert_inventory(self, cantidad, id_producto):
        self.cursor.execute('INSERT INTO Inventario(cantidad, id_producto) VALUES (?,?)', (cantidad, id_producto))
        self.conn.commit()
        
    def get_inventory(self):
        self.cursor.execute('SELECT * FROM Inventario')
        return self.cursor.fetchall()
    
    def insert_sale(self, fecha, medio, valor_final):
        self.cursor.execute('INSERT INTO Venta(fecha, medio, valor_final) VALUES (?,?,?)', (fecha, medio, valor_final))
        self.conn.commit()
        
    def get_sales(self):
        self.cursor.execute('SELECT * FROM Venta')
        return self.cursor.fetchall()
    
    def insert_product_sale(self, id_producto, id_venta, cantidad):
        self.cursor.execute('INSERT INTO Producto_Venta(id_producto, id_venta, cantidad) VALUES (?,?,?)', (id_producto, id_venta, cantidad))
        self.conn.commit()
        
    def get_product_sales(self):
        self.cursor.execute('SELECT * FROM Producto_Venta')
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()
        
