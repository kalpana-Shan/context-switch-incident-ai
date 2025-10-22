import os 
import logging 
from dotenv import load_dotenv 
from correlation_engine import ContextCorrelator 
 
# Load environment variables 
load_dotenv() 
 
# Set up logging 
logging.basicConfig( 
    level=os.getenv('LOG_LEVEL', 'INFO'), 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' 
) 
 
def main(): 
    print("?? CONTEXT-SWITCH Incident Context Aggregator") 
    print("=" * 50) 
 
    # Initialize the correlation engine 
    correlator = ContextCorrelator() 
 
    # Demo mode or interactive mode 
    if os.getenv('DEMO_MODE', 'false').lower() == 'true': 
        run_demo(correlator) 
    else: 
        run_interactive(correlator) 
 
def run_interactive(correlator): 
    """Interactive mode for testing""" 
    print("\n?? Enter incident details (or press Enter for demo data):") 
 
    alert_subject = input("Alert Subject: ").strip() 
    alert_body = input("Alert Body: ").strip() 
 
    # Use demo data if nothing entered 
    if not alert_subject: 
        alert_subject = "Database latency spike detected" 
        alert_body = "CPU usage at 95% for 10 minutes, response times increased by 300%" 
        print("Using demo data...") 
 
    print("\n?? Analyzing incident with AI...") 
 
    try: 
        # Process the incident 
        analysis = correlator.process_incident(alert_subject, alert_body) 
 
        # Display results 
        print("\n" + "="*50) 
        print("?? INCIDENT ANALYSIS COMPLETE") 
        print("="*50) 
        print(f"?? Alert: {alert_subject}") 
        print(f"?? Root Cause: {analysis.root_cause}") 
        print(f"?? Confidence: {analysis.confidence_score}/10") 
        print(f"?? Correlation Score: {analysis.correlation_score:.2f}/1.0") 
 
        print("\n?? Immediate Actions:") 
        for i, action in enumerate(analysis.immediate_actions, 1): 
            print(f"  {i}. {action}") 
 
        print("\n?? Experts to Involve:") 
        for expert in analysis.experts_to_involve: 
            print(f"   {expert}") 
 
        print(f"\n? Ready for Slack integration!") 
 
    except Exception as e: 
        print(f"? Error processing incident: {e}") 
        logging.error(f"Error in main: {e}") 
 
def run_demo(correlator): 
    """Run with predefined demo data""" 
    demo_scenarios = [ 
        { 
            "subject": "Database latency spike detected", 
            "body": "CPU usage at 95% for 10 minutes, response times +300%" 
        }, 
        { 
            "subject": "API error rate increased dramatically", 
            "body": "5xx errors jumped from 1% to 25% in last 5 minutes" 
        } 
    ] 
 
    print("?? Running demo scenarios...") 
 
    for i, scenario in enumerate(demo_scenarios, 1): 
        print(f"\n?? Demo {i}/{len(demo_scenarios)}: {scenario['subject']}") 
        analysis = correlator.process_incident(scenario['subject'], scenario['body']) 
        print(f"   Root Cause: {analysis.root_cause}") 
        print(f"   Confidence: {analysis.confidence_score}/10") 
        print(f"   Correlation: {analysis.correlation_score:.2f}") 
 
if __name__ == "__main__": 
    main() 
