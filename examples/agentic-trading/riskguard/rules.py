import logging
from dataclasses import dataclass
from typing import Any, Dict

# Import defaults from the common config
from common.config import (
    DEFAULT_RISKGUARD_MAX_CONCENTRATION,
    DEFAULT_RISKGUARD_MAX_POS_SIZE,
)

logger = logging.getLogger(__name__)


@dataclass
class RiskCheckResult:
    """Dataclass to hold the result of a risk check."""

    approved: bool
    reason: str = ""


def check_trade_risk_logic(
    trade_proposal: Dict[str, Any],
    portfolio_state: Dict[str, Any],
    max_pos_size: float = DEFAULT_RISKGUARD_MAX_POS_SIZE,  # Use imported default
    max_concentration: float = DEFAULT_RISKGUARD_MAX_CONCENTRATION,  # Use imported default
) -> RiskCheckResult:
    """
    Encapsulates the risk checking logic, using provided limits.

    Args:
        trade_proposal: Dict with {'action': 'BUY'/'SELL', 'ticker': str, 'quantity': int, 'price': float}
        portfolio_state: Dict with current {'cash': float, 'shares': int, 'total_value': float}

    Returns:
        RiskCheckResult indicating approval status and reason.
    """
    logger.info(f"Checking proposal: {trade_proposal}")

    # Basic validation
    ticker = trade_proposal.get("ticker")
    action = trade_proposal.get("action")
    quantity = trade_proposal.get("quantity")
    price = trade_proposal.get("price")
    if (
        not all(
            [
                ticker,
                isinstance(action, str),
                isinstance(quantity, int),
                isinstance(price, float),
            ]
        )
        or quantity <= 0
        or price <= 0
    ):
        logger.warning("Invalid trade proposal structure or values.")
        return RiskCheckResult(
            approved=False, reason="Invalid trade proposal structure or values."
        )

    # Get portfolio details safely
    cash = portfolio_state.get("cash", 0.0)
    current_shares = portfolio_state.get("shares", 0)
    total_value = portfolio_state.get("total_value", 0.0)
    if total_value <= 0:
        logger.warning("Invalid total portfolio value for risk check.")
        return RiskCheckResult(
            approved=False, reason="Invalid total portfolio value for risk check."
        )

    proposed_trade_value = quantity * price
    action_upper = action.upper()

    if action_upper == "BUY":
        # Rule 1 (BUY): Sufficient Cash
        if proposed_trade_value > cash:
            reason = (
                f"Insufficient cash ({cash:.2f} < required {proposed_trade_value:.2f})"
            )
            logger.warning(f"REJECTED - {reason}")
            return RiskCheckResult(approved=False, reason=reason)

        # Rule 2 (BUY): Max Asset Concentration (Post-Trade)
        post_trade_shares = current_shares + quantity
        post_trade_holdings_value = post_trade_shares * price
        post_trade_total_value = (
            cash - proposed_trade_value
        ) + post_trade_holdings_value  # More accurate
        if post_trade_total_value <= 0:
            post_trade_total_value = total_value  # Fallback if cash becomes negative

        concentration = (
            post_trade_holdings_value / post_trade_total_value
            if post_trade_total_value > 0
            else 1.0
        )
        if concentration > max_concentration:  # Use parameter
            reason = f"Exceeds max asset concentration ({concentration*100:.1f}% > {max_concentration*100:.1f}%)"
            logger.warning(f"REJECTED - {reason}")
            return RiskCheckResult(approved=False, reason=reason)

        # Rule 3 (BUY): Max Position Size per Trade (Check after cash/concentration)
        if proposed_trade_value > max_pos_size:  # Use parameter
            reason = f"Exceeds max position size per trade (${proposed_trade_value:.2f} > ${max_pos_size:.2f})"
            logger.warning(f"REJECTED - {reason}")
            return RiskCheckResult(approved=False, reason=reason)

    elif action_upper == "SELL":
        # Rule 1 (SELL): Sufficient Shares to Sell
        if quantity > current_shares:
            reason = (
                f"Insufficient shares to sell ({current_shares} < requested {quantity})"
            )
            logger.warning(f"REJECTED - {reason}")
            return RiskCheckResult(approved=False, reason=reason)

        # Rule 2 (SELL): Max Position Size per Trade (Check after sufficient shares)
        if proposed_trade_value > max_pos_size:  # Use parameter
            reason = f"Exceeds max position size per trade (${proposed_trade_value:.2f} > ${max_pos_size:.2f})"
            logger.warning(f"REJECTED - {reason}")
            return RiskCheckResult(approved=False, reason=reason)

    else:
        logger.warning(f"Unknown trade action '{action}'.")
        return RiskCheckResult(
            approved=False, reason=f"Unknown trade action '{action}'."
        )

    # If all checks passed for the given action
    logger.info("APPROVED - Trade adheres to risk rules.")
    return RiskCheckResult(approved=True, reason="Trade adheres to risk rules.")
