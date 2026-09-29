V1
This is the simple chat bot involving:
->local Ollama runtime and gemma3:4b model
If you want to connect to the cloud Ollama add authentication (api_key)

v2.1
Have added a conversational memory in the form of python list (holding list of key value pair as role, content)
Bot can remember as long as the bot is running and for the next time execution a fresh convo starts
limitation: looses convo once the program closes
            persistant memory not available 
            can hold capacity only equivalent to list

v2.2
have added persistant memory using a built in module sqlite3
deosn't loose the convo when the program closes
limitations: The conversation keeps getting bigger and hence Context-window limitation
             We're retrieving everything, rather than retrieving what is relevant.
             More tokens = more computation = more cost
             SQLite doesn't understand meaning
             

