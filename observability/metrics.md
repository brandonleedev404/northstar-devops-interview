# Metrics contract
An existing gateway (outside this exercise) exports counter `http_requests_total` with labels `job="parcel-api"`, `status`, `route`, and `instance`. Routes are `/shipments/:id`, `/healthz`, and `/readyz`. The Python process does not expose Prometheus metrics itself. Counters reset independently on gateway restarts.

Target: page when shipment 5xx ratio exceeds 1% for 10 minutes using a 5-minute rate window, provided shipment volume exceeds 1 request/second. Treat no traffic as non-paging. Aggregate instances before dividing. Use synthetic samples for local verification.
