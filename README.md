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

### Google API

Authenticate Gmail or Google Calendar to read, and send emails or send a calendar invite.

```python
from ant.google import GmailAPI, load_user_credentials

# Load your saved credentials
creds = load_user_credentials("credentials.my_google_account.json")

# Direct tool usage
gmail = GmailAPI(creds)
messages = gmail.search_messages(query="from:github.com", limit=10)
```


## How to run tests

`uv run pytest`
