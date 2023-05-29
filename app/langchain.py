import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)


def generate_lk_bio(
    professional_title, personalized_fact, background, current_role, relevant_skills
):
    prompt = PromptTemplate(
        input_variables=[
            "professional_title",
            "personalized_fact",
            "background",
            "current_role",
            "relevant_skills",
        ],
        template=" create a linkedin 'about me section'by analyzing the following user inputs and identifying"
        "how everything fits together: "
        "professional_title, personalized_fact,background, current_role and relevant skills."
        "you're going to use the 'professional_title' as context to how the summary should be formulated"
        " accordingly to the user title. professional_title:{professional_title}"
        "you're going to use relevant_skills as a way of knowing what the user knows.Then you're going to "
        "relate the"
        "answer with the whole context provided.relevant_skills:{relevant_skills}."
        "you're going to use 'personalized_fact' as a way of personalizing the summary, relating those facts"
        " with the assumed mentality of the person. personalized_fact:{personalized_fact}"
        "you're going to use 'background' as a way of making every fact work together and relate with "
        "each other, understanding the story of the person. background:{background}"
        "you're going to use 'current role' as a way of understanding what the user is learning and"
        " wants to develop knowledge in. current_role:{current_role}",
    )
    formatted_prompt = prompt.format(
        professional_title=professional_title,
        personalized_fact=personalized_fact,
        background=background,
        current_role=current_role,
        relevant_skills=relevant_skills,
    )
    return llm(formatted_prompt)
