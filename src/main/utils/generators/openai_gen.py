import json
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file in src directory
env_path = Path(__file__).parents[3] / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize the OpenAI client with API key from environment
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def generate_stream_response(request):
    try:
        data = json.loads(request.body)
        user_message = data.get("message", "").strip()
        requested_model = data.get("model", "gpt-4o-mini")
        
        if not user_message:
            yield "data: [Error: Empty message]\n\n"
            return
            
        # Handle different model types
        if requested_model == "dall-e-3":
            yield from generate_dalle_response(user_message)
        else:
            # Default to GPT model - support multiple GPT models
            model_name = requested_model if requested_model != "dall-e-3" else "gpt-4o-mini"
            yield from generate_gpt_response(user_message, model_name)

    except Exception as e:
        yield f"data: [Error: {str(e)}]\n\n"
        
def generate_dalle_response(prompt):
    """Generate an image with DALL-E and return the URL"""
    try:
        yield "data: I'm creating an image based on your description. This might take a moment...\n\n"
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        yield f"data: Here's your image: \n\n"
        yield f"data: <img src=\"{image_url}\" class=\"mt-2 rounded-lg max-w-full\" />\n\n"
        
    except Exception as e:
        yield f"data: [Error generating image: {str(e)}]\n\n"

def generate_gpt_response(prompt, model="gpt-4o-mini"):
    """Generate a text response with the specified GPT model"""
    prompt_message = "You are a helpful assistant. Please answer the following question like for a 6-14 year old: " + prompt
    
    # Using the new API format
    response_stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt_message}],
        stream=True
    )

    for chunk in response_stream:
        if chunk.choices[0].delta.content is not None:
            text_piece = chunk.choices[0].delta.content
            # Format properly as SSE (Server-Sent Events)
            yield f"data: {text_piece}\n\n"