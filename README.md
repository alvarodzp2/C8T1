# C8T1 - Sistema de Gestión de Pedidos e Inventario

Sistema de consola para registrar, mostrar, editar y eliminar productos y pedidos.

## Cómo ejecutar

```bash
python c8t1_gestion_pedidos.py
```

## Funcionalidades

**Inventario**
- Registrar producto
- Ver inventario
- Editar producto
- Eliminar producto

**Pedidos**
- Registrar pedido
- Ver pedidos
- Editar pedido
- Eliminar pedido

## Estructura de datos

Se usan listas paralelas (arreglos unidimensionales). El índice `i` representa el mismo registro en todas las listas.

```
inv_ids / inv_nombres / inv_precios / inv_cantidades
ped_ids / ped_clientes / ped_productos / ped_cantidades / ped_estados
```

## Notas

- Al registrar un pedido se descuenta el stock automáticamente.
- Al eliminar un pedido pendiente se devuelve el stock al inventario.
