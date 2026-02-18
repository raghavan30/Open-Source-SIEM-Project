

from elasticsearch import Elasticsearch
from datetime import datetime, timedelta, timezone

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "VYP7PzPFi9du9qur=vyH"),
    verify_certs=False
)

time_threshold = datetime.now(timezone.utc) - timedelta(minutes=5)
