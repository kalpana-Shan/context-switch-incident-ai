import os
import json
from openai import OpenAI
from shared_contract import IncidentAlert, IncidentAnalysis
from typing import Dict

class IncidentSynthesizer:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def analyze_incident(self, alert_subject: str, alert_body: str, context: Dict) -> IncidentAnalysis:
        """Main AI analysis function"""
        print("🤖 AI analyzing incident with context...")
        
        # Get AI analysis
        ai_response = self._get_ai_analysis(alert_subject, alert_body, context)
        
        # Calculate correlation score
        correlation_score = self._calculate_correlation_score(context)
        
        # Create analysis object
        analysis = IncidentAnalysis(
            root_cause=ai_response.get('root_cause', 'Unknown'),
            immediate_actions=ai_response.get('immediate_actions', []),
            confidence_score=ai_response.get('confidence_score', 5),
            experts_to_involve=ai_response.get('experts_to_involve', []),
            correlation_score=correlation_score
        )
        
        return analysis
    
    def _get_ai_analysis(self, subject: str, body: str, context: Dict) -> Dict:
        """Get AI analysis using OpenAI"""
        prompt = self._build_analysis_prompt(subject, body, context)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=500
            )
            
            result = response.choices[0].message.content
            return json.loads(result)
            
        except Exception as e:
            print(f"❌ AI analysis failed: {e}")
            return self._get_fallback_analysis(subject)
    
    def _build_analysis_prompt(self, subject: str, body: str, context: Dict) -> str:
        """Build the prompt for AI analysis"""
        prompt_text = """You are an expert incident response analyst. Analyze this incident with the provided context and provide actionable insights.

INCIDENT:
Subject: {subject}
Details: {body}

CONTEXT FOUND:
- Slack Discussions: {slack_messages}
- Recent Code Changes: {github_changes}
- Historical Incidents: {historical_incidents}

Provide your analysis as JSON with this exact structure:
{{
    "root_cause": "Brief likely root cause based on context",
    "immediate_actions": ["Action 1", "Action 2", "Action 3"],
    "confidence_score": 7,
    "experts_to_involve": ["@database_team", "@backend_team"]
}}

Be concise and actionable.
""".format(
            subject=subject,
            body=body,
            slack_messages=context.get('slack_messages', []),
            github_changes=context.get('github_changes', []),
            historical_incidents=context.get('historical_incidents', [])
        )
        return prompt_text
    
    def _calculate_correlation_score(self, context: Dict) -> float:
        """Calculate how well the context correlates with potential causes"""
        score = 0.0
        
        # Score based on context richness
        if context.get('slack_messages'):
            score += 0.3
        if context.get('github_changes'):
            score += 0.3
        if context.get('historical_incidents'):
            score += 0.4
            
        return min(score, 1.0)
    
    def _get_fallback_analysis(self, subject: str) -> Dict:
        """Fallback analysis if AI fails"""
        return {
            "root_cause": "Requires manual investigation - AI analysis unavailable",
            "immediate_actions": [
                "Check recent deployments",
                "Review monitoring dashboards", 
                "Contact on-call engineer"
            ],
            "confidence_score": 3,
            "experts_to_involve": ["@oncall_engineer"]
        }