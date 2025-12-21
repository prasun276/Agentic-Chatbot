# 🤖 LangGraph Agentic AI Chatbot

An end-to-end project showcasing Agentic AI Chatbots built with LangGraph, featuring multiple use cases including basic chatbots, web-enabled chatbots, and AI news aggregation.

## 🌟 Features

This application provides three main use cases:

1. **Basic Chatbot** - A simple conversational AI chatbot powered by Groq's LLM models
2. **Chatbot With Web** - An advanced chatbot with web search capabilities using Tavily API
3. **AI News** - Automated AI news aggregation and summarization with daily, weekly, and monthly options

## 🚀 Quick Start

### Running Locally

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "Agentic Chatbot"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API Keys (Required - via environment variables)**
   ```bash
   # For Groq (required)
   export GROQ_API_KEY="your-groq-api-key"
   
   # For Tavily (required for "Chatbot With Web" and "AI News" use cases)
   export TAVILY_API_KEY="your-tavily-api-key"
   ```
   
   **Note**: API keys must be set as environment variables. The application does not provide UI input for security reasons, especially for public deployments.

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🔑 API Keys

### Getting API Keys

- **Groq API Key**: Get your free API key from [Groq Console](https://console.groq.com/keys)
- **Tavily API Key**: Get your API key from [Tavily](https://app.tavily.com/home)

### Using API Keys

API keys are **only** configured via environment variables for security and ease of deployment:

- Set `GROQ_API_KEY` in your environment (required for all use cases)
- Set `TAVILY_API_KEY` in your environment (required for "Chatbot With Web" and "AI News" use cases)

This approach ensures:
- ✅ Secure key management (keys are not exposed in the UI)
- ✅ Easy deployment to cloud platforms like Hugging Face Spaces
- ✅ No need for users to enter keys when using the deployed application

## 🎯 Usage

1. **Select LLM**: Choose from available Groq models:
   - `llama-3.1-8b-instant` - Fast and efficient
   - `llama-3.3-70b-versatile` - More capable model
   - `openai/gpt-oss-120b` - Largest model option

2. **Select Use Case**:
   - **Basic Chatbot**: Simple conversations without external tools
   - **Chatbot With Web**: Enhanced with web search capabilities
   - **AI News**: Fetch and summarize AI news by timeframe

3. **Enter your message** or use the "Fetch Latest AI News" button for the AI News use case

## 📦 Deployment to Hugging Face Spaces

This application is ready for deployment to Hugging Face Spaces. Here's how:

### Step 1: Create a Hugging Face Space

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Fill in the details:
   - **Owner**: Your Hugging Face username
   - **Space Name**: Choose a unique name (e.g., `langgraph-agentic-chatbot`)
   - **SDK**: Select **Streamlit**
   - **Hardware**: Select appropriate tier (CPU Basic is sufficient for most use cases)

### Step 2: Set Up Secrets (Required)

1. Go to your Space settings
2. Navigate to "Variables and secrets"
3. Add the following secrets (these are required for the application to work):
   - `GROQ_API_KEY`: Your Groq API key (required for all features)
   - `TAVILY_API_KEY`: Your Tavily API key (required for "Chatbot With Web" and "AI News" use cases)

**Important**: Without these environment variables set as secrets, the application will not function properly. Users of your deployed Space will not need to enter any API keys - they're all pre-configured.

### Step 3: Upload Files

Upload all project files to your Space. The key files needed are:
- `app.py` - Main application entry point
- `requirements.txt` - Python dependencies
- `src/` - Source code directory
- `.gitignore` - Git ignore file
- `README.md` - This file

### Step 4: Wait for Build

Hugging Face Spaces will automatically:
- Install dependencies from `requirements.txt`
- Build and deploy your Streamlit application
- Make it accessible via a public URL

### Important Notes for Hugging Face Spaces

- ✅ **API keys must be set as secrets** in Space settings - the UI does not accept key input
- ✅ The application automatically uses environment variables from Space secrets
- ✅ Users don't need to enter any API keys - they're all pre-configured
- ⚠️ File writes (like AI News summaries) will be ephemeral on Spaces (files don't persist)
- ⚠️ Ensure `AINews/` directory exists or modify the code to handle file paths dynamically

## 🛠️ Project Structure

```
.
├── app.py                          # Main Streamlit entry point
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── src/
│   └── LangGraph_agenticAi/
│       ├── main.py                 # Main application logic
│       ├── graph/                  # LangGraph graph definitions
│       ├── LLMS/                   # LLM configurations
│       ├── nodes/                  # Graph node implementations
│       ├── state/                  # State management
│       ├── tools/                  # Tool definitions (Tavily search)
│       └── ui/                     # Streamlit UI components
└── AINews/                         # Generated news summaries (local only)
```

## 📋 Requirements

See `requirements.txt` for the complete list. Main dependencies include:
- `streamlit` - Web UI framework
- `langchain` & `langgraph` - LangChain and LangGraph frameworks
- `langchain_groq` - Groq LLM integration
- `tavily-python` & `langchain-tavily` - Tavily search integration
- `faiss-cpu` - Vector database (if needed)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

[Specify your license here]

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Powered by [Groq](https://groq.com/) for LLM inference
- Web search powered by [Tavily](https://tavily.com/)

---

**Note**: This is an educational project showcasing agentic AI capabilities with LangGraph. For production use, ensure proper error handling, rate limiting, and security measures are in place.
