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

  ##capturas
  Menu principal
  <img width="370" height="267" alt="image" src="https://github.com/user-attachments/assets/1b07de62-5a61-404f-8c4a-3a3988974518" />

  
  Ver inventario
  <img width="408" height="181" alt="image" src="https://github.com/user-attachments/assets/33f3f583-fa8f-4dce-b005-ab96f7062f8f" />

  Editar producto
  <img width="379" height="141" alt="image" src="https://github.com/user-attachments/assets/534b6aea-36df-4004-9c8a-7777afd75a45" />
