 '''
 IPO News Crawler using GoogleNews Python package.

This module provides a crawler implementation for fetching IPO-related news.
 '''

from __future__ import annotations

import json
import logging
import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List

from GoogleNews import GoogleNews

# ---------------------------------------------------------------------------
# Paths
# 設定程式的上上層目錄
BASE_DIR = Path(__file__).resolve().parent[2]
# 建立data/ logs/ 資料夾用於儲存結果與日誌
DATA_DIR = BASE_DIR / 'data'
LOG_DIR = BASE_DIR / 'logs'

DATA_DIR.mkdir(parents=True, exit_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / "crawler.log", encoding="utf-8"),
    ],
)

logger = logging.getLogger(__name__)

def fetch_news(keyword: str, pages: int = 1, days: int = 1):
  '''
    Fetch news articles for the given keyword

    Args:
        keyword: Search keyword for news articles
        pages: Number of result pages to retrieve
        days: Number of days in the past to fetch news from
    Returns:
        List of news articles as dictionaries
  '''
  logger.info(f'開始搜尋關鍵字：{keyword}，頁數：{pages}，天數：{days}')
  try:
   # Calculate date range
   end_date = datetime.now()
   start_date = end_date - timedelta(days=days)
   # Initialize GoogleNews
   google_news = GoogleNews(lang='zh-TW', period='custom')
   google_news.set_time_range(
   start_date.strftime('%m/%d/%Y'),
   end_date.strftime('%m/%d/%Y')
   )
   logger.info(f'開始搜尋關鍵字: {keyword}')
   google_news.search(keyword)
   results: List[Dict[str, Any]] = []
   for page in range(pages):
    logger.info(f'正在抓取第 {page + 1} 頁...')
    page_results = google_news.results(sort=True)
    if not page_results:
      logger.warning(f'第 {page + 1} 頁沒有結果')
      break 
    # Move to next page if not the last iteration
    if page < page -1:
      google_news.next_page()
      time.sleep(2) # Be Respectful to the server
   
    logger.info(f'總共抓取到 {len(results)} 筆新聞')
    return results

  except Exception as e:
    logger.error(f'抓取新聞時發生錯誤: {e}')
    raise
 
def save_results(keyword: str, results: List[Dict[str, Any]]) -> str:
  '''
  Save results to a Json file under DATA_DER.
  Args:
    keyword: Search keyword used
    results: List of news articles
  Returns:
    Path to saved file
  '''
  try:
    # ensure data dictionary exists
    DATA_DIR.mkdir(parents=True, exit_ok=True)

    # generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'{keyword.replace(' ', '_')}_{timestamp}.json'
    file_path = DATA_DIR / filename

    # Save Results
    with open(file_path, 'w', encoding='utf-8') as f:
      json.dump(results, f, ensure_ascii=False, indent=2)
      logger.info(f'結果已經儲存至: {file_path}')
      return str(file_path)
    
  except Exception as e:
    logger.error(f'儲存結果時發生錯誤: {e}')
    raise
  
def crawl(keyword: str, days: int = 1, pages: int = 1) -> str:
  '''
  Main crawling function

  Args:
    keyword: Search keyword
    days: Number of days back to search
    pages: Number of pages to fetch
  Returns:
    path to saved results file
  '''
  logger.info(f'開始爬蟲作業 - 關鍵字: {keyword}, 天數: {days}, 頁數: {pages}')
  try:
    # Fetch news
    results = fetch_news(keyword, pages=pages, days=days)

    if not results:
      logger.warning('沒有找到任何新聞')
      return ''
    
    # Save Results
    output_path = save_results(keyword, results)
    logger.info(f'爬蟲作業完成，結果儲存於: {output_path}')

    return output_path
  except Exception as e:
    logger.error(f'爬蟲作業失敗: {e}')
    raise
  
if __name__ == '__main__':
  keyword = 'IPO'
  try:
    output_path = crawl(keyword, days=7, pages=2)
    print(f'爬蟲完成，結果儲存於：{output_path}')
  except Exception as e:
    print(f'爬蟲失敗: {e}')
