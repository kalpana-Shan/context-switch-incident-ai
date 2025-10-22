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
