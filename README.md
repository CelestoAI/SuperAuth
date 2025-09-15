# ant 🐜

Simplest way to use APIs for your enterprise apps and services like Google, Notion, Hubspot, Apollo, etc. 🚀

MCP server coming soon.

## Quick Start

### Install

Install the latest version:

```bash
pip install git+https://github.com/celestoai/ant.git
```

Setup your API keys in the environment variables:

```bash
APOLLO_API_KEY=your_apollo_api_key
```

### Apollo.io Example

Find contacts in your Apollo.io account by keywords.

```python
from ant.apollo_io import Apollo

apollo = Apollo()
response = apollo.contact.search("John Doe")
print(response)
```

## How to run tests

`uv run pytest`
