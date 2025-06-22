# IPO News Analysis

This project provides a simple crawler that gathers news about IPOs using the
`GoogleNews` library. The crawler can be run from the command line and stores
retrieved articles as JSON files.

## Data directory

All crawled data is written to the `data` directory at the repository root.
The crawler will create this directory automatically if it does not already
exist. The path is exposed in the code via the constant `DATA_DIR`.

## Usage

```bash
python -m crawler "IPO" --days 7 --pages 3
```

The command above searches for "IPO" news from the last seven days and saves the
results to a timestamped JSON file inside `data/`.