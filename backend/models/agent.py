import openai
from openai import OpenAI
from backend.preprocess.alignment_score import get_alignment_summary
from backend.preprocess.params import values_keywords
import json


system_prompt = """
You are a senior brand strategy AI assistant helping professionals in marketing, advertising, and brand management.

You specialize in identifying misalignments between a brand’s messaging (from its official texts) and how users actually perceive that brand (from user reviews).

---

Available Tool:
You can call `get_alignment_summary(brand)` to:
- Compute a similarity or alignment score between brand and user values
- See the top brand-stated values vs top user-perceived values
- Identify gaps where the brand is over- or under-communicating
- Get a recommendation on what to reinforce or shift

Always call this function **before** making campaign suggestions.

---

Your Goals:
When asked about a brand’s strategy, perception, values, or ideas for campaigns:
1. Use `get_alignment_summary(...)` to gather insights
2. Highlight:
   - Misaligned values
   - Overused or under-recognized themes
   - Strategic risks or opportunities
3. Recommend campaign direction:
   - Messaging focus (which values to amplify or dial down)
   - Channels or formats (ads, content, UX, partnerships)
   - Taglines or positioning ideas

You are clear, confident, and helpful — like a brand strategist with insight from user behavior data.
"""


supported_brands = ["Klarna", "N26", "Revolut", "Trade Republic", "Bunq"]

def extract_brand_names(text: str, brand_list=None):
    if brand_list is None:
        brand_list = supported_brands
    text_lower = text.lower()
    extracted_brand = [brand for brand in brand_list if brand.lower() in text_lower]
    return extracted_brand


def handle_query(question: str, brand_kw_df, review_kw_df, api_key):
    client = OpenAI(api_key=api_key)
    brands = extract_brand_names(question)
    print(brands)

    # If no brands found, return a message
    if not brands:
        return f"Sorry, I couldn't find any known brands in your question. Supported brands: {', '.join(supported_brands)}."

    elif len(brands) == 1:
        brand = brands[0]
        summary = get_alignment_summary(brand, brand_kw_df, review_kw_df)
        context = (
            f"You are analyzing the brand alignment for {brand}.\n"
            f"Use the JSON summary below to understand user perception vs brand values and generate strategy insights.\n\n"
            f"{json.dumps(summary, indent=2)}"
        )
        prompt = (
            f"You are a brand strategy consultant.\n\n"
            f"User asked: \"{question}\"\n\n"
            f"Use the summary below to answer with strategic recommendations:\n\n"
            f"{context}"
        )

    elif len(brands) == 2:
        b1, b2 = brands
        summary1 = get_alignment_summary(b1, brand_kw_df, review_kw_df)
        summary2 = get_alignment_summary(b2, brand_kw_df, review_kw_df)
        context = json.dumps({
            f"{b1}": summary1,
            f"{b2}": summary2
            }, indent=2)
        prompt = (
            f"You are a brand strategist comparing two brands.\n\n"
            f"User asked: \"{question}\"\n\n"
            f"Use the summaries below to compare their alignment with user perception."
            f"Highlight key differences and suggest which brand is better positioned:\n\n"
            f"{context}"
        )

    else:
        return "I can only compare up to two brands at a time. Please ask about one or two brands."

    # Send to OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"
