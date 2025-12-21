# 🚀 Deployment Guide - Hugging Face Spaces

This guide will walk you through deploying your LangGraph Agentic AI Chatbot to Hugging Face Spaces.

## Prerequisites

- ✅ A Hugging Face account ([Sign up here](https://huggingface.co/join) if needed)
- ✅ Groq API key ([Get it here](https://console.groq.com/keys))
- ✅ Tavily API key ([Get it here](https://app.tavily.com/home))
- ✅ Your project is working locally (you've tested it)

## Step-by-Step Deployment

### Step 1: Create a Hugging Face Space

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click the **"Create new Space"** button (top right)
3. Fill in the Space creation form:
   - **Owner**: Select your username
   - **Space name**: Choose a unique name (e.g., `langgraph-agentic-chatbot`)
   - **SDK**: Select **Streamlit** ⚠️ (Important: Must be Streamlit, not Gradio)
   - **Hardware**: 
     - **CPU Basic** (free) - Sufficient for most use cases
     - Or upgrade if you expect high traffic
   - **Visibility**: Public (recommended) or Private
4. Click **"Create Space"**

### Step 2: Set Up API Keys as Secrets

⚠️ **CRITICAL**: Do this BEFORE uploading your code to avoid errors.

1. In your new Space, go to **Settings** (gear icon in the sidebar)
2. Scroll down to **"Variables and secrets"** section
3. Click **"New secret"** and add:

   **Secret 1: GROQ_API_KEY**
   - Name: `GROQ_API_KEY`
   - Value: Your Groq API key (paste it here)
   - Click **"Add secret"**

   **Secret 2: TAVILY_API_KEY**
   - Name: `TAVILY_API_KEY`
   - Value: Your Tavily API key (paste it here)
   - Click **"Add secret"**

4. Verify both secrets are listed (they'll show as `GROQ_API_KEY` and `TAVILY_API_KEY` with masked values)

### Step 3: Upload Your Code

You have three options:

#### Option A: Using Git (Recommended for version control)

1. **Initialize Git in your project** (if not already done):
   ```bash
   cd "D:\Agentic_AI_Workspace\LangGraph\Agentic Chatbot"
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Add Hugging Face as remote**:
   ```bash
   git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   # Replace YOUR_USERNAME and YOUR_SPACE_NAME with your actual values
   ```

3. **Push to Hugging Face**:
   ```bash
   git push origin main
   ```

#### Option B: Using Hugging Face Web UI

1. In your Space, click **"Files and versions"** tab
2. Click **"Add file"** → **"Upload files"**
3. Upload these files/folders (drag and drop or click to select):
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `src/` folder (entire directory)
   - `AINews/` folder (can be empty, but include it)

   **Note**: You can select multiple files at once. Make sure to upload the entire `src/` directory structure.

#### Option C: Using Hugging Face CLI

1. Install Hugging Face CLI:
   ```bash
   pip install huggingface_hub
   ```

2. Login:
   ```bash
   huggingface-cli login
   ```

3. Upload files:
   ```bash
   cd "D:\Agentic_AI_Workspace\LangGraph\Agentic Chatbot"
   huggingface-cli upload YOUR_USERNAME/YOUR_SPACE_NAME . --repo-type=space
   ```

### Step 4: Monitor the Build

1. After uploading, go to the **"Logs"** tab in your Space
2. Watch the build process:
   - It will install dependencies from `requirements.txt`
   - Build your Streamlit app
   - Show any errors if something goes wrong

3. **Typical build time**: 2-5 minutes

4. Once you see **"Your app is live!"** or similar message, you're done!

### Step 5: Test Your Deployment

1. Go to the **"App"** tab in your Space
2. Test all three use cases:
   - ✅ Basic Chatbot
   - ✅ Chatbot With Web
   - ✅ AI News (Daily/Weekly/Monthly)

3. Verify:
   - No API key input fields are shown (they're hidden)
   - All features work correctly
   - No errors in the UI

## 📋 Files Checklist

Before deploying, ensure you have these files:

- ✅ `app.py` - Main entry point
- ✅ `requirements.txt` - Dependencies
- ✅ `README.md` - Documentation
- ✅ `.gitignore` - Excludes venv, __pycache__, etc.
- ✅ `src/` - All source code
  - ✅ `src/LangGraph_agenticAi/`
  - ✅ All subdirectories and Python files
- ✅ `AINews/` - Directory (can be empty)

## 🔧 Troubleshooting

### Build Fails

**Issue**: Build error or dependency installation fails
- Check the **Logs** tab for specific error messages
- Verify `requirements.txt` has all dependencies
- Ensure Python version compatibility (Spaces uses Python 3.10 by default)

### API Key Errors

**Issue**: "GROQ_API_KEY environment variable is not set"
- Verify secrets are set in Space Settings → Variables and secrets
- Check secret names are exactly: `GROQ_API_KEY` and `TAVILY_API_KEY`
- Restart the Space after adding secrets

### Module Not Found Errors

**Issue**: Import errors for custom modules
- Ensure `src/` directory structure is preserved
- Check all `__init__.py` files are included
- Verify relative imports are correct

### File Write Errors (AI News)

**Issue**: Cannot write to AINews directory
- The code now auto-creates the directory, but files are ephemeral
- This is expected behavior on Hugging Face Spaces
- Files will be deleted when the Space restarts

## 🎉 Post-Deployment

Once deployed successfully:

1. **Share your Space**: 
   - Copy your Space URL (e.g., `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`)
   - Share it with others!

2. **Update README**:
   - Add your Space URL to the main README
   - Add screenshots if desired

3. **Monitor Usage**:
   - Check the **Metrics** tab to see usage statistics
   - Monitor API key usage in Groq and Tavily dashboards

## 📝 Important Notes

- ⚠️ **API Keys**: Never commit API keys to Git. Always use Space secrets.
- ⚠️ **File Storage**: Files written to disk (like AI News summaries) are ephemeral and won't persist across Space restarts.
- ⚠️ **Rate Limits**: Be aware of API rate limits for Groq and Tavily.
- ⚠️ **Costs**: Monitor your API usage to avoid unexpected costs.

## 🆘 Need Help?

- Check [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- Visit [Hugging Face Forums](https://discuss.huggingface.co/)
- Check your Space's Logs tab for error details

---

**Congratulations!** 🎊 Your LangGraph Agentic AI Chatbot is now live on Hugging Face Spaces!

