from prometheus_client import Counter

REQUEST_COUNTER = Counter(
    "http_requests_total",
    "Total HTTP Requests",
)