from dataclasses import dataclass 
from datetime import datetime 
from typing import List, Dict, Any 
 
@dataclass 
class IncidentAlert: 
    subject: str 
    body: str 
    source: str = 'manual' 
    timestamp: datetime = None 
    severity: str = 'medium' 
 
@dataclass 
class IncidentAnalysis: 
    root_cause: str 
    immediate_actions: List[str] 
    confidence_score: int 
    experts_to_involve: List[str] 
    correlation_score: float = 0.0 
 
 
# Mock data for development 
MOCK_CONTEXT = { 
    "slack_messages": [ 
        { 
            "user": "dev_team", 
            "text": "Just deployed new database indexes to production", 
            "timestamp": "2 hours ago", 
            "relevance": 0.9 
        } 
    ], 
    "github_changes": [ 
        { 
            "commit": "abc123", 
            "message": "feat: Add new database indexes", 
            "files": ["database/schema.sql"], 
            "relevance": 0.8 
        } 
    ], 
    "historical_incidents": [ 
        { 
            "title": "Database performance issue", 
            "fix": "Rolled back index changes", 
            "similarity": 0.85 
        } 
    ] 
} 
