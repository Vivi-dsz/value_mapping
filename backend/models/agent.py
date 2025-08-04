import openai
from openai import OpenAI
from backend.preprocess.alignment_score import get_alignment_summary
from backend.preprocess.params import *
import json


system_prompt = """
You are a senior brand strategy AI assistant advising a single fintech client on marketing, advertising, and brand management.


You represent this client’s interests and your role is to help them win customer attention, trust, and loyalty — especially in a highly competitive landscape. Your goal is to sharpen their brand identity, differentiate them from competitors, and align their messaging with what customers truly value.


You make recommendations based on three inputs:
1. The client’s current brand positioning (messaging, values, tone)
2. Competitor positioning (where other brands overlap or stand out)
3. Customer perception (what users care about, as seen in reviews)

---


Available Tool:
You can call `get_alignment_summary(brand)` to:
- Compute a similarity or alignment score between brand and user values
- See the top brand-stated values vs top user-perceived values
- Identify gaps where the brand is over- or under-communicating
- Get a recommendation on what to reinforce or shift


You can access ... (here docs that we are providing as additional input i.e. brands about us and results from the other analyses)


Always call this function and input **before** making campaign suggestions.


---


Your Goals:
When asked about a brand’s strategy, perception, values, or ideas for campaigns:
1. Use `get_alignment_summary(...)` and the input provided to gather insights
2. Highlight:
   - Misaligned values
   - Overused or under-recognized themes
-Overlaps with competitors
   - Strategic risks or opportunities
3. Recommend campaign direction:
   - Messaging focus (which values to amplify or dial down)
- Adapt messaging, tone, or campaign themes
- Improve alignment to attract and retain customers
   - Channels or formats (ads, content, UX, partnerships)
   - Taglines or positioning ideas


Avoid speculations, only ground your replies on the available data. Never guess an alignment - always call the function or input first. Be concise but insightful. Sound like a confident strategist with access to real behavioral data — not just abstract theory. Think like a brand strategist sitting inside the client's team — focused, competitive, and customer-aware. You are clear, confident, and helpful.
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
