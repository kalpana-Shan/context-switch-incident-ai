import sys 
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
 
from src.correlation_engine import ContextCorrelator 
from src.ai_synthesizer import IncidentSynthesizer 
 
def test_ai_analysis(): 
    """Test AI analysis with mock data""" 
    print("?? Testing AI analysis...") 
 
    synthesizer = IncidentSynthesizer() 
    result = synthesizer.analyze_incident( 
        "Database slow", 
        "CPU at 95% for 10 minutes", 
        { 
            "slack_messages": [{"text": "deployed database changes"}], 
            "github_changes": [{"message": "add indexes"}], 
            "historical_incidents": [{"title": "similar issue"}] 
        } 
    ) 
 
    assert hasattr(result, 'root_cause') 
    assert hasattr(result, 'immediate_actions') 
    assert hasattr(result, 'confidence_score') 
    print("? AI analysis test passed!") 
 
def test_correlation_engine(): 
    """Test the full correlation engine""" 
    print("?? Testing correlation engine...") 
 
    correlator = ContextCorrelator() 
    result = correlator.process_incident( 
        "Test incident", 
        "This is a test incident body" 
    ) 
 
    assert hasattr(result, 'correlation_score') 
    assert result.confidence_score 
    print("? Correlation engine test passed!") 
 
if __name__ == "__main__": 
    test_ai_analysis() 
    test_correlation_engine() 
    print("?? All tests passed! Ready for integration.") 
