# 📘 Gestor Inteligente de Estudio

## 🎯 Objetivo del proyecto
Crear una aplicación en Python con interfaz gráfica que ayude al usuario a decidir qué estudiar, basándose en su historial, dificultad percibida y tiempo sin repaso.

No es una agenda.
Es un sistema de apoyo a decisiones.

---

## 🧠 Conceptos principales

### 📌 Tema
Representa una unidad de estudio.

**Información que contiene:**
- Nombre del tema
- Materia o categoría
- Nivel de dificultad percibida
- Tiempo total estudiado
- Fecha del último estudio
- Estado actual (activo, olvidado, dominado)

**Responsabilidades:**
- Actualizar su propio historial
- Calcular su nivel de prioridad
- Decidir si necesita repaso

---

### 📌 Sesión de estudio
Representa un evento concreto de estudio.

**Información que contiene:**
- Tema asociado
- Duración
- Fecha
- Observaciones (opcional)

**Responsabilidades:**
- Modificar los datos del tema
- Servir como registro histórico

---

### 📌 Motor de prioridad
Es la inteligencia del sistema.

**Factores que analiza:**
- Dificultad del tema
- Días sin estudiar
- Tiempo total invertido
- Frecuencia de repaso

**Decisiones que toma:**
- Ordenar temas por urgencia
- Detectar temas evitados
- Recomendar acciones

---

## 🪟 Interfaz gráfica (Tkinter)

### Ventana principal
**Muestra:**
- Lista de temas
- Prioridad visual (colores u orden)
- Estado general del estudio

**Permite:**
- Seleccionar un tema
- Acceder a acciones principales

---

### Ventana de registro
**Permite:**
- Agregar nuevos temas
- Registrar sesiones de estudio
- Ajustar dificultad percibida

---

### Ventana de análisis (futuro)
**Muestra:**
- Resúmenes
- Tendencias
- Alertas de temas descuidados

---

## 🗂️ Gestión de datos

### Almacenamiento
- Persistencia local
- Formato simple y legible

**Responsabilidades:**
- Guardar el estado completo del sistema
- Recuperar datos al iniciar la aplicación
- Evitar pérdida de información

---

## 🔄 Flujo general del sistema
1. El usuario abre la aplicación
2. El sistema carga los datos guardados
3. Se calculan prioridades
4. Se muestran sugerencias visuales
5. El usuario registra una sesión de estudio
6. El sistema se actualiza
7. Los datos se guardan automáticamente

---

## 🧪 Posibles mejoras futuras
- Estadísticas visuales
- Filtros por materia
- Sistema de metas
- Exportación de datos
- Notificaciones

---

## 🧭 Principios del proyecto
- Primero la lógica, luego la interfaz
- Una responsabilidad por componente
- Decisiones explícitas
- Código legible antes que código corto
