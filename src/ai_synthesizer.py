import os
import json
import ollama
from shared_contract import IncidentAlert, IncidentAnalysis
from typing import Dict

class IncidentSynthesizer:
    def __init__(self):
        self.model = "phi:2.7b"  
        print("🤖 Initializing Ollama AI engine...")
        
    def analyze_incident(self, alert_subject: str, alert_body: str, context: Dict) -> IncidentAnalysis:
        """Main AI analysis function"""
        print("🤖 AI analyzing incident with context...")
        
        # Get AI analysis
        ai_response = self._get_ai_analysis(alert_subject, alert_body, context)
        
        # Calculate correlation score
        correlation_score = self._calculate_correlation_score(context)
        
        # Create analysis object
        analysis = IncidentAnalysis(
            root_cause=ai_response.get('root_cause', 'Analysis in progress'),
            immediate_actions=ai_response.get('immediate_actions', []),
            confidence_score=ai_response.get('confidence_score', 7),
            experts_to_involve=ai_response.get('experts_to_involve', []),
            correlation_score=correlation_score
        )
        
        return analysis
    
    def _get_ai_analysis(self, subject: str, body: str, context: Dict) -> Dict:
        """Get AI analysis using Ollama"""
        prompt = self._build_analysis_prompt(subject, body, context)
        
        try:
            print("🔄 Querying Ollama...")
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                options={'temperature': 0.1}
            )
            
            result = response['response']
            print(f"📄 Ollama response: {result[:100]}...")
            return self._extract_json(result)
            
        except Exception as e:
            print(f"❌ Ollama analysis failed: {e}")
            return self._get_fallback_analysis(subject)
    
    def _extract_json(self, text: str) -> Dict:
        """Extract JSON from Ollama response"""
        try:
            # Find JSON in the response
            start = text.find('{')
            end = text.rfind('}') + 1
            if start != -1 and end != 0:
                json_str = text[start:end]
                return json.loads(json_str)
        except:
            pass
        return self._get_fallback_analysis("parse error")
    
    def _build_analysis_prompt(self, subject: str, body: str, context: Dict) -> str:
        """Build the prompt for AI analysis"""
        return f"""Analyze this incident and return ONLY JSON:

INCIDENT: {subject} - {body}

CONTEXT:
Slack: {context.get('slack_messages', [])}
GitHub: {context.get('github_changes', [])}
History: {context.get('historical_incidents', [])}

Return JSON with: root_cause, immediate_actions, confidence_score, experts_to_involve"""
    
    def _calculate_correlation_score(self, context: Dict) -> float:
        """Calculate correlation score"""
        score = 0.0
        if context.get('slack_messages'): score += 0.3
        if context.get('github_changes'): score += 0.3
        if context.get('historical_incidents'): score += 0.4
        return min(score, 1.0)
    
    def _get_fallback_analysis(self, subject: str) -> Dict:
        """Fallback analysis"""
        return {
            "root_cause": "System analysis in progress",
            "immediate_actions": ["Check logs", "Review deployments", "Contact team"],
            "confidence_score": 6,
            "experts_to_involve": ["@oncall_engineer"]
        }
