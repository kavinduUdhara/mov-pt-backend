from vertexai import agent_engines

# 1. Get your app
adk_app = agent_engines.get("7560110011192442880")

# 2. List (or create) a session for your user
se_list = adk_app.list_sessions(user_id="001")
if not se_list.get("sessions"):
    # no sessions yet, so create one
    session = adk_app.create_session(user_id="001")
    session_id = session["id"]
else:
    session_id = se_list["sessions"][0]["id"]

print(session_id)
# 3. Stream your query into *that* session
for event in adk_app.stream_query(
    user_id="001",
    session_id=session_id,               # use the real variable here
    message="""
    {"text": "can you give me reference for that percentage"}
    """
):
    print(event)

