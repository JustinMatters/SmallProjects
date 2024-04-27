import openai
import os
openai.api_key = os.environ["OPENAI_API_KEY"]

help( openai.ChatCompletion.create)

# outline_prompt = " ".join([
#     "You are to take the role of an expert author who writes works of fiction.",
#     "The first line of your response will consist only of a title for the story.",
#     "Next, you will write a 1000 word overview of a story including brief details of the main characters.",
#     "Finally, you will return a list of precisely 10 chapter headings each on their own line.",
#     "Please respond to the following prompt:",
# ])

# user_prompt = " ".join([
#     "Please create a story about three British able seamen called John, Andrew, and William during the age of sail.",
#     "The three are friends aboard the frigate HMS Rose, a sailing vessel during the start of the Napoleonic Wars.",
#     "The tale will tell of shipboard life under officers both good and bad.",
#     "It will also cover their adventures on ship and ashore, including lovers in port, and storms, naval discipline, and battles at sea.",
# ])

# stream = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[{"role": "assistant", "content": outline_prompt},{"role": "user", "content": user_prompt}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.get("content", "") is not None:
#         print(chunk.choices[0].delta.get("content", ""), end="")