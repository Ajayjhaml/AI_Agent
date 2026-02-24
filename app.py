import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

from agent.llm import get_llm
from agent.tools import analyze_symbol
from agent.prompts import SYSTEM_PROMPT

def main():
    llm = get_llm()
    llm_with_tools = llm.bind_tools([analyze_symbol])

    # Ask user for stock symbol dynamically
    stock_symbol = input("Enter the stock symbol (e.g., AAPL, TSLA, BTC-USD): ").upper()

    # Construct query dynamically using the user input
    user_query = f"Analyze {stock_symbol} with latest news or impactful news and output the news"

    response = llm_with_tools.invoke(
        [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ]
    )

    # Check if LLM decided to call the tool
    if response.tool_calls:
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            if tool_name == "analyze_symbol":
                # Pass the stock symbol dynamically
                result = analyze_symbol.invoke(tool_args or stock_symbol)
                print("\n===== TOOL OUTPUT =====\n")
                print(result)
                return

    print("\n===== MODEL OUTPUT =====\n")
    print(response.content)


if __name__ == "__main__":
    main()