"""Simulates market price movements for trading algorithm testing."""

import random
from collections import deque
from typing import List


class MarketDataSimulator:
    """Generates a stream of simulated market prices."""

    def __init__(
        self,
        initial_price: float = 100.0,
        volatility: float = 0.02,
        trend: float = 0.0005,
        history_size: int = 60,
    ):
        """
        Initializes the market data simulator.

        Args:
            initial_price: The starting price for the simulation.
            volatility: The standard deviation of the daily price change percentage.
            trend: The average daily price change percentage (drift).
            history_size: The maximum number of historical prices to store.
        """
        self.current_price: float = initial_price
        self.volatility: float = volatility
        self.trend: float = trend
        # Store a rolling window of historical prices.
        self.history: deque[float] = deque(maxlen=history_size)
        self.history.append(self.current_price)  # Start history with the initial price

    def _generate_and_add_price(self) -> None:
        """Internal helper to generate the next price based on trend and volatility, and add it to history."""
        change_pct = random.normalvariate(self.trend, self.volatility)
        self.current_price *= 1 + change_pct
        self.current_price = max(
            1.0, self.current_price
        )  # Ensure price doesn't go below 1.0
        self.history.append(self.current_price)

    def next_price(self) -> float:
        """Generates, stores, and returns the next market price."""
        self._generate_and_add_price()
        return self.current_price

    def get_historical_prices(self) -> List[float]:
        """Returns the current list of historical prices."""
        return list(self.history)

    def get_current_price(self) -> float:
        """Returns the most recently generated price."""
        return self.current_price
