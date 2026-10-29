import json, logging                      # json: logs estructurados; logging: sistema de logs de Python
from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)                     # crea la aplicación web
REQUESTS = Counter("taskapi_requests_total", "Peticiones totales", ["endpoint"])  # métrica con etiqueta "endpoint"
logging.basicConfig(level=logging.INFO, format="%(message)s")  # los logs salen a stdout (Loki los recoge de ahí)
log = logging.getLogger("taskapi")

@app.route("/")                           # ruta principal
def index():
    REQUESTS.labels(endpoint="/").inc()   # suma 1 al contador
    log.info(json.dumps({"event": "request", "path": "/"}))
    return jsonify(message="Hola DevOps", version="1.0.0")

@app.route("/health")                     # la usarán los probes de Kubernetes
def health():
    return jsonify(status="ok")

@app.route("/metrics")                    # Prometheus lee esta ruta
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)