# Portfolio Drawdown Sentinel

Tracks synthetic portfolio drawdowns and recovery bands.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m portfolio_drawdown_sentinel.cli --input data/sample_positions.json
```

## Test

```bash
python3 -m unittest discover tests
```
