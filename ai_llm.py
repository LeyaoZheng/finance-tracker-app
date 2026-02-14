import os
from openai import OpenAI

def get_llm_budget_advice(*, lang: str, summary: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        return "AI not configured." if lang == "en" else "AI 未配置。"

    client = OpenAI(api_key=api_key)

    if lang == "zh":
        instructions = (
            "你是一名专业的个人理财顾问。"
            "请基于提供的数据，用简洁的方式给出："
            "1. 趋势判断 2. 风险评估 3. 一条核心建议。"
            "控制在150字以内。"
        )
    else:
        instructions = (
            "You are a financial advisor. "
            "Based on the data, give: "
            "1. Trend assessment "
            "2. Risk level "
            "3. One key recommendation. "
            "Limit to 120 words."
        )

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions=instructions,
            input=summary,
            max_output_tokens=200
        )

        return response.output_text.strip()

    except Exception:
        return (
            "AI temporarily unavailable."
            if lang == "en"
            else "AI 暂时不可用。"
        )
