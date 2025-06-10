"""
IPO NEWS Crawler 執行腳本
"""

import sys
import os
import argparse
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from . import ipo_news_crawler


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="IPO News crawler")
    parser.add_argument("keyword", help="Keyword to search on Google News")
    parser.add_argument(
        "--days", type=int, default=1, help="Number of days in the past to fetch"
    )
    parser.add_argument(
        "--pages", type=int, default=1, help="Number of result pages to retrieve"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> Any:
    args = parse_args(argv)
    return crawl(args.keyword, days=args.days, pages=args.pages)


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()