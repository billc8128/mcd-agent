# 🍔 McDonald's Agent - Setup Guide

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/billc8128/mcd-agent.git
cd mcd-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your Token

```bash
cp .env.example .env
```

Edit `.env` and add your McDonald's MCP Token:

```
MCD_MCP_TOKEN=snV4IpNWwK1NcWKxqfxbtvnaM1sFywal
MCD_API_URL=https://mcp.mcd.cn
MCD_TIMEOUT=30
MCD_DEBUG=false
```

### 4. Run Examples

```bash
python examples/basic_usage.py
```

## Integration with Claude / ChatGPT

### Method 1: Direct Python Integration

```python
from mcd_agent import MCDAgent

# Initialize the agent
agent = MCDAgent(token="your_token_here")

# Query data
account = agent.get_account()
menu = agent.get_menu()
orders = agent.get_orders()

# Don't forget to close
agent.close()
```

### Method 2: As Context Manager

```python
from mcd_agent import MCDAgent

with MCDAgent(token="your_token_here") as agent:
    # All operations here
    account = agent.get_account()
    menu = agent.get_menu()
    # Automatically closes when exiting the context
```

### Method 3: MCP Server Setup

1. Install MCP SDK:
```bash
pip install mcp
```

2. Create `mcp_server.py`:
```python
from mcp.server import Server
from mcd_agent import MCDAgent

app = Server("mcd-agent")
agent = MCDAgent()

@app.call_tool()
def get_account():
    return agent.get_account()

@app.call_tool()
def get_menu():
    return agent.get_menu()

# Add more tools...
```

3. Configure in Claude/ChatGPT as MCP Server:
```json
{
  "mcp_servers": [
    {
      "name": "mcd-agent",
      "url": "http://localhost:3000",
      "token": "your_mcp_token"
    }
  ]
}
```

## Available Functions

### Account Operations
- `get_account()` - Get account information
- `get_loyalty_points()` - Get loyalty points balance
- `get_summary()` - Get comprehensive summary

### Menu Operations
- `get_menu()` - Get all menu items
- `search_menu(keyword)` - Search menu items

### Order Operations
- `get_orders()` - Get order history
- `get_order(order_id)` - Get specific order
- `place_order(items)` - Place new order

### Store Operations
- `get_stores()` - Get nearby stores
- `get_stores(latitude, longitude, radius)` - Get stores by location

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `MCD_MCP_TOKEN` | Yes | Your McDonald's MCP Token |
| `MCD_API_URL` | No | API endpoint (default: https://mcp.mcd.cn) |
| `MCD_TIMEOUT` | No | Request timeout in seconds (default: 30) |
| `MCD_DEBUG` | No | Enable debug logging (default: false) |

## Error Handling

```python
from mcd_agent import MCDAgent
import logging

logging.basicConfig(level=logging.INFO)

try:
    agent = MCDAgent(token="your_token")
    orders = agent.get_orders()
except Exception as e:
    print(f"Error: {e}")
finally:
    agent.close()
```

## Troubleshooting

### Token Not Working
- Verify your MCP Token is correct
- Check that the token hasn't expired
- Regenerate token from https://open.mcd.cn/mcp

### Connection Issues
- Verify API URL is correct
- Check network connectivity
- Enable debug mode: `MCD_DEBUG=true`

### Rate Limiting
- The client has automatic retry logic
- Default retry strategy: 3 attempts with exponential backoff

## Security Best Practices

1. **Never commit `.env` to version control**
   - Add `.env` to `.gitignore`

2. **Use environment variables in production**
   ```bash
   export MCD_MCP_TOKEN="your_token"
   ```

3. **Rotate tokens regularly**
   - Regenerate from https://open.mcd.cn/mcp

4. **Use over HTTPS only**
   - API endpoint is https://mcp.mcd.cn

## License

MIT License - See LICENSE file for details

## Support

For issues or questions:
1. Check the examples in `/examples`
2. Review API documentation
3. Open an issue on GitHub
