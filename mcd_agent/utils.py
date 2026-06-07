"""Utility functions for MCDAgent"""

import json
from typing import Any, Dict
from datetime import datetime


def format_order(order: Dict[str, Any]) -> str:
    """Format order data for display
    
    Args:
        order: Order data dictionary
    
    Returns:
        Formatted order string
    """
    order_id = order.get('id', 'N/A')
    total = order.get('total', 0)
    status = order.get('status', 'Unknown')
    date = order.get('date', 'N/A')
    
    return f"Order #{order_id} - ${total:.2f} - Status: {status} ({date})"


def format_menu_item(item: Dict[str, Any]) -> str:
    """Format menu item for display
    
    Args:
        item: Menu item dictionary
    
    Returns:
        Formatted menu item string
    """
    name = item.get('name', 'Unknown')
    price = item.get('price', 0)
    description = item.get('description', '')
    
    result = f"{name} - ${price:.2f}"
    if description:
        result += f" - {description}"
    
    return result


def format_store(store: Dict[str, Any]) -> str:
    """Format store data for display
    
    Args:
        store: Store data dictionary
    
    Returns:
        Formatted store string
    """
    name = store.get('name', 'Unknown')
    address = store.get('address', 'N/A')
    phone = store.get('phone', 'N/A')
    distance = store.get('distance', 'N/A')
    
    return f"{name} - {address} - {phone} ({distance} km away)"


def pretty_print_json(data: Dict[str, Any]) -> str:
    """Pretty print JSON data
    
    Args:
        data: Dictionary to print
    
    Returns:
        Formatted JSON string
    """
    return json.dumps(data, indent=2, ensure_ascii=False)


def get_timestamp() -> str:
    """Get current timestamp
    
    Returns:
        ISO format timestamp
    """
    return datetime.now().isoformat()
