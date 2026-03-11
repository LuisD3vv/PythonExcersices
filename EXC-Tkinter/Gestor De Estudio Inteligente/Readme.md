# 📘 Gestor Inteligente de Estudio

## Versión Simplificada (MVP) + Roadmap de Construcción

> No es una agenda. No es un tracker. No es un planner.
> Es un **sistema de apoyo a decisiones de estudio**.

---

# 🎯 Objetivo del proyecto

Crear una aplicación en Python que ayude al usuario a decidir **qué estudiar**, basándose en reglas simples de prioridad.

No busca organizar horarios.
Busca **reducir fricción mental** y evitar la procrastinación por indecisión.

---

# 🧠 Versión mínima viable (MVP)

Esta es la versión reducida, realista y construible:

## 📌 Tema

Representa una unidad de estudio.

**Datos:**

* nombre
* dificultad (1–5)
* ultimo_estudio (fecha)
* total_tiempo (minutos)

**Responsabilidades:**

* Actualizar su historial
* Exponer datos para cálculo de prioridad

---

## 📌 Sesión de estudio

Representa un evento de estudio.

**Datos:**

* tema
* duracion
* fecha

**Responsabilidades:**

* Actualizar datos del tema
* Servir como registro histórico

---

## 🧠 Motor de prioridad (simple)

Regla inicial:

```
prioridad = dias_sin_estudiar * dificultad
```

**Factores:**

* Días sin estudiar
* Dificultad percibida

**Decisión:**

* Ordenar temas por urgencia

---

# 🪟 Interfaz mínima

Una sola ventana (Tkinter):

**Muestra:**

* Lista de temas
* Prioridad visual (orden + colores)

**Permite:**

* Agregar tema
* Registrar sesión de estudio

---

# 💾 Gestión de datos

**Persistencia local:**

Archivo único:

```
data.json
```

Estructura:

```json
{
  "temas": [],
  "sesiones": []
}
```

---

# 🧱 Arquitectura mínima

```
main.py      → arranque del sistema
models.py    → Tema, Sesion
logic.py     → cálculo de prioridad
storage.py   → guardar/cargar JSON
ui.py        → interfaz Tkinter
```

---

# 🔄 Flujo del sistema

1. Cargar datos
2. Calcular prioridades
3. Mostrar temas ordenados
4. Usuario registra sesión
5. Actualizar datos
6. Guardar automáticamente

---

# 🧪 Roadmap de construcción

## 🥉 Fase 1 — Base lógica (sin interfaz)

* CLI
* JSON
* Clases Tema y Sesion
* Cálculo de prioridad
* Registro manual

Objetivo: **funcionalidad pura**

---

## 🥈 Fase 2 — Estructura limpia

* Separación de archivos
* Arquitectura modular
* Persistencia estable

Objetivo: **ingeniería de software**

---

## 🥇 Fase 3 — Interfaz básica

* Tkinter
* Lista de temas
* Botones básicos
* Colores por prioridad

Objetivo: **usabilidad mínima**

---

## 🧠 Fase 4 — Motor inteligente

* Más factores
* Historial
* Frecuencia
* Estados

Objetivo: **sistema de decisión real**

---

## 📊 Fase 5 — Análisis

* Resúmenes
* Tendencias
* Alertas
* Visualización

Objetivo: **sistema de autogestión del aprendizaje**

---

# 🧭 Principios del proyecto

* Primero lógica, luego interfaz
* Una responsabilidad por módulo
* Código legible > código corto
* Sistemas > scripts
* Pensamiento estructural > copiar código

---

# 🗿 Filosofía del proyecto

Esto no es un ejercicio.

Es un **sistema personal de aprendizaje**.

Entrena:

* pensamiento lógico
* arquitectura
* modelado de datos
* diseño de sistemas
* ingeniería real
* disciplina
* visión de proyecto

---

# 🧠 Frase guía

> No construyas todo.
> Construye el núcleo.
> Luego crece.

---

# 🚀 Objetivo final

Tener una herramienta que:

* piense contigo
* decida contigo
* te quite fricción mental
* te diga qué estudiar

No una agenda.
No un calendario.

Un **sistema inteligente personal**.
