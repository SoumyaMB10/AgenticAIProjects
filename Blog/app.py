import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import os 

from langchain_groq import ChatGroq
from langgraph.graph import START,END, StateGraph
from typing_extensions import TypedDict

from IPython.display import display, Image
from langchain_community.document_loaders import YoutubeLoader

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="qwen-2.5-32b")

# Title of the Streamlit App
st.title("🎬 YouTube Blog Generation")

# User Input for YouTube URL
url = st.text_input("📌 Enter YouTube URL:")

# Submit Button
if st.button("Generate Blog"):
    if url:
        class State(TypedDict):
            input_url:str
            transcript:str
            blog:str


        #nodes 

        def yt_transcript(state:State):
            ## url human in loop 
            """get the transcript of the url provided by the user
            """
            #url = state["input_url"]
            loader = YoutubeLoader.from_youtube_url(f"{state["input_url"]}",add_video_info = False).load()
            transcript = [doc.page_content for doc in loader]
            #state['transcript'] = transcript
            return {"transcript":transcript}
        

        def blog_generate(state:State):
            """generate the blog based on transcript given
            """
            blog = llm.invoke("Generate the blog for the youtube video transcript" + f"{state['transcript']}")
            #state['blog'] = blog
            return {"blog":blog}
        
        ## build graph 

        builder = StateGraph(State)

        ## graph nodes 
        builder.add_node("yt_transcript", yt_transcript)
        builder.add_node("blog_generate", blog_generate)

        #graph edges 
        builder.add_edge(START,"yt_transcript")
        builder.add_edge("yt_transcript","blog_generate")
        builder.add_edge("blog_generate",END)

        #compiling 
        graph = builder.compile()

        res = graph.invoke({"input_url":url})

        #display(Image(graph.get_graph().draw_mermaid_png()))
            
        blog_content = res['blog'].content

        # # Placeholder logic for blog generation
        # blog_content = f"""
        # # ✍️ Generated Blog for {url}

        # ## 🌟 Introduction
        # This blog is based on the YouTube video at {url}.  
        # We summarize key points, insights, and takeaways from the video.

        # ## 📌 Key Points
        # - **Main Topic:** Example topic from the video  
        # - **Important Takeaway #1**  
        # - **Important Takeaway #2**  

        # ## 🎯 Conclusion
        # This blog summarizes the key learnings from the video. Stay tuned for more updates!

        # _Generated using AI-powered YouTube content analysis._
        # """
        
        # Display blog output
        st.markdown(blog_content)
    else:
        st.warning("⚠️ Please enter a valid YouTube URL!")

