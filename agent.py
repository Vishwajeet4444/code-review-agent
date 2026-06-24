from google import genai
from dotenv import load_dotenv
import sys
import os
import time

# --- CONFIG ---
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

def run_agent(prompt, label):
    print(f"\n{'='*50}")
    print(f"🤖 {label}")
    print('='*50)
    for attempt in range(3):
        try:
            response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            result = response.text
            print(result)
            return result
        except Exception as e:
            if attempt < 2:
                print(f"⚠️ Attempt {attempt+1} failed, retrying in 5s... ({e})")
                time.sleep(5)
            else:
                print(f"❌ All attempts failed: {e}")
                return ""

def review_code(code, filename="code"):
    print(f"\n📂 Reviewing: {filename}")
    print(f"📏 Lines: {len(code.splitlines())}")

    # --- AGENT 1: Analyzer ---
    analysis = run_agent(f"""
You are a code analyzer agent. Analyze the following code and identify:
1. Bugs or logical errors
2. Security vulnerabilities
3. Performance issues
4. Code quality issues (naming, readability, structure)

Be specific. Mention line numbers where possible.

Code:
```
{code}
```

Output only the analysis. No fixes yet.
""", "AGENT 1: Analyzer")

    # --- AGENT 2: Suggester ---
    suggestions = run_agent(f"""
You are a code improvement suggester agent. Based on this analysis of the code, provide specific fix suggestions for each issue found.

Original Code:
```
{code}
```

Analysis:
{analysis}

For each issue, give a clear, actionable fix. Be concise.
""", "AGENT 2: Suggester")

    # --- AGENT 3: Refactor ---
    run_agent(f"""
You are a code refactoring agent. Rewrite the original code applying all the suggested fixes.

Original Code:
```
{code}
```

Fixes to apply:
{suggestions}

Output ONLY the refactored code with brief inline comments explaining key changes. No extra explanation outside the code.
""", "AGENT 3: Refactored Code")

    print("\n✅ Review complete!")

def main():
    if len(sys.argv) < 2:
        print("Usage: python agent.py <filename>")
        print("Example: python agent.py my_script.py")
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    if not code.strip():
        print("❌ File is empty.")
        sys.exit(1)

    review_code(code, filename=filepath)

if __name__ == "__main__":
    main()