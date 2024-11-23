import json
from gql import gql, Client
from datetime import datetime
from gql.transport.aiohttp import AIOHTTPTransport

from vibbo_stats.query import vibboThreadsQuery
from vibbo_stats.metrics import print_metrics

headers = {
    "Cookie": "TODO: Get cookie from browser when logged in"
}

if "TODO" in headers["Cookie"]:
    raise ValueError("You need to replace the 'TODO' in the headers with a valid cookie")

transport = AIOHTTPTransport(url="https://vibbo.no/graphql?name=vibboThreadBySlug", headers=headers)
client = Client(transport=transport, fetch_schema_from_transport=False)
query = gql(vibboThreadsQuery)


messages = []

after_date = f"{datetime.now().isoformat()}Z"
start_2024 = f"{datetime(2024, 1, 1).isoformat()}Z"
while after_date >= start_2024:
    print(f"Getting messages after {after_date}")
    variables = {
        "afterDate": after_date,
        "search": "",
        "organizationId": "toyenparken-boligselskap",
        "boardPerspective": True,
        "status": "ANSWERED",
        "limit": 25
    }

    result = client.execute(query, variables, "vibboThreadsQuery")
    threads = result["organization"]["threads"]["threads"]

    for thread in threads:
        messages += thread["messages"]
    after_date = threads[-1]["lastMessageAt"]

with open("dump.json", "w+") as f:
    f.write(json.dumps(messages, indent=4))

print_metrics(messages)