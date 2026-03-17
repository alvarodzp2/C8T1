#librerias
import os

# --- Inventario ---
inv_ids        = []   # str
inv_nombres    = []   # str
inv_precios    = []   # float
inv_cantidades = []   # int

# --- Pedidos ---
ped_ids        = []   # str
ped_clientes   = []   # str
ped_productos  = []   # str  (id de producto)
ped_cantidades = []   # int
ped_estados    = []   # str: "pendiente" | "enviado" | "cancelado"
#funciones del inventario
# registrar un nuevo producto en el inventario
def registrar_producto(pid: str, nombre: str, precio: float, cantidad: int) -> None:
    if pid in inv_ids:
        print(f"  El ID '{pid}' ya existe en inventario.")
        return
    inv_ids.append(pid)
    inv_nombres.append(nombre)
    inv_precios.append(precio)
    inv_cantidades.append(cantidad)
    print(f"  Producto '{nombre}' registrado con ID {pid}.")

# mostrar todos los productos del inventario
def mostrar_inventario() -> None:
    if not inv_ids:
        print("  Inventario vacio.")
        return
    print(f"\n  {'ID':<8} {'Nombre':<22} {'Precio':>8} {'Stock':>6}")
    print("  " + "-" * 48)
    for i in range(len(inv_ids)):
        print(f"  {inv_ids[i]:<8} {inv_nombres[i]:<22} "
              f"{inv_precios[i]:>8.2f} {inv_cantidades[i]:>6}")

# editar nombre, precio o cantidad de un producto
def editar_producto(pid: str, nombre: str, precio: float, cantidad: int) -> None:
    if pid not in inv_ids:
        print(f"  ID '{pid}' no encontrado.")
        return
    i = inv_ids.index(pid)
    inv_nombres[i]    = nombre
    inv_precios[i]    = precio
    inv_cantidades[i] = cantidad
    print(f"  Producto {pid} actualizado.")

# eliminar un producto del inventario
def eliminar_producto(pid: str) -> None:
    if pid not in inv_ids:
        print(f"  ID '{pid}' no encontrado.")
        return
    i = inv_ids.index(pid)
    inv_ids.pop(i)
    inv_nombres.pop(i)
    inv_precios.pop(i)
    inv_cantidades.pop(i)
    print(f"  Producto {pid} eliminado.")

#funciones apra pedidos
# registrar un nuevo pedido
def registrar_pedido(pid: str, cliente: str, id_producto: str, cantidad: int) -> None:
    if pid in ped_ids:
        print(f"  El ID de pedido '{pid}' ya existe.")
        return
    if id_producto not in inv_ids:
        print(f"  Producto '{id_producto}' no existe en inventario.")
        return
    idx = inv_ids.index(id_producto)
    if inv_cantidades[idx] < cantidad:
        print(f"  Stock insuficiente. Disponible: {inv_cantidades[idx]}")
        return
    # descuenta del inventario al registrar el pedido
    inv_cantidades[idx] -= cantidad
    ped_ids.append(pid)
    ped_clientes.append(cliente)
    ped_productos.append(id_producto)
    ped_cantidades.append(cantidad)
    ped_estados.append("pendiente")
    print(f"  Pedido {pid} registrado para {cliente}.")


# mostrar todos los pedidos
def mostrar_pedidos() -> None:
    if not ped_ids:
        print("  Sin pedidos registrados.")
        return
    print(f"\n  {'ID':<8} {'Cliente':<18} {'Producto':<10} {'Cant':>5} {'Estado':<12}")
    print("  " + "-" * 58)
    for i in range(len(ped_ids)):
        print(f"  {ped_ids[i]:<8} {ped_clientes[i]:<18} "
              f"{ped_productos[i]:<10} {ped_cantidades[i]:>5} {ped_estados[i]:<12}")


# editar cliente o estado de un pedido
def editar_pedido(pid: str, cliente: str, estado: str) -> None:
    if pid not in ped_ids:
        print(f"  Pedido '{pid}' no encontrado.")
        return
    estados_validos = ("pendiente", "enviado", "cancelado")
    if estado not in estados_validos:
        print(f"  Estado invalido. Opciones: {estados_validos}")
        return
    i = ped_ids.index(pid)
    ped_clientes[i] = cliente
    ped_estados[i]  = estado
    print(f"  Pedido {pid} actualizado.")


