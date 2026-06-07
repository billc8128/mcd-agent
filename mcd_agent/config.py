"""Configuration management for MCD Agent"""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    """MCD Agent Configuration"""
    
    mcp_token: str
    api_url: str = "https://mcp.mcd.cn"
    timeout: int = 30
    debug: bool = False
    
    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables"""
        mcp_token = os.getenv("MCD_MCP_TOKEN")
        if not mcp_token:
            raise ValueError("MCD_MCP_TOKEN environment variable is not set")
        
        return cls(
            mcp_token=mcp_token,
            api_url=os.getenv("MCD_API_URL", "https://mcp.mcd.cn"),
            timeout=int(os.getenv("MCD_TIMEOUT", "30")),
            debug=os.getenv("MCD_DEBUG", "false").lower() == "true"
        )
    
    @classmethod
    def create(cls, token: str, **kwargs) -> "Config":
        """Create configuration with custom parameters"""
        return cls(mcp_token=token, **kwargs)
