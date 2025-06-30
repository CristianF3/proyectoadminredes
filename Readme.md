
# 🧩 Microservicios con Docker Compose

Este proyecto contiene una arquitectura básica de microservicios utilizando Docker Compose. Incluye:

- `user-service`: Servicio de usuarios (FastAPI)
- `task-service`: Servicio de tareas (FastAPI)
- `nginx-proxy-manager`: Proxy reverso con interfaz web 

---

## 🚀 Requisitos

Antes de comenzar, asegúrate de tener instalado:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 📦 Clonar y ejecutar

1. Clona este repositorio:

```bash
git clone https://github.com/CristianF3/proyectoadminredes.git
cd proyectoadminredes
cd MicroserviciosU2-3
```

2. Construye y levanta los servicios:

```bash
docker-compose up --build
```

---

## 🔐 Acceso a Nginx Proxy Manager

Una vez levantado el entorno, accede a la interfaz de administración de **Nginx Proxy Manager** en:

```
http://localhost:81
```

> Si estás desplegando en un servidor remoto (como Google Cloud), usa la IP pública de tu instancia:

```
http://<tu-ip-pública>:81
```

**Credenciales por defecto:**
- **Correo:** `admin@example.com`
- **Contraseña:** `changeme`

Al iniciar sesión por primera vez, se te pedirá que cambies estos datos.

---

## 🌐 Conectar tu dominio

1. Apunta tu dominio o subdominio (ej: `midominio.com`) a la IP pública de tu servidor.
2. Entra al panel de Nginx Proxy Manager.
3. Ve a **"Proxy Hosts" > "Add Proxy Host"**:
   - **Domain Names**: `midominio.com`
   - **Forward Hostname/IP**: `miip`
   - **Forward Port**: `81`
4. Agregar Custom locations
   - **location**:
    `/admmin`
   - **Forward Hostname/IP**: `miip`
   - **Forward Port**: `81`
   - **location**:
    `/api/tasks/`
   - **Forward Hostname/IP**: `miip`
   - **Forward Port**: `5001`
   - **location**:
    `user-service`
   - **Forward Hostname/IP**: `miip`
   - **Forward Port**: `5000`
---

## 🧹 Detener los servicios

```bash
docker-compose down
```

Para borrar también los volúmenes:

```bash
docker-compose down -v
```

---

