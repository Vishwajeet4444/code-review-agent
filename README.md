# 🤖 CodeReview Agent

A multi-agent AI pipeline that reviews your code using **3 specialized agents** powered by **Gemini 2.5 Flash**.

Built as a capstone project for the [Google x Kaggle 5-Day AI Agents Intensive (2026)](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project). 

---

## 🧠 Agent Pipeline

```
Your Code → [Agent 1: Analyzer] → [Agent 2: Suggester] → [Agent 3: Refactorer] → Reviewed Code
```

| Agent | Role |
|---|---|
| 🔍 **Analyzer** | Finds bugs, security issues, performance problems |
| 💡 **Suggester** | Proposes specific fixes for each issue found |
| ⚡ **Refactorer** | Rewrites the code applying all fixes |

Each agent's output feeds into the next — making this a true sequential multi-agent pipeline, not just a single LLM prompt.

---

## 🚀 Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/Vishwajeet4444/code-review-agent
cd code-review-agent
```

**2. Install dependency**
```bash
pip install google-generativeai
```

**3. Set your Gemini API key**
```bash
export GEMINI_API_KEY="your_api_key_here"
```
Get a free key at [aistudio.google.com](https://aistudio.google.com)

**4. Run on any code file**
```bash
python agent.py yourfile.py
```

---

## 📸 Example Output

```
📂 Reviewing: sample.py
📏 Lines: 32

==================================================
🤖 AGENT 1: Analyzer
==================================================
1. Line 12: SQL query is vulnerable to injection attack
2. Line 7: Variable `x` has unclear naming
3. Line 20: Inefficient loop — O(n²) complexity

==================================================
🤖 AGENT 2: Suggester
==================================================
1. Use parameterized queries instead of string formatting
2. Rename `x` to `user_count` for clarity
3. Replace nested loop with dictionary lookup — O(n)

==================================================
🤖 AGENT 3: Refactored Code
==================================================
# Fixed and optimized version
...

✅ Review complete!
```

---

## 🛠 Tech Stack

- **Python 3.8+**
- **Gemini 1.5 Flash** via `google-generativeai`
- **Supports:** `.py`, `.js`, `.ts`, `.java`, `.go`, `.cpp`, `.rb` and any text-based file

---

## 📁 Project Structure

```
code-review-agent/
├── agent.py        # Main multi-agent pipeline
└── README.md
```

---

## 🔮 Future Scope

- Web UI (Next.js) with real-time streaming output
- GitHub PR integration — auto-review on pull request
- Support for multi-file projects
- Custom rules per language
