import streamlit as st
import os

from src.LangGraph_agenticAi.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False


        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # API key is read from environment variables only
                env_api_key = os.environ.get("GROQ_API_KEY", "")
                self.user_controls["GROQ_API_KEY"] = env_api_key  # Store for use in other components
                if not env_api_key:
                    st.warning("⚠️ GROQ_API_KEY environment variable is not set. Please configure it in your deployment settings.")
            
            ## USecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases",usecase_options)

            if self.user_controls["selected_usecase"] =="Chatbot With Web" or self.user_controls["selected_usecase"] =="AI News" :
                # API key is read from environment variables only
                env_tavily_key = os.environ.get("TAVILY_API_KEY", "")
                self.user_controls["TAVILY_API_KEY"] = env_tavily_key  # Store for use in other components
                if not env_tavily_key:
                    st.warning("⚠️ TAVILY_API_KEY environment variable is not set. This feature requires Tavily API key configured in deployment settings.")

            if self.user_controls['selected_usecase']=="AI News":
                st.subheader("📰 AI News Explorer ")
                
                with st.sidebar:
                    time_frame = st.selectbox(
                        "📅 Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0
                    )
                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame


        return self.user_controls