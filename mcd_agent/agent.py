"""Main MCDAgent class"""

import logging
from typing import Any, Dict, List, Optional

from .config import Config
from .mcp_client import MCPClient

logger = logging.getLogger(__name__)


class MCDAgent:
    """McDonald's Data Agent
    
    This agent connects to McDonald's API through MCP and provides
    convenient access to menu, orders, and account information.
    """
    
    def __init__(self, token: str = None, config: Config = None, **kwargs):
        """Initialize MCDAgent
        
        Args:
            token: MCP token (if config is not provided)
            config: Config object
            **kwargs: Additional config parameters
        """
        if config is None:
            if token is None:
                config = Config.from_env()
            else:
                config = Config.create(token, **kwargs)
        
        self.config = config
        self.client = MCPClient(config)
        logger.info("MCDAgent initialized successfully")
    
    # Menu Operations
    def get_menu(self, **kwargs) -> Dict[str, Any]:
        """Get all menu items
        
        Returns:
            Menu data containing all available items
        """
        logger.info("Fetching menu...")
        return self.client.get_menu(**kwargs)
    
    def search_menu(self, keyword: str, **kwargs) -> Dict[str, Any]:
        """Search menu items by keyword
        
        Args:
            keyword: Search keyword (e.g., 'burger', 'chicken')
        
        Returns:
            Matching menu items
        """
        logger.info(f"Searching menu for: {keyword}")
        return self.client.search_menu(keyword, **kwargs)
    
    # Order Operations
    def get_orders(self, **kwargs) -> Dict[str, Any]:
        """Get user's order history
        
        Returns:
            List of orders
        """
        logger.info("Fetching orders...")
        return self.client.get_orders(**kwargs)
    
    def get_order(self, order_id: str, **kwargs) -> Dict[str, Any]:
        """Get specific order details
        
        Args:
            order_id: ID of the order
        
        Returns:
            Order details
        """
        logger.info(f"Fetching order: {order_id}")
        return self.client.get_order(order_id, **kwargs)
    
    def place_order(self, items: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """Place a new order
        
        Args:
            items: List of items to order, each should contain:
                - id: Item ID
                - quantity: Quantity
                - customizations: Optional customizations
        
        Returns:
            Order confirmation with order ID and total price
        """
        logger.info(f"Placing order with {len(items)} items...")
        return self.client.place_order(items, **kwargs)
    
    # Account Operations
    def get_account(self, **kwargs) -> Dict[str, Any]:
        """Get account information
        
        Returns:
            Account data including name, email, phone, etc.
        """
        logger.info("Fetching account information...")
        return self.client.get_account(**kwargs)
    
    def get_loyalty_points(self, **kwargs) -> Dict[str, Any]:
        """Get loyalty points balance
        
        Returns:
            Loyalty points information
        """
        logger.info("Fetching loyalty points...")
        return self.client.get_loyalty_points(**kwargs)
    
    # Store Operations
    def get_stores(self, latitude: float = None, longitude: float = None, 
                  radius: int = None, **kwargs) -> Dict[str, Any]:
        """Get nearby stores
        
        Args:
            latitude: Latitude (optional)
            longitude: Longitude (optional)
            radius: Search radius in km (optional)
        
        Returns:
            List of nearby stores
        """
        logger.info("Fetching nearby stores...")
        params = {}
        if latitude is not None:
            params['lat'] = latitude
        if longitude is not None:
            params['lng'] = longitude
        if radius is not None:
            params['radius'] = radius
        
        if params:
            kwargs['params'] = {**kwargs.get('params', {}), **params}
        
        return self.client.get_stores(**kwargs)
    
    # Summary Methods
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of account and recent orders
        
        Returns:
            Summary data
        """
        logger.info("Generating account summary...")
        try:
            return {
                'account': self.get_account(),
                'loyalty_points': self.get_loyalty_points(),
                'recent_orders': self.get_orders(limit=5)
            }
        except Exception as e:
            logger.error(f"Error generating summary: {e}")
            raise
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()
    
    def close(self):
        """Close the agent and cleanup resources"""
        logger.info("Closing MCDAgent...")
        if self.client:
            self.client.close()
