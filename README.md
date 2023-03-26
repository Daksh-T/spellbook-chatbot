# AI Chatbot powered by Spellbook

A simple chatbot app that uses [Spellbook API](https://spellbook.scale.com/) for access to OpenAI models. You must have Spellbook API access for this to work.

## Versions
``promptmachine.py`` generates outputs seperately for each prompt

``chat.py`` uses the full context of the conversation

## Setup

1. Create an app at [Spellbook Dashboard](https://spellbook.scale.com/) and then create a 'Prompt' using the model of your choice. You must use ``{{input}}`` as the variable name. An example prompt is
```
Complete the next response in this chat

{{input}}
```

2. Deploy this prompt and copy the URL and API Key from the Deployment page

3. Replace the ``<API Key>`` with your API Key you copied earlier and ``<Endpoint URL>`` with your Endpoint URL.
For example:
```python
    headers = {"Authorization": "Basic abcdefgh1234abc"}
    response = requests.post(
        "https://dashboard.scale.com/spellbook/api/v2/zy123xw",
```

## Disclaimer

This program is released under a GPL v3 license and comes with NO WARRANTY whatsover. I request you to create a pull request or issue if you find anything that doesn't work as expected!
