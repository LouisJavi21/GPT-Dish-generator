# GPT-dish-generator

The three pieces of code together generate a dataset of random dishes with country of origin and ingredients.
The visualization of it can be found here:
https://graphcommons.com/graphs/b7390b42-1001-43fb-85a9-f8425476d0ca

# How-to
1. The generator.py generates the raw dataset itself. Before running it an OPENAI API Key should be given as follows: ```export OPENAI_API_KEY="YOUR KEY HERE"```
2. When the raw dataset got generated the cleaner.py will preprocess the CSV from the generator.py. Note that it does not clean all cases.
3. The last script is the structurer.py, this structures the JSON dataset from the cleaner.py into Nodes and Edges CSV files that can be used by GraphCommons.

# Notes
This is a small project for the Datawise minor of the RUG to explore the use of GPT to generate datasets.
