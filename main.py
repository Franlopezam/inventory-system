import sqlite3

DB = "inventario.db"

def conectar():
    return sqlite3.connect(DB)

def preparar():
    with conectar() as db:
        db.execute('CREATE TABLE IF NOT EXISTS productos (\n            id INTEGER PRIMARY KEY AUTOINCREMENT,\n            nombre TEXT NOT NULL,\n            precio REAL NOT NULL,\n            cantidad INTEGER NOT NULL DEFAULT 0\n        )')

def agregar(nombre, precio, cantidad):
    with conectar() as db:
        db.execute("INSERT INTO productos(nombre,precio,cantidad) VALUES(?,?,?)",
                   (nombre, precio, cantidad))

def listar():
    with conectar() as db:
        return db.execute("SELECT id,nombre,precio,cantidad FROM productos ORDER BY id").fetchall()

def eliminar(producto_id):
    with conectar() as db:
        db.execute("DELETE FROM productos WHERE id=?", (producto_id,))

def menu():
    preparar()
    while True:
        print("\n--- INVENTARIO ---")
        print("1. Agregar")
        print("2. Listar")
        print("3. Eliminar")
        print("4. Salir")
        op=input("> ").strip()
        if op=="1":
            nombre=input("Nombre: ").strip()
            precio=float(input("Precio: "))
            cantidad=int(input("Cantidad: "))
            agregar(nombre,precio,cantidad)
        elif op=="2":
            for p in listar():
                print(f"#{p[0]} {p[1]} | ${p[2]:.2f} | stock: {p[3]}")
        elif op=="3":
            eliminar(int(input("ID: ")))
        elif op=="4":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
