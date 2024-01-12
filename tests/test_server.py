import os
import unittest
from unittest.mock import patch
from app.server import response


class ServiceTests(unittest.TestCase):
    def test_liveness(self):
        self.assertEqual(response("/healthz"), (200, {"status": "ok"}))

    def test_unknown_route(self):
        self.assertEqual(response("/unknown")[0], 404)

    def test_sample_shipment(self):
        with patch.dict(os.environ, {"DATA_FILE": "data/shipments.json"}):
            self.assertEqual(response("/shipments/PKG-1001")[1]["status"], "in_transit")

    def test_missing_data(self):
        with patch.dict(os.environ, {"DATA_FILE": "/nonexistent/interview-data.json"}):
            self.assertEqual(response("/shipments/PKG-1001")[0], 503)
