# hackernews-mcp

AI Friendly MCP Server for Hacker News. Get current top stories — no API key required.

## Tools

| Tool | Description | Arguments |
|------|-------------|-----------|
| `get_top_stories` | Current top stories from HN | `limit` (int, default 10, max 30) |

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python server.py
```

## Config

```json
{
  "mcpServers": {
    "hackernews": {
      "command": "python",
      "args": ["/absolute/path/to/hackernews-mcp/server.py"]
    }
  }
}
```

## Keywords

「帮我看一下 Hacker News 现在的热门」
「用 MCP 拉一下 HN top stories」
「获取 Hacker News 前 10 条」
「调用 get_top_stories」
「用 hackernews 这个 MCP 查一下」

## License

MIT
