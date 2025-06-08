"""
IPO NEWS Crawler 執行腳本
"""

import sys
import os
import argparse
from datetime import datetime

# 增加src目錄到Python路徑
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from crawler.