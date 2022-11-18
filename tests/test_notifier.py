import pytest

from simple_raspi_notifier.notifier import Email


class TestNotifier:
    @pytest.fixture
    def email(self):
        return Email()

    def test_email_notify(self, email):
        params = {
            "Subject": "テストメールのタイトル",
            "Content": "テストメールの本文です",
        }
        try:
            email.notify(params)
        except Exception:
            pytest.fail("Unexpected error")
