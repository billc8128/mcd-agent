"""MCP API Client for McDonald's"""

import json
import logging
from typing import Any, Dict, List, Optional
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import Config

logger = logging.getLogger(__name__)


class MCPClient:
    """McDonald's MCP API Client"""
    
    def __init__(self, config: Config):
        """Initialize MCP Client
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.session = self._create_session()
        self.base_url = config.api_url
        self.headers = {
            "Authorization": f"Bearer {config.mcp_token}",
            "Content-Type": "application/json",
            "User-Agent": "MCDAgent/1.0"
        }
    
    def _create_session(self) -> requests.Session:
        """Create requests session with retry strategy"""
        session = requests.Session()
        
        # Set up retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        return session
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request to MCP API
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            **kwargs: Additional request parameters
        
        Returns:
            Response data as dictionary
        
        Raises:
            requests.RequestException: If request fails
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            if self.config.debug:
                logger.debug(f"{method} {url}")
            
            response = self.session.request(
                method,
                url,
                headers=self.headers,
                timeout=self.config.timeout,
                **kwargs
            )
            response.raise_for_status()
            
            return response.json() if response.content else {}
        
        except requests.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise
    
    def get_menu(self, **kwargs) -> Dict[str, Any]:
        """Get menu items
        
        Returns:
            Menu data
        """
        return self._request("GET", "/menu", **kwargs)
    
    def search_menu(self, keyword: str, **kwargs) -> Dict[str, Any]:
        """Search menu items
        
        Args:
            keyword: Search keyword
        
        Returns:
            Search results
        """
        return self._request(
            "GET",
            "/menu/search",
            params={"q": keyword},
            **kwargs
        )
    
    def get_orders(self, **kwargs) -> Dict[str, Any]:
        """Get user orders
        
        Returns:
            Order list
        """
        return self._request("GET", "/orders", **kwargs)
    
    def get_order(self, order_id: str, **kwargs) -> Dict[str, Any]:
        """Get specific order details
        
        Args:
            order_id: Order ID
        
        Returns:
            Order details
        """
        return self._request("GET", f"/orders/{order_id}", **kwargs)
    
    def get_account(self, **kwargs) -> Dict[str, Any]:
        """Get account information
        
        Returns:
            Account data
        """
        return self._request("GET", "/account", **kwargs)
    
    def get_loyalty_points(self, **kwargs) -> Dict[str, Any]:
        """Get loyalty points
        
        Returns:
            Loyalty points data
        """
        return self._request("GET", "/account/loyalty", **kwargs)
    
    def get_stores(self, **kwargs) -> Dict[str, Any]:
        """Get nearby stores
        
        Returns:
            Store list
        """
        return self._request("GET", "/stores", **kwargs)
    
    def place_order(self, items: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """Place an order
        
        Args:
            items: List of items to order
        
        Returns:
            Order confirmation
        """
        return self._request(
            "POST",
            "/orders",
            json={"items": items},
            **kwargs
        )
    
    def close(self):
        """Close the session"""
        if self.session:
            self.session.close()