# eliminar un pedido (devuelve stock si estaba pendiente)
def eliminar_pedido(pid: str) -> None:
    if pid not in ped_ids:
        print(f"  Pedido '{pid}' no encontrado.")
        return
    i = ped_ids.index(pid)
    # si el pedido estaba pendiente, devuelve las unidades al inventario
    if ped_estados[i] == "pendiente" and ped_productos[i] in inv_ids:
        idx = inv_ids.index(ped_productos[i])
        inv_cantidades[idx] += ped_cantidades[i]
    ped_ids.pop(i)
    ped_clientes.pop(i)
    ped_productos.pop(i)
    ped_cantidades.pop(i)
    ped_estados.pop(i)
    print(f"  Pedido {pid} eliminado.")

#funciones para pedir datos de entrada

def pedir_float(msg: str, minimo: float = 0.0) -> float:
    while True:
        try:
            v = float(input(msg))
            if v >= minimo: return v
            print(f"  Minimo: {minimo}")
        except: print("  Valor invalido.")

def pedir_int(msg: str, minimo: int = 0) -> int:
    while True:
        try:
            v = int(input(msg))
            if v >= minimo: return v
            print(f"  Minimo: {minimo}")
        except: print("  Valor invalido.")


#fucniones dle menu principal
def flujo_registrar_producto() -> None:
    print("\n  REGISTRAR PRODUCTO")
    pid      = input("  ID del producto: ").strip().upper()
    nombre   = input("  Nombre: ").strip()
    precio   = pedir_float("  Precio: ", 0.01)
    cantidad = pedir_int("  Cantidad en stock: ", 0)
    registrar_producto(pid, nombre, precio, cantidad)

def flujo_editar_producto() -> None:
    mostrar_inventario()
    print("\n  EDITAR PRODUCTO")
    pid      = input("  ID a editar: ").strip().upper()
    nombre   = input("  Nuevo nombre: ").strip()
    precio   = pedir_float("  Nuevo precio: ", 0.01)
    cantidad = pedir_int("  Nueva cantidad: ", 0)
    editar_producto(pid, nombre, precio, cantidad)

def flujo_eliminar_producto() -> None:
    mostrar_inventario()
    print("\n  ELIMINAR PRODUCTO")
    pid = input("  ID a eliminar: ").strip().upper()
    eliminar_producto(pid)

def flujo_registrar_pedido() -> None:
    mostrar_inventario()
    print("\n  REGISTRAR PEDIDO")
    pid        = input("  ID del pedido: ").strip().upper()
    cliente    = input("  Nombre del cliente: ").strip()
    id_prod    = input("  ID del producto: ").strip().upper()
    cantidad   = pedir_int("  Cantidad: ", 1)
    registrar_pedido(pid, cliente, id_prod, cantidad)

def flujo_editar_pedido() -> None:
    mostrar_pedidos()
    print("\n  EDITAR PEDIDO")
    pid     = input("  ID del pedido: ").strip().upper()
    cliente = input("  Nuevo cliente: ").strip()
    estado  = input("  Nuevo estado (pendiente/enviado/cancelado): ").strip().lower()
    editar_pedido(pid, cliente, estado)

def flujo_eliminar_pedido() -> None:
    mostrar_pedidos()
    print("\n  ELIMINAR PEDIDO")
    pid = input("  ID del pedido: ").strip().upper()
    eliminar_pedido(pid)

#menu para usuario

def limpiar() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def menu() -> None:
    while True:
        limpiar()
        print("=" * 46)
        print("  SISTEMA DE GESTION DE PEDIDOS E INVENTARIO")
        print("=" * 46)
        print("  INVENTARIO")
        print("  1. Ver inventario")
        print("  2. Registrar producto")
        print("  3. Editar producto")
        print("  4. Eliminar producto")
        print("  PEDIDOS")
        print("  5. Ver pedidos")
        print("  6. Registrar pedido")
        print("  7. Editar pedido")
        print("  8. Eliminar pedido")
        print("  0. Salir")
        print("=" * 46)
        op = input("  Opcion: ").strip()

        if   op == "1": limpiar(); mostrar_inventario()
        elif op == "2": limpiar(); flujo_registrar_producto()
        elif op == "3": limpiar(); flujo_editar_producto()
        elif op == "4": limpiar(); flujo_eliminar_producto()
        elif op == "5": limpiar(); mostrar_pedidos()
        elif op == "6": limpiar(); flujo_registrar_pedido()
        elif op == "7": limpiar(); flujo_editar_pedido()
        elif op == "8": limpiar(); flujo_eliminar_pedido()
        elif op == "0": print("\n  Sistema cerrado."); break
        else:           print("  Opcion no valida.")

        if op != "0":
            input("\n  Presiona Enter para continuar")

#llamda al programa
if __name__ == "__main__":
    menu()