import locale
import logging
from dataclasses import dataclass
from enum import Enum, auto

logger = logging.getLogger(__name__)


class TradeAction(Enum):
    BUY = auto()
    SELL = auto()


@dataclass
class PortfolioState:
    """Holds the current state of the trading portfolio."""

    cash: float = 100_000.0
    shares: int = 0
    holdings_value: float = 0.0
    total_value: float = 100_000.0

    def _format_currency(self, value: float) -> str:
        """Internal helper to format currency using locale, with fallback."""
        try:
            # Attempt to use locale formatting (assuming locale set elsewhere)
            # Set locale temporarily if needed, or ensure it's set globally.
            # Example: locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
            return locale.currency(value, grouping=True)
        except Exception as e:
            # Broad exception catch for any locale or formatting issues
            logger.warning(
                f"Locale currency formatting failed (value: {value}): {e}. Using fallback."
            )
            return f"${value:,.2f}"  # Basic fallback format

    def update_valuation(self, current_price: float):
        """Updates holding and total values based on the current price."""
        self.holdings_value = self.shares * current_price
        self.total_value = self.cash + self.holdings_value

    def execute_trade(self, action: TradeAction, quantity: int, price: float) -> bool:
        """Applies a trade to the portfolio state using TradeAction enum."""
        price_f = self._format_currency(price)

        if action == TradeAction.BUY:
            cost = quantity * price
            if cost > self.cash:
                cost_f = self._format_currency(cost)
                cash_f = self._format_currency(self.cash)
                logger.warning(
                    f"Attempted BUY overdraft. Need: {cost_f}, Have: {cash_f}"
                )
                return False
            self.cash -= cost
            self.shares += quantity
            logger.info(f"Executed: BUY {quantity} @ {price_f}")
            return True
        elif action == TradeAction.SELL:
            if quantity > self.shares:
                logger.warning(
                    f"Attempted SELL more shares than held. Have: {self.shares}, Want: {quantity}"
                )
                return False
            self.cash += quantity * price
            self.shares -= quantity
            logger.info(f"Executed: SELL {quantity} @ {price_f}")
            return True
        # No 'else' needed as TradeAction enum covers all valid cases.
        # If an invalid value somehow gets passed, it would raise an error earlier.
        return False  # Should not be reached if using the enum correctly

    def __str__(self):
        """Returns a locale-formatted string representation of the portfolio."""
        cash_f = self._format_currency(self.cash)
        holdings_f = self._format_currency(self.holdings_value)
        total_f = self._format_currency(self.total_value)
        return f"Cash={cash_f}, Shares={self.shares}, Holdings={holdings_f}, Total={total_f}"
