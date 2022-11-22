class Email:
    def __init__(self):
        import os
        from dotenv import load_dotenv
        from email.message import EmailMessage

        load_dotenv()
        self._host = os.environ["EMAIL_SMTP_HOST"]
        self._port = int(os.environ["EMAIL_SMTP_PORT"])
        self._username = os.environ["EMAIL_SMTP_USERNAME"]
        self._password = os.environ["EMAIL_SMTP_PASSWORD"]
        email_to = os.environ["EMAIL_TO"]
        email_from = os.environ["EMAIL_FROM"]
        email_subject = os.environ["EMAIL_SUBJECT"]
        email_content = os.environ["EMAIL_CONTENT"]

        self._message = EmailMessage()
        self._message["To"] = email_to
        self._message["From"] = email_from
        self._message["Subject"] = email_subject
        self._message.set_content(email_content)

    def notify(self, params=None):
        if params is not None:
            del self._message["Subject"]
            self._message["Subject"] = params["Subject"]
            self._message.set_content(params["Content"])

        import ssl
        from smtplib import SMTP_SSL

        context = ssl.create_default_context()
        server = SMTP_SSL(self._host, self._port, context=context)
        server.login(self._username, self._password)
        server.send_message(self._message)
        server.quit()


class Slack:
    def __init__(self):
        import os
        from dotenv import load_dotenv
        from slack_sdk.web import WebClient

        load_dotenv()
        token = os.environ["SLACK_API_TOKEN"]
        self._text = os.environ["SLACK_TEXT"]
        self._channel = os.environ["SLACK_CHANNEL"]
        self._client = WebClient(token=token)

    def notify(self):
        self._client.chat_postMessage(text=self._text, channel=self._channel)


class Notifier:
    def __init__(self):
        import os
        from dotenv import load_dotenv

        load_dotenv()
        email_enable = int(os.environ["EMAIL_ENABLE"])
        slack_enable = int(os.environ["SLACK_ENABLE"])

        self._email = Email() if email_enable else None
        self._slack = Slack() if slack_enable else None

    def notify(self):
        if self._email is not None:
            self._email.notify()
        if self._slack is not None:
            self._slack.notify()

    def stop(self):
        pass
