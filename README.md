# 🧠 Productive ETL – Documentación Técnica

Este proyecto ejecuta un pipeline ETL que extrae datos desde la API de **Productive**, los transforma y los carga en **Google BigQuery**, con logs automáticos y notificación opcional por **Discord**.

---

## 🧰 Requisitos técnicos

- Python 3.9 o superior
- Acceso al proyecto de Google Cloud con permisos sobre BigQuery
- Token de API de Productive
- (Opcional) Webhook de Discord para alertas

---

## 📁 Estructura del proyecto

Productive_Solu/
├── main.py
├── notificador.py
├── requirements.txt
├── .env
├── .env.example
├── README.md
├── productive/
│ ├── extractor.py
│ ├── transformer.py
│ ├── loader.py
│ ├── entidades.py
│ └── funciones/
├── bigquery/
│ ├── bigquery_func.py
│ └── querys.py
├── schema/
│ └── schemas.py
├── credenciales/
│ └── data-warehouse-xxxxxx.json
└── logs/
└── productive_etl.log


---

## 🧪 Instalación

```bash
# Crear entorno virtual
python -m venv myenv
myenv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt


---

## 📄 .env.example

# Google Cloud / BigQuery
PROJECT_ID=
DATASET_FINAL=
DATASET_TEMP=
GOOGLE_APPLICATION_CREDENTIALS=credenciales/data-warehouse-xxxxxx.json

# Productive API
ACCESS_TOKEN=
X_ORGANIZATION_ID=

# Discord (opcional)
DISCORD_WEBHOOK=


## ▶️ Ejecución
bash
Copiar
Editar
python main.py
El script detecta automáticamente si debe ejecutarse de forma:

Diaria

Semanal (los lunes)

Mensual (el 1° de cada mes)

Histórica (flag interno)

## 🧾 ¿Qué hace?
Llama a los endpoints de Productive

Limpia y transforma los datos

Carga DataFrames en BigQuery (con WRITE_TRUNCATE)

Ejecuta MERGE SQL para mantener actualizado el dataset final

Genera un log local

(Opcional) Envia resumen a Discord en formato embed

## 🧠 Notificaciones por Discord (opcional)
Si definís la variable DISCORD_WEBHOOK en tu .env, se enviará un resumen como este:

✅ Productive ETL – Ejecución DIARIA

## 🛠️ Mantenimiento
Token de Productive puede expirar → renovar ACCESS_TOKEN

Revisar productive_etl.log en carpeta logs/

Consultar canal de Discord si algo falla fuera de horario

## 👤 Contacto
Responsable funcional: Tomás Pérez Zorraquín