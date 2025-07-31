import openai
from backend.preprocess.params import *

client = openai.OpenAI(api_key=api_key)

def get_topic_from_openai_constrained(review_text, values_keywords):
    """
    This function uses a prompt to get ONE topic from a predefined topics (in params.py).
    This function only get the topic from the keys in the dictionary.
    """
    try:
        # Create a flattened list of allowed keywords
        all_keywords = sorted(set([kw for v in values_keywords.values() for kw in v]))
        keyword_list = ", ".join(all_keywords)
        print(all_keywords)
        print(keyword_list)

        # Format a prompt to limit GPT’s choice
        # prompt = (
        #     f"You are a marketing assistant. Based on the customer review below, "
        #     f"choose ONE keyword that best fits the main topic. Only use keywords from this list:\n\n"
        #     f"{keyword_list}\n\n"
        #     f"Review: \"{review_text}\"\n\n"
        #     f"Respond with only ONE keyword from the list."
        # )

        prompt = (
            f"You are a marketing assistant. Analyze the customer review below.\n\n"
            f"First, choose up to TWO keywords that best describe the main topics of the review."
            f"Only use keywords from this list:\n\n"
            f"{keyword_list}\n\n"
            f'Keyword 1 should be the **most relevant**.\n'
            f'Keyword 2 is **optional**, only include it if a second clear topic is present.\n\n'
            f"Second, classify the **sentiment** of the review based on the customer’s emotion."
            f"Choose one of the following sentiment labels:\n"
            f"very negative, negative, neutral, positive, very positive.\n\n"
            f"Review: \"{review_text}\"\n\n"
            f"Respond in this exact format:\n"
            f"Keyword 1: <first keyword>\n"
            f"Keyword 2: <second keyword or leave blank>\n"
            f"Sentiment: <sentiment label>"
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )


        response_text = response.choices[0].message.content.strip()
        lines = response_text.splitlines()

        # Simple parser
        keyword_1 = lines[0].split(":", 1)[1].strip().lower()
        keyword_2 = lines[1].split(":", 1)[1].strip().lower()
        sentiment = lines[2].split(":", 1)[1].strip().lower()

        return keyword_1, keyword_2, sentiment


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
