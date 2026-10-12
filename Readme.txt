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
             

V3.1 RAG pipeline with semantic retrieval engine
Have used ollama "nomic-embed-text" embedding model that generates vectors or embeddings.
comparision between vectors (input and all the documents)are done using cosine similarity
semantic search is done to retrive top k related vectors
top k context is sent to the LLM to generate response by using only the information from the context
we have considered list of python dictonaries as documents where each dictionary is a document
we have not used any memory to store the chatbot convo
use python -m app.test_rag to run this version
