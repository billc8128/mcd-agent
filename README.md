# 🍔 McDonald's Data Agent

A powerful AI agent that connects to your McDonald's data through MCP (Model Context Protocol).

## 📋 Features

- 🔗 **Connected to McDonald's API** - Access your account data directly
- 📊 **Data Integration** - Query menus, orders, and account information
- 🤖 **AI-Powered** - Built with MCP for seamless integration
- ⚡ **Real-time Access** - Get live data from McDonald's servers

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- McDonald's MCP Token
- MCP SDK

### Installation

```bash
git clone https://github.com/billc8128/mcd-agent.git
cd mcd-agent
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file in the root directory:

```bash
MCD_MCP_TOKEN=snV4IpNWwK1NcWKxqfxbtvnaM1sFywal
MCD_API_URL=https://mcp.mcd.cn
```

2. Initialize the agent:

```python
from mcd_agent import MCDAgent

agent = MCDAgent(token="YOUR_MCP_TOKEN")
```

## 📚 Usage

### Query Menu

```python
# Get all menu items
menu = agent.get_menu()

# Search for items
burgers = agent.search_menu(keyword="burger")
```

### Check Orders

```python
# Get order history
orders = agent.get_orders()

# Get specific order details
order = agent.get_order(order_id="123456")
```

### Account Information

```python
# Get account info
account = agent.get_account()

# Get loyalty points
points = agent.get_loyalty_points()
```

## 🏗️ Architecture

```
mcd-agent/
├── mcd_agent/
│   ├── __init__.py
│   ├── agent.py          # Main agent class
│   ├── mcp_client.py     # MCP API client
│   ├── config.py         # Configuration management
│   └── utils.py          # Utility functions
├── tests/
│   └── test_agent.py
├── requirements.txt
├── .env.example
└── README.md
```

## 🔐 Security

- Your MCP Token is stored securely in `.env`
- Never commit `.env` to version control
- Use environment variables for production

## 📖 Documentation

For more details, check out:
- [MCP Documentation](https://open.mcd.cn/mcp)
- [API Reference](https://open.mcd.cn/api/docs)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License

## 🙋 Support

If you have any questions, please open an issue!
