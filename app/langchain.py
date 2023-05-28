import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)


def generate_lk_bio(
    professional_title,
    years_of_experience,
    professional_values,
    problem_solving,
    emotional_intelligence,
    personal_growth_mindset,
    teamwork_collaboration,
    communication_skills,
    initiative_proactivity,
    adaptability_resilience,
    value_creation,
    passion_motivation,
):
    prompt = PromptTemplate(
        input_variables=[
            "professional_title",
            "years_of_experience",
            "professional_values",
            "problem_solving",
            "emotional_intelligence",
            "personal_growth_mindset",
            "teamwork_collaboration",
            "communication_skills",
            "initiative_proactivity",
            "adaptability_resilience",
            "value_creation",
            "passion_motivation",
        ],
        template="generate a linkedin bio (summary/about me field) based on the following variables:"
        "professional_title: {professional_title},"
        "years_of_experience: {years_of_experience},"
        "professional_values: {professional_values},"
        "problem_solving: {problem_solving},"
        "emotional_intelligence: {emotional_intelligence},"
        "personal_growth_mindset: {personal_growth_mindset},"
        "teamwork_collaboration: {teamwork_collaboration},"
        "communication_skills: {communication_skills},"
        "initiative_proactivity: {initiative_proactivity},"
        "adaptability_resilience: {adaptability_resilience},"
        "value_creation: {value_creation},"
        "passion_motivation: {passion_motivation}",
    )
    formatted_prompt = prompt.format(
        professional_title=professional_title,
        years_of_experience=years_of_experience,
        professional_values=professional_values,
        problem_solving=problem_solving,
        emotional_intelligence=emotional_intelligence,
        personal_growth_mindset=personal_growth_mindset,
        teamwork_collaboration=teamwork_collaboration,
        communication_skills=communication_skills,
        initiative_proactivity=initiative_proactivity,
        adaptability_resilience=adaptability_resilience,
        value_creation=value_creation,
        passion_motivation=passion_motivation,
    )
    return llm(formatted_prompt)
