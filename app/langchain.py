import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.8)


def generate_lk_bio(professional_experience, personalized_fact, skills):
    prompt = PromptTemplate(
        input_variables=[
            "professional_experience",
            "personalized_fact",
            "skills",
        ],
        template="Generate a clear,concise,professional but -->personal<-- linkedin bio (in english)"
        " about a person based on"
        " the following person's information: {professional_experience},{personalized_fact},{skills}."
        "Make sure to:"
        "- check your dataset for what makes a good linkedin bio;"
        "- do not simply repeat what the information says, but identify how the"
        "information relates with each other -> it is important to create a bio that values"
        "the owner of the bio;"
        "- make sure to compare and identify soft and hard skills, and treat them as such. see how they relate"
        " with each other and how they correlate with the whole context of the person's experience."
        "- if there isn't enough information on what the user has done or accomplished, do not make up"
        " information. Simply correlate the information available with the context provided and create a"
        " clear and concise bio.",
    )
    formatted_prompt = prompt.format(
        professional_experience=professional_experience,
        personalized_fact=personalized_fact,
        skills=skills,
    )
    return llm(formatted_prompt)
