# LogiPack - Sistema de Gestión de Logística y Mensajería

Este proyecto es una aplicación web desarrollada para **LogiPack**, una empresa de logística especializada en la entrega de paquetes a nivel nacional. El sistema automatiza y optimiza las tareas de gestión eficiente de entregas.

## 📦 Características Principales
La aplicación permite la gestión de los siguientes aspectos operativos:

1. **Recepción de Pedidos:** Registro de paquetes por parte de los despachantes (con detalles del destinatario, peso, sucursal, fecha y hora de recepción).
2. **Transporte de Paquetes:** Gestión de traslados de paquetes entre distintas sucursales. Registro de salida y llegada de los transportes.
3. **Gestión de Repartidores:** Asignación de paquetes a repartidores de una sucursal específica.
4. **Entrega de Paquetes:** Registro de entrega al destinatario final por parte del repartidor, o registro de las causas en caso de no poder concretar la entrega.

## 🛠️ Tecnologías Utilizadas
- **Python 3**
- **Flask** (Framework Web)
- **SQLAlchemy** (ORM para la gestión de base de datos)
- **SQLite** (Base de datos relacional)
- **HTML/CSS** (Interfaz web)

## 🚀 Cómo ejecutar el proyecto

1. Asegúrate de tener Python instalado y la librería Flask (`pip install flask flask-sqlalchemy`).
2. Abre una terminal y ubícate en la carpeta del proyecto.
3. Ejecuta el archivo principal:
   ```bash
   python App.py
   ```
4. Abre tu navegador web e ingresa a `http://127.0.0.1:5000/`.

## 👥 Usuarios del Sistema
El sistema cuenta con interfaces pensadas para dos perfiles:
- **Despachantes:** Encargados de recibir paquetes, gestionar transportes y asignar paquetes a repartidores.
- **Repartidores:** Encargados de registrar las entregas a los clientes finales.
