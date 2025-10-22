import os 
import logging 
from dotenv import load_dotenv 
from correlation_engine import ContextCorrelator 
from slack_manager import SlackManager 
from historical_manager import HistoricalManager 
 
load_dotenv() 
 
def main(): 
    print("CONTEXT-SWITCH - AI Incident Context Aggregator") 
    print("=" * 50) 
 
    correlator = ContextCorrelator() 
    slack_manager = SlackManager() 
    history_manager = HistoricalManager() 
 
    print("Choose mode:") 
    print("1. Interactive mode (type your own alerts)") 
    print("2. Demo mode (predefined scenarios)") 
    print("3. Quick test (simple alert)") 
 
    choice = input("Enter choice (1/2/3): ").strip() 
 
    if choice == "2": 
        run_demo_mode(correlator, slack_manager, history_manager) 
    elif choice == "3": 
        run_quick_test(correlator, slack_manager, history_manager) 
    else: 
        run_interactive_mode(correlator, slack_manager, history_manager) 
 
def run_demo_mode(correlator, slack_manager, history_manager): 
    demo_scenarios = [ 
        {"subject": "Database latency spike detected", "body": "CPU usage at 95% for 10 minutes"}, 
        {"subject": "API error rate increased dramatically", "body": "5xx errors jumped from 1% to 25%"}, 
        {"subject": "Production deployment issues", "body": "New deployment causing 40% of requests to fail"} 
    ] 
 
    print(f"Running {len(demo_scenarios)} demo scenarios...") 
 
    for i, scenario in enumerate(demo_scenarios, 1): 
        print(f"Demo {i}/{len(demo_scenarios)}") 
        print(f"Alert: {scenario['subject']}") 
 
        analysis = correlator.process_incident(scenario['subject'], scenario['body']) 
 
        print(f"AI Analysis: {analysis.root_cause}") 
        print(f"Confidence: {analysis.confidence_score}/10") 
 
        slack_manager.send_incident_alert(analysis, scenario['subject']) 
        print("Sent to Slack") 
 
        history_manager.log_incident(scenario['subject'], analysis) 
        print("Logged to history") 
        print() 
 
if __name__ == "__main__": 
    main() 
