from dataclasses import dataclass

@dataclass
class BotConfig:
    symbol: str = "XAUUSDm"

    execution_tf: int = 15
    trend_tf: int = 60

    risk_per_trade_pct: float = 0.002
    daily_drawdown_limit_pct: float = 0.02
    max_open_positions: int = 1
    max_lot: float = 0.10
    min_lot: float = 0.01

    atr_period: int = 14
    sl_atr_mult: float = 2.0
    tp_rr_ratio: float = 2.5
    trailing_atr_mult: float = 1.5
    break_even_atr_mult: float = 1.0

    magic_number: int = 20261003
    deviation_points: int = 30

    report_path: str = "quant_trading_report.xlsx"
    initial_capital: float = 10000.0
    backtest_days: int = 60
