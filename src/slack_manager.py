import os
import logging
from composio import Composio
from shared_contract import IncidentAnalysis

class SlackManager:
    def __init__(self):
        self.composio = Composio(api_key=os.getenv('COMPOSIO_API_KEY'))
        self.logger = logging.getLogger(__name__)
        self.channel = "#incidents"

    def send_incident_alert(self, analysis: IncidentAnalysis, original_alert: str):
        """Send formatted incident analysis to Slack"""
        try:
            message_blocks = [
                {"type": "header", "text": {"type": "plain_text", "text": "INCIDENT CONTEXT ASSEMBLED"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": f"*Alert:* {original_alert}\n*Root Cause:* {analysis.root_cause}"}}
            ]

            result = self.composio.execute_action(
                "slack_send_message",
                channel=self.channel,
                blocks=message_blocks,
                text=f"Incident: {analysis.root_cause}"
            )

            self.logger.info("Incident alert sent to Slack")
            return True

        except Exception as e:
            self.logger.error(f"Failed to send Slack message: {e}")
            return False
