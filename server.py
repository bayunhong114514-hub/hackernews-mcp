import json

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hackernews-mcp")

MOCK_STORIES = [
    {"id": 1, "title": "Show HN: I built a tiny MCP server", "url": "https://example.com/mcp", "score": 512},
    {"id": 2, "title": "Ask HN: What are you working on this week?", "url": None, "score": 328},
    {"id": 3, "title": "Rust 2.0 roadmap announced", "url": "https://example.com/rust", "score": 891},
    {"id": 4, "title": "Why local-first software matters", "url": "https://example.com/local-first", "score": 445},
    {"id": 5, "title": "Postgres tips from production", "url": "https://example.com/pg", "score": 267},
    {"id": 6, "title": "The rise of AI agents in 2026", "url": "https://example.com/agents", "score": 703},
    {"id": 7, "title": "A deep dive into SQLite internals", "url": "https://example.com/sqlite", "score": 389},
    {"id": 8, "title": "Open source LLM tooling roundup", "url": "https://example.com/llm", "score": 214},
    {"id": 9, "title": "How we cut API latency by 80%", "url": "https://example.com/latency", "score": 556},
    {"id": 10, "title": "Writing a kernel module in Zig", "url": "https://example.com/zig", "score": 178},
]

@mcp.tool()
def get_top_stories(limit: int = 10) -> str:
    """获取 Hacker News 当前热门故事（mock 数据）。"""
    n = max(1, min(limit, len(MOCK_STORIES)))
    return json.dumps(MOCK_STORIES[:n], ensure_ascii=False, indent=2)

if __name__ == "__main__":
    mcp.run()

# python -c "from server import get_top_stories; print(get_top_stories(3))"