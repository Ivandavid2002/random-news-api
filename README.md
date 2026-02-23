# 📰 Random News API

API REST desarrollada con **FastAPI** que consume la API pública de NewsAPI y devuelve una noticia aleatoria según una palabra clave.

---

## 🚀 Características

- 🔹 Obtiene noticias en tiempo real
- 🔹 Devuelve una noticia aleatoria por petición
- 🔹 Permite búsqueda por palabra clave
- 🔹 Documentación automática con Swagger
- 🔹 Manejo de errores
- 🔹 Estructura profesional del proyecto
- 🔹 Lista para Docker

---

## 🛠️ Tecnologías Utilizadas

- Python 3.10+
- FastAPI
- Uvicorn
- Requests
- NewsAPI
- Pytest

---

## 📁 Estructura del Proyecto

random-news-api/
│
├── app/
│ ├── main.py
│ ├── services.py
│ ├── models.py
│ ├── config.py
│
├── tests/
│ └── test_api.py
│
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md

yaml
Copiar código

---

## ⚙️ Instalación

1️⃣ Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/random-news-api.git
cd random-news-api
2️⃣ Crear entorno virtual:

bash
Copiar código
python -m venv venv
3️⃣ Activarlo:

Windows:

bash
Copiar código
venv\Scripts\activate
4️⃣ Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
🔑 Configuración
Crear un archivo .env basado en .env.example:

ini
Copiar código
NEWS_API_KEY=tu_api_key
NEWS_API_URL=https://newsapi.org/v2/everything
Puedes obtener tu API Key gratis en:

https://newsapi.org

▶️ Ejecutar el Proyecto
bash
Copiar código
uvicorn app.main:app --reload
📚 Documentación Automática
Una vez ejecutado, abre:

arduino
Copiar código
http://127.0.0.1:8000/docs
También disponible en:

arduino
Copiar código
http://127.0.0.1:8000/redoc
📌 Endpoint Principal
Obtener noticia aleatoria
arduino
Copiar código
GET /news/random?q=technology
Parámetro:
Parámetro	Tipo	Descripción
q	string	Palabra clave para buscar noticias

📤 Ejemplo de Respuesta JSON
json
Copiar código
{
  "title": "Tech innovation reaches new milestone",
  "description": "A breakthrough in artificial intelligence...",
  "url": "https://example.com/news",
  "source": "BBC News",
  "published_at": "2026-02-23T10:30:00Z"
}
🧪 Ejecutar Tests
bash
Copiar código
pytest
🐳 Ejecutar con Docker
bash
Copiar código
docker build -t random-news-api .
docker run -p 8000:8000 random-news-api
👨‍💻 Autor
Desarrollado por Iván David

GitHub: https://github.com/ivandavid04

📄 Licencia
Este proyecto es de uso educativo y demostrativo.

yaml
Copiar código

---












