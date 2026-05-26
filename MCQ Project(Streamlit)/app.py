import streamlit as st
import requests
from bs4 import BeautifulSoup

# 1. Bring in the Google AI tool and give it a short nickname: "genai"
import google.generativeai as genai

# 2. Give the AI our secret password so it lets us in
# MAKE SURE YOUR KEY IS INSIDE THE QUOTATION MARKS! Like this: api_key="AIzaSy..."
genai.configure(api_key="AIzaSyDM69FQuAZ7AbjrAaUztB2_QQnx1OEx2wQ")

# ... keep your scrape_website_text function exactly as it is below this ...

def  scrape_website_text(url):
    try:
        # 1. Create an "ID Badge" to pretend we are a normal Windows computer using Chrome
        my_id_badge = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        
        # 2. Knock on the website's door and show the badge
        response = requests.get(url, headers=my_id_badge, timeout=10)
        
        # 3. Read the text
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        full_text = " ".join([p.get_text() for p in paragraphs]).strip() # .strip() removes empty spaces
        
        # 4. If the page is still blank, tell us!
        if len(full_text) == 0:
            return "Error: The website gave us a blank page!"
            
        return full_text
        
    except Exception as e:
        return f"Error reading website: {e}"

# 1. This sets up the name on our web browser tab
st.set_page_config(page_title="AI Quiz Generator", page_icon="📚")

# 2. This creates a big, beautiful title on our screen
st.title("📚 Automated Study Buddy Quiz Generator")
st.write("Welcome to your MCA project! Enter a website link below to generate a quiz.")

# 3. This creates a text box where users can paste a link
website_url = st.text_input("Paste the educational website URL / link here:")

def create_quiz_with_ai(text):
    try:
        # 1. Choose which AI brain we want to use (Gemini 1.5 Flash is very fast and smart!)
        model = genai.GenerativeModel('gemini-3.5-flash')
        
        # 2. Write our exact instructions for the AI (This is called the Prompt)
        my_instructions = f"""
        You are a helpful teacher. I will give you some text to read. 
        Please create exactly 10 multiple-choice questions based on the text.
        
        FORMAT INSTRUCTIONS:
        You must format your response exactly like this example, using Markdown:
        
        ### Question 1: [Your Question Here]
        * **A)** [Option A]
        * **B)** [Option B]
        * **C)** [Option C]
        * **D)** [Option D]
        
        > **Correct Answer:** [The Answer]
        
        ---
        (Do this for all 10 questions)
        
        Here is the text to read:
        {text}
        """
        
        # 3. Send the instructions to the AI and wait for it to write the quiz
        response = model.generate_content(my_instructions)
        
        # 4. Hand the finished quiz back to our app
        return response.text
        
    except Exception as e:
        return f"Error talking to AI: {e}"


# 4. This creates a clickable button


# --- BUTTON LOGIC ---
if st.button("Generate Quiz"):
    if website_url:
        # Step 1: Tell the user we are working
        st.info("Step 1: Reading the website... Please wait.")
        
        # Step 2: Use our Scraper to get the text
        scraped_text = scrape_website_text(website_url)
        
        if "Error" in scraped_text:
            st.error(scraped_text)
        else:
            st.success("Website read successfully!")
            
            # Step 3: Tell the user the AI is thinking
            st.info("Step 2: AI is creating your quiz... Brain power activating!")
            
            # Step 4: Hand the text to the AI and wait for the quiz
            final_quiz = create_quiz_with_ai(scraped_text)
            
            if "Error" in final_quiz:
                st.error(final_quiz)
            else:
                # Step 5: SUCCESS! Print the final quiz on the screen!
                st.success("Quiz created!")
                st.write("---") # This draws a clean horizontal line on the screen
                st.write(final_quiz)
                
    else:
        st.error("Please paste a link first!")