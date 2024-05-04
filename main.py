import chainlit as cl
import litellm
import re
from typing import Dict, Optional

GREETING_PATTERNS = [
    r"^hi$|^hello$|^hey$",
    r"^good\s*(morning|afternoon|evening|night)$",
    r"^how\s+are\s+you\??$",
]

def google_serp_api(query):
    api_key = "API_KEY"
    url = f"https://api.scaleserp.com/search?api_key={api_key}&q={query}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['organic_results'][0]['snippet'] if data['organic_results'] else "No results found"

@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    return default_user

@cl.on_chat_start
def start_chat():
  post_prompt = "If this is not related to medicine, just return 'I don\'t know'"
  system_message = {
    "role": "system", 
    "content": "You are a helpful medical assistant who tries their best to answer questions. If the question is not about medical advice, please let the user know.",
    "post_prompt": post_prompt
  }
  cl.user_session.set("message_history", [system_message])

@cl.on_message
async def on_message(message: cl.Message):
  messages = cl.user_session.get("message_history")

  for pattern in GREETING_PATTERNS:
    if re.match(pattern, message.content.lower()):
        greeting_response = (
            "Hello! I'm a medical chatbot. How can I assist you today?"
        )
        await cl.Message(content=greeting_response).send()
        return
        
  if len(message.elements) > 0:
    for element in message.elements:
      with open(element.path, "r") as uploaded_file:
        content = uploaded_file.read()
      messages.append({"role": "user", "content": content})
      confirm_message = cl.Message(content=f"Uploaded file: {element.name}")
      await confirm_message.send()

  msg = cl.Message(content="")
  await msg.send()
  
  messages.append({"role": "user", "content": message.content + "If my question is not related to medical advice, please respond. I don\'t know."})

  response = await litellm.acompletion(
    model="ollama/medllama2",
    messages = [
        {"role": "system", "content": "You are a helpful medical assistant who tries their best to answer questions. If the question is not about medical advice, please let the user know."},
        {"role": "user", "content": message.content}
    ],
    api_base="http://localhost:11434",
    stream=True
  )

  async for chunk in response:
    if chunk:
      content = chunk.choices[0].delta.content
      if content:
        await msg.stream_token(content)

  messages.append({"role": "assistant", "content": msg.content})
  await msg.update()