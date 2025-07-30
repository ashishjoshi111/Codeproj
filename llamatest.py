from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Replace with the actual model name
model_name = "Llama3.1-8B-Instruct\Meta-Llama-3.1-8B-Instruct" 

# Load the model and tokenizer
try:
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    exit()

# Create a pipeline for text generation
try:
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device_map="auto")
except Exception as e:
    print(f"Error creating pipeline: {e}")
    exit()

# Example prompt
prompt = "Write a short poem about a cat."

# Generate text
try:
  sequences = pipe(prompt, max_length=100, num_return_sequences=1)
  print(sequences[0]['generated_text'])
except Exception as e:
  print(f"Error generating text: {e}")