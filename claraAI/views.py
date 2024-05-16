from models import SessionLog
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain_core.prompts.prompt import PromptTemplate
from django.db import transaction
from models import SessionLog
import uuid

def process_ai_request(session_id, messages, models):
    responses = []
    with transaction.atomic():
        for message, model_name in zip(messages, models):
            # Update the model if necessary
            if llm.model != model_name:
                llm = Ollama(model=model_name)
            
            prompt = PromptTemplate.from_template(message)
            chain = LLMChain(llm=llm, prompt=prompt)
            response = chain.invoke()
            responses.append(response)
            
            # Log each response separately
            SessionLog.objects.create(session_id=uuid.UUID(session_id), request_data=message, response_data=response)
        
        # Update the session status and responses after processing all messages
        sessions[session_id]["status"] = "complete"
        sessions[session_id]["responses"] = responses