# QuantLight Signals — Public Feed

Auto-generated daily by the QuantLight EOD scanner.

**Last updated:** 21 Sep 2026 23:50 IST

---

## Files

### `structural_rr_setups.json`
All Structural R:R Setups from the QuantLight Gamma Density engine.
Fields per setup: `symbol`, `rank`, `setup_type`, `direction`, `expiry`, `dte`,
`spot_entry`, `spot_sl`, `spot_target`, `spot_rr`, `option_type`, `option_strike`, `option_rr`,
`score`, `regime`, `pattern`, `ivp`.

### `option_strategies_with_legs.json`
Best option strategy per stock with full leg detail.
Fields: `symbol`, `strategy_name`, `legs` (action / qty / opt_type / strike / premium),
`net_debit_per_lot`, `net_credit_per_lot`, `max_profit_per_lot`, `max_loss_per_lot`,
`rr`, `breakeven`, `prob_of_profit`, plus `all_strategies` ranked by score.

---

*Data is for informational purposes only and does not constitute financial advice.*
