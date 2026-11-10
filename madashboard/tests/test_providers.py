# Django
from django.test import TestCase

# AA Member Audit Dashboard
from madashboard import __title__
from madashboard.providers import AppLogger, logger


class TestAppLogger(TestCase):
    def test_logger_is_app_logger(self):
        self.assertIsInstance(logger, AppLogger)
        self.assertEqual(logger.logger.name, "madashboard.providers")
        self.assertEqual(logger.prefix, __title__)

    def test_should_add_prefix(self):
        with self.assertLogs(logger.logger, level="INFO") as logs:
            logger.info("Test message")

        self.assertEqual(logs.records[0].getMessage(), f"[{__title__}] Test message")
