import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)


def generate_lk_bio(
        bio_samples,
        professional_title,
        personalized_fact,
        value_creation,
        passion_motivation,
):
    prompt = PromptTemplate(
        input_variables=[
            "bio_samples"
            "professional_title",
            "personalized_fact"
            "value_creation",
            "passion_motivation",
        ],
        template="i want you to generate a linkedin bio/summary/aboutme section."
                 "i am going to provide you a sample of example bios so that you can base your"
                 " answer upon that. after providing you the examples i want you to implement"
                 " a new bio based on the following user inputs: professional title,a fact about"
                 "the user (i want you to use this fact about the user to personalize the bio,"
                 "again, using the example ones as context.)"
                 " what is their passion/motivation/drive and what value can they provide to the world."
                 "context = {bio_samples}, professional title : {professional_title}, fact about the user:"
                 "{personalized_fact}, passion/motivation/drive : {passion_motivation}, value_creation:"
                 "{value_creation}"

    )
    formatted_prompt = prompt.format(
        bio_samples=bio_samples,
        professional_title=professional_title,
        personalized_fact=personalized_fact,
        value_creation=value_creation,
        passion_motivation=passion_motivation,
    )
    return llm(formatted_prompt)
