"""Input validation"""
from typing import Tuple, Optional

def validate_order_params(symbol: str, side: str, order_type: str, 
                         quantity: float, price: Optional[float] = None) -> Tuple[bool, str]:
    if not symbol or len(symbol) < 5:
        return False, "Invalid symbol"
    if side.upper() not in ['BUY', 'SELL']:
        return False, "Side must be BUY/SELL"
    if order_type.upper() not in ['MARKET', 'LIMIT']:
        return False, "Type must be MARKET/LIMIT"
    if quantity <= 0:
        return False, "Quantity must be positive"
    if order_type.upper() == 'LIMIT' and (not price or price <= 0):
        return False, "Price required for LIMIT orders"
    return True, "Valid"
