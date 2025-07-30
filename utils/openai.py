import openai
from utils.params import *

client = openai.OpenAI(api_key=api_key)

def get_topic_from_openai_constrained(review_text, values_keywords):
    try:
        # Create a flattened list of allowed keywords
        all_keywords = sorted(set([kw for v in values_keywords.values() for kw in v]))
        keyword_list = ", ".join(all_keywords)
        print(all_keywords)
        print(keyword_list)

        # Format a prompt to limit GPT’s choice
        prompt = (
            f"You are a marketing assistant. Based on the customer review below, "
            f"choose ONE keyword that best fits the main topic. Only use keywords from this list:\n\n"
            f"{keyword_list}\n\n"
            f"Review: \"{review_text}\"\n\n"
            f"Respond with only ONE keyword from the list."
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        keyword = response.choices[0].message.content.strip().lower()
        return keyword

    except Exception as e:
        print(f"Error: {e}")
        return None


def reverse_keyword_mapping(values_keywords: dict) -> dict:
    """
    Reverse a dictionary of categories to keywords into keyword to category.

    This is just because a first thought that maybe OpenAI works faster if we give more keywords to pick from.

    Args:
        values_keywords (dict): A dictionary with value categories as keys
        and list of keywords as values.

    Returns:
        dict: A reversed dictionary mapping each keyword to its category.
    """
    keyword_to_category = {}
    for category, keywords in values_keywords.items():
        for keyword in keywords:
            keyword_to_category[keyword.lower()] = category.lower()

    return keyword_to_category
