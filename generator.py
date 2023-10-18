import openai


for i in range(1000):
    # Use ChatCompletion to generate a random dish.
    # Temperature is set at 0.8 for creativity and randomness.
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Fill in the following format with a dish from a random country with ingredients: 'country;dish;ingredients "}],
                temperature=0.8,
                max_tokens=1000,
                stop=["END"]
            )
    
    # Write the data into a CSV format.
    with open("responses.csv", "a+") as outfile:
        outfile.write(response["choices"][0]["message"]["content"]+"\n") 
