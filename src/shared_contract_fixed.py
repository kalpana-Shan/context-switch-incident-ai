from dataclasses import dataclass 
from typing import List, Dict, Any 
 
@dataclass 
class IncidentAlert: 
    subject: str 
    body: str 
    timestamp: str = "" 
 
@dataclass 
class IncidentAnalysis: 
    root_cause: str 
    confidence_score: int 
    correlation_score: float 
    immediate_actions: List[str] 
    experts_to_involve: List[str] 
 
MOCK_CONTEXT = { 
    'slack_messages': [ 
        {'user': 'system', 'text': 'Monitoring systems normal', 'timestamp': '2 hours ago', 'relevance': 0.3} 
    ], 
    'github_changes': [ 
        {'repo': 'backend', 'change': 'Updated database config', 'timestamp': '4 hours ago'} 
    ], 
    'historical_incidents': [ 
        {'title': 'Similar database issue', 'date': '2024-01-15', 'resolution': 'Index optimization'} 
    ] 
} 
