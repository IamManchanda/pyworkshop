greetings_with_dict = {
    "English": "Hello", 
    "French": "Bonjour", 
    "Spanish": "Holo", 
    "Hindi": "Namastey", 
    "Punjabi": "Shat Shri Akal",
}

for index, (key, value) in enumerate(greetings_with_dict.items()):
    print(f"{ index + 1 }: { key } - { value }, Mr Manchanda.")
