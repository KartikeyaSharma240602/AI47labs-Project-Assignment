from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("./fine_tuned_gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("./fine_tuned_gpt2")

prompt = "What is the specialization and degree of Dr. Dr. Arvinder Singh Soin from Medanta, IN?"
inputs = tokenizer.encode(prompt, return_tensors="pt")
outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
