from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

SYSTEM_PROMPT = """
# 角色與目標
你是一個名為「智能助理」的頂尖 AI 資訊探勘專家。你的核心任務是利用即時的網路搜尋能力，為使用者提供最準確、全面且客觀的答案。你不僅僅是資訊的搬運工，更是一位能夠綜合、分析並清晰呈現資訊的研究員。
"""

# 新增這個函式 — 專門執行搜尋並回傳原始結果
def perform_raw_search(query: str):
    print("Performing raw Google search...")
    results = google_search(query)  # 使用內建工具執行搜尋
    print("Raw search results:\n")
    for i, result in enumerate(results, start=1):
        print(f"[{i}] {result.get('title', 'No Title')}")
        print(f"    URL: {result.get('link', 'No URL')}")
        print(f"    Snippet: {result.get('snippet', 'No Description')}\n")
    return results

# 初始化 AI Agent
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An agent that assists users by answering questions using Google Search.',
    instruction=SYSTEM_PROMPT,
    tools=[google_search],
)

# 使用者輸入問題
user_question = input('Ask me anything: ')

# 先顯示搜尋結果
raw_results = perform_raw_search(user_question)

# 再讓 Agent 整理答案
print(" Generating summarized AI response...")
response = root_agent.run(user_question)
print("AI Response:")
print(response)
