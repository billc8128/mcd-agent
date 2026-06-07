#!/usr/bin/env python
"""Basic usage examples for MCDAgent"""

import sys
import logging
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from mcd_agent import MCDAgent
from mcd_agent.utils import format_order, format_menu_item, pretty_print_json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def example_get_account():
    """Example: Get account information"""
    print("\n=== Get Account Information ===")
    
    # Initialize agent with token
    agent = MCDAgent(token="snV4IpNWwK1NcWKxqfxbtvnaM1sFywal")
    
    try:
        account = agent.get_account()
        print("Account Info:")
        print(pretty_print_json(account))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.close()


def example_get_menu():
    """Example: Get menu"""
    print("\n=== Get Menu ===")
    
    agent = MCDAgent(token="snV4IpNWwK1NcWKxqfxbtvnaM1sFywal")
    
    try:
        menu = agent.get_menu()
        print(f"Total items: {len(menu.get('items', []))}")
        
        for item in menu.get('items', [])[:5]:  # Show first 5 items
            print(f"  - {format_menu_item(item)}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.close()


def example_search_menu():
    """Example: Search menu"""
    print("\n=== Search Menu ===")
    
    agent = MCDAgent(token="snV4IpNWwK1NcWKxqfxbtvnaM1sFywal")
    
    try:
        results = agent.search_menu("burger")
        print(f"Found {len(results.get('items', []))} items:")
        
        for item in results.get('items', []):
            print(f"  - {format_menu_item(item)}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.close()


def example_get_orders():
    """Example: Get orders"""
    print("\n=== Get Orders ===")
    
    agent = MCDAgent(token="snV4IpNWwK1NcWKxqfxbtvnaM1sFywal")
    
    try:
        orders = agent.get_orders()
        print(f"Total orders: {len(orders.get('items', []))}")
        
        for order in orders.get('items', []):
            print(f"  {format_order(order)}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.close()


def example_get_loyalty_points():
    """Example: Get loyalty points"""
    print("\n=== Get Loyalty Points ===")
    
    agent = MCDAgent(token="snV4IpNWwK1NcWKxqfxbtvnaM1sFywal")
    
    try:
        points = agent.get_loyalty_points()
        print("Loyalty Points:")
        print(pretty_print_json(points))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.close()


def example_get_summary():
    """Example: Get account summary"""
    print("\n=== Get Account Summary ===")
    
    agent = MCDAgent(token="snV4IpNWwK1NcWKxqfxbtvnaM1sFywal")
    
    try:
        summary = agent.get_summary()
        print("Summary:")
        print(pretty_print_json(summary))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.close()


def example_context_manager():
    """Example: Using agent as context manager"""
    print("\n=== Using Context Manager ===")
    
    try:
        with MCDAgent(token="snV4IpNWwK1NcWKxqfxbtvnaM1sFywal") as agent:
            account = agent.get_account()
            print("Account fetched successfully using context manager")
            print(pretty_print_json(account))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("McDonald's Agent - Basic Usage Examples")
    print("=======================================")
    
    # Uncomment the examples you want to run
    # example_get_account()
    # example_get_menu()
    # example_search_menu()
    # example_get_orders()
    # example_get_loyalty_points()
    # example_get_summary()
    # example_context_manager()
    
    print("\nAll examples defined. Uncomment the ones you want to run.")
