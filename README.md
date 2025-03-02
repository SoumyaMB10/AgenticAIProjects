🎬 YouTube Blog Generator
📌 Overview
This project is an AI-powered YouTube Blog Generator that extracts a video's transcript and generates a well-structured blog post using LangChain, LangGraph, and OpenAI/Groq models.

✅ Features:

Extracts transcripts from YouTube videos
Uses LLM (Groq's Qwen-2.5-32b) to generate a blog
StateGraph (LangGraph) manages processing flow

📌 Tech Stack
Python 3.10+
LangGraph → AI workflow orchestration
LangChain → Handles LLM-based blog generation
YoutubeLoader → Extracts transcripts from YouTube
Groq API (Qwen-2.5-32b) → AI model for blog generation
Dotenv → Manage API keys

📌 How It Works
1️⃣ User enters a YouTube URL in the Streamlit app
2️⃣ YouTube transcript is extracted via YoutubeLoader
3️⃣ LangGraph processes the transcript:

Step 1: yt_transcript(state) → Extracts transcript
Step 2: blog_generate(state) → AI generates a blog
4️⃣ The AI-generated blog is displayed in Markdown format
