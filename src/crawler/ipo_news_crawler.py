"""
IPO News Crawler using GoogleNews Python package
"""

import time
import pandas as pd
from datetime import datetime, timedelta
from GoogleNews import GoogleNews
import json
import logging
from typing import List, Dict, Any
import os

# 設定日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.
    ]
)