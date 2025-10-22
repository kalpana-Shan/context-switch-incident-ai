 
 
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
