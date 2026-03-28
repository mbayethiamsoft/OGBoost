# 🚀 OGBoost

OGBoost is an AI-powered tool that generates **high-performing social media posts** and **Open Graph images** from a simple idea or link.

Built with **LangGraph + AI agents**, OGBoost helps non-technical users create viral-ready content in seconds.

---

## ✨ Features

* 🧠 AI-generated posts (LinkedIn, threads, etc.)
* 🔥 Multiple viral hooks
* 🎨 Open Graph image prompt generation
* ⚡ Fast and simple UX (1 input → 1 click → results)
* 🔗 Built with agent workflows using LangGraph

---

## 🏗️ Tech Stack

### Backend

* Python
* FastAPI
* LangGraph
* LangChain
* OpenAI API
* uv (package manager)

### Frontend

* Next.js
* Axios

### OG Image Generation

* Vercel OG (optional)

---

## 📦 Project Structure

```
og-boost/
├── backend/
│   ├── main.py
│   ├── graph.py
│   ├── pyproject.toml
│   └── .env
│
├── frontend/
│   ├── pages/
│   ├── package.json
│   └── ...
```

---

## ⚙️ Installation

### 1. Clone the repo

```
git clone https://github.com/your-username/ogboost.git
cd ogboost
```

---

## 🐍 Backend setup (with uv)

### 1. Install uv (if not installed)

```
curl -Ls https://astral.sh/uv/install.sh | sh
```

or

```
pip install uv
```

---

### 2. Create environment & install dependencies

```
cd backend
uv venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows

uv pip install fastapi uvicorn langchain langgraph openai python-dotenv
```

---

### 3. Environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 4. Run the backend

```
uvicorn main:app --reload
```

Backend runs on:
👉 http://localhost:8000

---

## 🌐 Frontend setup

```
cd frontend
npm install
npm run dev
```

Frontend runs on:
👉 http://localhost:3000

---

## 🚀 Usage

1. Open the app in your browser
2. Enter a topic, idea, or link
3. Click **Generate 🚀**
4. Get:

   * A ready-to-post social media post
   * Hooks
   * An OG image prompt

---

## 🧠 How it works

OGBoost uses a **multi-step AI pipeline** powered by LangGraph:

1. **Summarization Agent** → extracts key ideas
2. **Hook Generator** → creates viral hooks
3. **Post Generator** → builds the final content
4. **OG Prompt Generator** → designs the visual concept

---

## ⚠️ Common Issues

### CORS Error (405 / OPTIONS)

Enable CORS in FastAPI:

```python
from fastapi.middleware.cors import CORSMiddleware
```

---

### OpenAI Quota Error (429)

Make sure:

* Billing is enabled
* Your API key is valid

---

## 💡 Roadmap

* [ ] Multiple post styles (fun, professional, storytelling)
* [ ] OG image rendering (not just prompt)
* [ ] Copy-to-clipboard buttons
* [ ] User accounts
* [ ] Viral score system

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📄 License

MIT License

---

## 🌟 Vision

OGBoost aims to make **content creation effortless** for everyone —
not just developers.

---

Made with ❤️ using AI
