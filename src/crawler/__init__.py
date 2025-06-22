'''
IPO NEWS Crawler 執行腳本
'''

import sys
import os
import argparse
from typing import Any

# 加入父目錄到 Python 路徑

sys.path.append(os.path.dirname(__name__), '..')
from .ipo_news_crawler import crawl

def parse_args(argv: list[str] | None=None) -> argparse.Namespace:
    '''Parse command line arguments.'''
    parser = argparse.ArgumentParser(description='IPO News crawler')
    parser.add_argument('keyword', help='要搜尋的關鍵字')
    parser.add_argument('--days', type=int, default=1, help='要搜尋過去幾天的新聞(default:1)')
    parser.add_argument('--pages', type=int, default=1, help='要抓取的結果頁數 (default:1)')
    return parser.parse_args(argv)

def main(argv: list[str] | None = None) -> str:
    '''Main entry point for the crawler'''
    args = parse_args(argv)
    return crawl(args.keyword, days=args.days, pages=args.pages)

if __name__ == '__main__':
    main()