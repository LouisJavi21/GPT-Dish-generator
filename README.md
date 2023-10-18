# GPT-dish-generator

Three pieces of code together to generate a dataset of random dishes with country of origin and ingredients.
The visualization can be found here:
https://graphcommons.com/graphs/b7390b42-1001-43fb-85a9-f8425476d0ca

# How-to

To generate the data the generator should first be run. This script needs an OPEN-API key to run.
Use: ```export OPENAI_API_KEY="YOUR KEY HERE"```
Before running the generator.

The cleaner after this preprocesses the CSV data from the generator. Run this after GPT has generated the data.

The last one is the structurer, this would structure the JSON dataset from the cleaner into 2 CSV files that can be used by GraphCommons. Nodes and Edges.

# Notes
This is a small project for the Datawise minor of the RUG to explore the use of GPT to generate datasets.
