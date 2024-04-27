import openai
import os


save_path = 'C:/Users/justi/Documents/stories/'

# Set your OpenAI API key here
openai.api_key = os.environ["OPENAI_API_KEY"]

outline_prompt = " ".join(
    [
        "You are to take the role of an expert author who writes works of fiction",
        "The first line of your response will consist only of a title for the story"
        "Next you will write a 1000 word overview of a story including brief details of the main characters."
        "Finally you will return a list of precisely 10 chapter headings each on their own line.",
        "Please respond to the following prompt:",
    ]
)

def generate_story_outline_and_chapters(prompt):
    # Generate a 1000-word story outline and list of ten chapters
    response = openai.ChatCompletion.create(
        engine="gpt-4-turbo-preview",  # or the latest available version
        # prompt=prompt,
        messages=[
            {
                "role": 'assistant', 
                "content":outline_prompt ,
            }
        ]+[
            {
                "role": "user", 
                "content": prompt,
            }
        ],
        max_tokens=4000,  # Adjust based on the model's limits and your requirements
        stream=True,
        n=1,
        stop=None,
        temperature=0.7,
    )
    story_outline = response.choices[0].text.strip()

    # Save the story outline to a file
    file_location = os.path.join(save_path, "Summary.txt")

    with open(file_location, 'w') as f:
        f.write(story_outline)
    print("Story outline saved to story_outline.txt")
    print(story_outline)
    user_prompt = input("Continue with story Y/N?")
    if user_prompt.lower() != "y":
        exit()

    with open(file_location) as my_file:
        outline = my_file.read()

    # Assuming the outline includes a clear list of chapter titles, we parse these
    # This is a simplification; you might need more sophisticated parsing based on your output
    chapters = outline.split('\n')[-10:]  # Assuming the last 10 lines are chapter titles

    chapter_writing_prompt = " ".join(
    [
        "You are to take the role of an expert author who writes works of fiction",
        "Given an overview of the desired story and a list of chapter headings, please write the chapter requested by the user.",
        "Each chapter must be no more than 2500 words long.Overall there are 10 chapters"
    ]
    )

    precis =  " ".join(
        [
            "Here is the outline and the chapter names",
            outline
        ]
    )

    # Generate and save each chapter
    for i, chapter_title in enumerate(chapters, start=1):
        chapter_prompt = f"Write the chapter entitled: {chapter_title}. This is chapter {i} of 10. Please bear in mind that the previous chapter went as follows {chapter_response}"
        chapter_response = openai.ChatCompletion.create(
            engine="gpt-4-turbo-preview",
            # prompt=chapter_prompt,
            messages=[
                {
                    "role": 'assistant', 
                    "content":chapter_writing_prompt ,
                }
            ]+[
                 {
                    "role": 'assistant', 
                    "content":precis,
                }
            ]+[
                {
                    "role": "user", 
                    "content": chapter_prompt,
                }
            ],
            max_tokens=4000,  # Adjust as needed
            stream=True,
            n=1,
            stop=None,
            temperature=0.7,
        )
        chapter_text = chapter_response.choices[0].text.strip()

        # Save the chapter to a file
        chapter_filename = f'chapter_{i}.txt'
        chapter_location = os.path.join(chapter_filename, chapter_filename)
        with open(chapter_location, 'w') as f:
            f.write(chapter_text)
        print(f"Chapter {i} saved to {chapter_filename}")
        print(chapter_text)

    print("All chapters have been written and saved.")

if __name__ == "__main__":
    # user_prompt = input("Enter your story prompt: ")
    user_prompt =   " ".join(
        [
            "Please create a story about three British able seamen called John, Andrew and William during the age of sail.",
            "The three are friends aboard the frigate HMS Rose, a sailing vessel during the start of the Napoleonic Wars ",
            "The tale will tell of shipboard life under officers both good and bad.",
            "It will also cover their adventures on ship and ashore, including lovers in port, and storms, naval discipline, and battles at sea.",
        ]
    ) 
    generate_story_outline_and_chapters(user_prompt)