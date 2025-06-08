"""IPO News Crawler using GoogleNews Python package."""

from datetime import datetime
from typing import List
import logging

import pandas as pd
from GoogleNews import GoogleNews

logger = logging.getLogger(__name__)


def _format_date(date_str: str) -> str:
    """Convert YYYY-MM-DD to MM/DD/YYYY for GoogleNews."""
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%m/%d/%Y")
    except ValueError:
        # Assume already in correct format
        return date_str


def fetch_ipo_news(start_date: str, end_date: str, pages: int = 1) -> pd.DataFrame:
    """Fetch IPO related news within a date range using GoogleNews.

    Parameters
    ----------
    start_date : str
        Start date in ``YYYY-MM-DD`` format.
    end_date : str
        End date in ``YYYY-MM-DD`` format.
    pages : int, optional
        Number of Google News result pages to fetch, by default 1.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing columns ``title``, ``media``, ``date`` and ``link``.
    """
    start = _format_date(start_date)
    end = _format_date(end_date)

    logger.info("Fetching IPO news from %s to %s", start_date, end_date)

    google_news = GoogleNews(start=start, end=end, lang="en")
    google_news.search("IPO")

    all_results: List[dict] = []
    for page in range(1, pages + 1):
        try:
            if page > 1:
                google_news.getpage(page)
        except Exception as exc:  # pragma: no cover - defensive
            logger.warning("Failed to fetch page %s: %s", page, exc)
            break
        all_results.extend(google_news.result())

    df = pd.DataFrame(all_results)
    if not df.empty:
        keep_cols = [c for c in ["title", "media", "date", "link"] if c in df.columns]
        df = df[keep_cols]
    return df
