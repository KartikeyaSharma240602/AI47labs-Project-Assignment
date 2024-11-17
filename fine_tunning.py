from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Tokenize your dataset
train_path = "training_data.txt"  # Your preprocessed text file
valid_path = "validation_data.txt"

def load_dataset(path, tokenizer, block_size=128):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return TextDataset(
        tokenizer=tokenizer,
        file_path=path,
        block_size=block_size,
        overwrite_cache=True,
    )

train_dataset = load_dataset(train_path, tokenizer)
valid_dataset = load_dataset(valid_path, tokenizer)

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

# Training arguments
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=500,
    save_total_limit=2,
    logging_dir="./logs",
    learning_rate=5e-5,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=valid_dataset,
)

# Train
trainer.train()


model.save_pretrained("./fine_tuned_gpt2")
tokenizer.save_pretrained("./fine_tuned_gpt2")