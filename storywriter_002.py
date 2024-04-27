import openai
import os

save_path = 'C:/Users/justi/Documents/stories/'

outline_prompt = " ".join([
    "You are to take the role of an expert author who writes works of fiction.",
    "The first line of your response will consist only of a title for the story.",
    "Next, you will write a 1000 word overview of a story including brief details of the main characters.",
    "Finally, you will return a list of precisely 10 chapter headings each on their own line.",
    "Please respond to the following prompt:",
])

user_prompt = " ".join([
        "Please create a story about three British able seamen called John, Andrew, and William during the age of sail.",
        "The three are friends aboard the frigate HMS Rose, a sailing vessel during the start of the Napoleonic Wars.",
        "The tale will tell of shipboard life under officers both good and bad.",
        "It will also cover their adventures on ship and ashore, including lovers in port, and storms, naval discipline, and battles at sea.",
])

# def generate_story_outline_and_chapters(prompt):
    # Set your OpenAI API key here
openai.api_key = os.environ["OPENAI_API_KEY"]
story_outline = ""
stream =  openai.ChatCompletion.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": 'assistant', "content": outline_prompt},
        {"role": "user", "content": user_prompt},
    ],
    stream=True,
    # max_tokens=4000,
    # temperature=0.7,
)
for chunk in stream:
    if chunk.choices[0].delta.get("content", "") is not None:
        story_outline += chunk.choices[0].delta.get("content", "")

file_location = os.path.join(save_path, "Summary.txt")
with open(file_location, 'w') as f:
    f.write(story_outline)
print("Story outline saved to Summary.txt")
print(story_outline)

user_prompt = input("Continue with story Y/N?")
if user_prompt.lower() != "y":
    exit()

with open(file_location) as my_file:
    outline = my_file.read()

chapters = outline.split('\n')[-10:]

chapter_writing_prompt = " ".join(
[
    "You are to take the role of an expert author who writes works of fiction",
    "Given an overview of the desired story and a list of chapter headings, please write the chapter requested by the user.",
    "Each chapter must be no more than 2500 words long.Overall there are 10 chapters",
    "Here is the outline and the chapter names",
    outline,
]
)

for i, chapter_title in enumerate(chapters, start=1):
    chapter_response = ""  # Initialize to handle the first iteration
    chapter_prompt = f"Write the chapter entitled: {chapter_title}. This is chapter {i} of 10."
    chapter_text = ""
    chapter_stream =  openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": 'assistant', "content": chapter_writing_prompt},
            {"role": "user", "content": chapter_prompt},
        ],
        stream=True,
        # max_tokens=4000,
        # temperature=0.7,
    )
    for chapter_chunk in chapter_stream:
        if chapter_chunk.choices[0].delta.get("content", "") is not None:
            chapter_text += chapter_chunk.choices[0].delta.get("content", "")
        # chapter_text = chapter_response.choices[0].text.strip()

    chapter_filename = f'chapter_{i}.txt'
    chapter_location = os.path.join(save_path, chapter_filename)
    with open(chapter_location, 'w') as f:
        f.write(chapter_text)
    print(f"Chapter {i} saved to {chapter_filename}")

print("All chapters have been written and saved.")

# if __name__ == "__main__":

#     generate_story_outline_and_chapters(user_prompt)