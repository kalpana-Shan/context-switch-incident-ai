🚀 CONTEXT-SWITCH - AI Incident Context Aggregator

Stop the 20-Minute Context Switch During Incidents.** CONTEXT-SWITCH uses local AI to automatically gather and analyze incident context in 30 seconds—keeping your engineers focused and your data private.


🎯 What It Does

When an incident occurs, CONTEXT-SWITCH automatically:
🤖 Local AI Analysis: Analyzes incidents using Ollama (local LLM) to identify root causes
📤 Slack Integration: Sends rich formatted alerts to your incident channel  
📚 Historical Logging: Tracks incidents in Google Sheets for future reference
🎭 Demo Mode: Pre-built scenarios for impressive demonstrations
🔒 Privacy-First: All AI processing happens locally with Ollama

🏗️ Architecture

Incident Alert → Ollama LLM Analysis → Slack Notification → Historical Logging
↓ ↓ ↓ ↓
Input Local AI Processing Slack API Google Sheets

📁 Project Structure

context-switch-incident-ai/
├── src/
│ ├── enhanced_main.py # Enhanced application with demo mode 
│ ├── slack_manager.py # Slack integration 
│ ├── historical_manager.py # Google Sheets logging 
│ ├── ollama_integration.py # Local LLM integration 
│ ├── main.py # Basic application 
│ ├── correlation_engine.py # AI analysis engine 
│ ├── ai_synthesizer.py # OpenAI integration
│ └── shared_contract.py # Data structures
├── .env # Environment variables
└── requirements.txt # Python dependencies

👥 Team Contributions

Member 1: Core AI Engine
✅ AI analysis and correlation logic
✅ Basic main application
✅ Data structures and contracts
✅ Ollama Integration - Local LLM processing (Privacy-focused)
✅ Bug fixes and code improvements

Member 2: Integrations & Local AI
✅ Slack integration with rich message formatting
✅ Historical data logging to Google Sheets
✅ Enhanced main application with multiple modes
✅ Demo mode with 3 impressive scenarios

🚀 Quick Start

1. Install Ollama

Download from https://ollama.ai
Pull a model:
ollama pull phi:2.7b

2. Clone & Setup

git clone https://github.com/your-username/context-switch-incident-ai
cd context-switch-incident-ai
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Configure Environment
Copy .env.example to .env:
Required for Ollama (local AI)
USE_OLLAMA=true

Optional integrations

SLACK_BOT_TOKEN=xoxb-your-slack-token
COMPOSIO_API_KEY=ak-your-composio-key
GOOGLE_SHEETS_ID=your-google-sheets-id
Not needed - we use local Ollama!
OPENAI_API_KEY=sk-...

4. Run the Demo

python src/enhanced_main.py
Choose option 2 for the automated demo with 3 scenarios!

🎮 Usage Modes

Demo Mode (Recommended)
python src/enhanced_main.py
Choose 2 for 3 automated demo scenarios

Interactive Mode
python src/enhanced_main.py
Choose 1 to enter custom incidents

Quick Test
python src/enhanced_main.py
Choose 3 for basic functionality test

🔧 Technology Stack

Component	Technology	Purpose
AI Engine	Ollama + Local LLM	Privacy-focused incident analysis
Messaging	Slack API	Real-time alert notifications
Storage	Google Sheets	Historical incident tracking
Orchestration	Composio	API integration management
Backend	Python 3.11	Application logic

🤖 Ollama Models Supported

llama2:7b - Recommended for balance of speed/accuracy
mistral:7b - Faster with good performance
codellama:7b - Code-focused incidents
llama2:13b - Higher accuracy (requires more RAM)

🎥 Demo Scenarios

The system includes 3 realistic incident scenarios:
Database latency spike - CPU at 95%, performance degradation
API error rate increase - 5xx errors jump from 1% to 25%
Production deployment issues - 40% of requests failing

💡 Key Features


🆓 Cost-Effective

No API costs - Uses local Ollama LLMs
Free forever - No monthly subscriptions

🔒 Privacy-Focused

100% local processing - No data leaves your infrastructure
Enterprise-ready - Compliant with strict security policies
Offline capable - Works without internet connection

⚡ Performance

Faster than cloud APIs - No network latency
No rate limits - Process as many incidents as needed
Customizable models - Choose optimal LLM for your needs

🛠️ Developer-Friendly

Easy setup - Simple Ollama installation
Mock mode available - Development without real APIs
Modular architecture - Easy to extend and customize

📊 Business Impact

⏱️ 20min → 30sec incident investigation time
💰 $0 API costs - Uses free local LLMs
🔒 Complete data privacy - No external AI providers
🔄 Eliminates context switching for engineers
📊 Provides actionable insights immediately

🚨 System Requirements

RAM: 8GB+ (16GB recommended for larger models)
Storage: 4GB+ for LLM models
Python: 3.8+
Ollama: Latest version

🔮 Future Enhancements

Multiple Ollama model support with auto-selection
Advanced prompt engineering for better analysis
Integration with local monitoring tools
Team-specific expert routing
Advanced correlation with system metrics

🐛 Troubleshooting

Ollama Not Responding
Check if Ollama is running
curl http://localhost:11434/api/tags
Restart Ollama service
ollama serve
Model Not Found
List available models
ollama list
Pull missing model
ollama pull phi:2.7b

📄 License

MIT License - feel free to use this project for your own initiatives!


Built with ❤️ by [SignalSleuths] - Privacy-First AI Incident Response
Demo video: https://youtu.be/W8WkCgz9WJ4


