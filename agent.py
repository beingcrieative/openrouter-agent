from dotenv import load_dotenv
import os
import requests
import json
import logfire
import traceback
import time

# Load environment variables
load_dotenv()

# Configure logfire
os.environ['LOGFIRE_TOKEN'] = os.getenv('LOGFIRE_PROJECT_TOKEN')
logfire.configure(send_to_logfire='always')

# Get API key
api_key = os.getenv('OPENROUTER_API_KEY')
if api_key:
    print(f"API key found: {api_key[:8]}...{api_key[-4:]}")
    logfire.info('api_key_loaded', masked_key=f"{api_key[:8]}...{api_key[-4:]}")
else:
    print("No API key found!")
    logfire.error('api_key_missing')
    exit(1)

class OpenRouterAgent:
    def __init__(self, model, system_prompt):
        self.model = model
        self.system_prompt = system_prompt
        self.api_key = api_key
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        logfire.info('agent_initialized', 
            model=model,
            system_prompt_length=len(system_prompt)
        )
        
    def run_sync(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "http://localhost",
            "X-Title": "Basic Gemini Agent"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ]
        }
        
        response = None
        start_time = time.time()
        try:
            logfire.info('openrouter_request_start',
                model=self.model,
                prompt_length=len(prompt),
                system_prompt_length=len(self.system_prompt),
                prompt=prompt,
                system_prompt=self.system_prompt
            )
            
            response = requests.post(self.base_url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            
            # Extract useful metrics
            response_content = result['choices'][0]['message']['content'].strip()
            total_tokens = result.get('usage', {}).get('total_tokens', 0)
            prompt_tokens = result.get('usage', {}).get('prompt_tokens', 0)
            completion_tokens = result.get('usage', {}).get('completion_tokens', 0)
            
            # Calculate response time
            response_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            
            # Log successful response metrics
            logfire.info('openrouter_response', 
                model=self.model,
                prompt_length=len(prompt),
                response_length=len(response_content),
                total_tokens=total_tokens,
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                response_time_ms=response_time,
                success=True,
                response_content=response_content
            )
            
            return response_content
                
        except Exception as e:
            error_msg = str(e)
            response_text = response.text if response and response.text else "No response"
            
            # Log detailed error information
            logfire.error('openrouter_error',
                error=error_msg,
                model=self.model,
                prompt_length=len(prompt),
                response_text=response_text,
                traceback=traceback.format_exc()
            )
            
            # Try to extract content even if there was an error
            if response and response.text:
                try:
                    result = response.json()
                    if 'choices' in result and len(result['choices']) > 0:
                        return result['choices'][0]['message']['content'].strip()
                except:
                    pass
                    
            print(f"Response: {response_text}")
            return None

try:
    # Create the agent
    agent = OpenRouterAgent(
        'google/gemini-2.0-flash-exp:free',
        'You are a helpful assistant that provides concise answers.'
    )

    def main():
        try:
            # Test the agent with a simple question
            print("\nSending request to OpenRouter...")
            start_time = time.time()
            
            response = agent.run_sync("What can you tell me about yourself?")
            
            if response:
                print("\nAgent response:", response)
                logfire.info('agent_response_received',
                    response_length=len(response),
                    total_time_ms=(time.time() - start_time) * 1000
                )
        except Exception as e:
            error_msg = str(e)
            logfire.error('agent_error', 
                error=error_msg,
                traceback=traceback.format_exc()
            )
            print(f"Error during agent execution: {error_msg}")

    if __name__ == "__main__":
        main()

except Exception as e:
    error_msg = str(e)
    logfire.error('agent_creation_error',
        error=error_msg,
        traceback=traceback.format_exc()
    )
    print(f"Error creating agent: {error_msg}")