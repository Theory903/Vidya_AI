# IMPORTS
import os
import spacy
import openai
from dotenv import load_dotenv
from Model.AI.Role import kwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

#TO INITIATE (.env) FILE
load_dotenv ()
# IT CALLS THE ROLE MODELES AND ITS COMPONENTS
rwords=kwords()

# IT CALLS THE API KEY 
apikey = os.getenv('API_KEY')
openai.api_key = apikey

# Load a spaCy model for text processing
nlp = spacy.load("en_core_web_sm")

# Define a dictionary of roles and their associated keywords
def categorize_role(prompt):
    # Tokenize the user's input prompt
    input_tokens = [token.text for token in nlp(prompt.lower())]

    # Create TF-IDF vectorizers for input tokens and role keywords
    tfidf_vectorizer = TfidfVectorizer()
    input_vector = tfidf_vectorizer.fit_transform([" ".join(input_tokens)])
    role_similarities = {}
    for role, keywords in rwords.items():
        # Convert role keywords into a single string for TF-IDF vectorization
        keyword_text = " ".join(keywords)
        keyword_vector = tfidf_vectorizer.transform([keyword_text])
        # Calculate cosine similarity between input and role keywords
        similarity_matrix = cosine_similarity(input_vector, keyword_vector)
        role_similarities[role] = similarity_matrix[0][0]

    # Categorize the role based on the highest similarity
    categorized_role = max(role_similarities, key=role_similarities.get)
    return categorized_role

#CHAT BOT FUNCTION TO CALL API AND GET RESPONSE
def Chat(role, temperature, top_p, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a {role} assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        top_p=top_p,
        max_tokens=500,
        frequency_penalty=0.3,
        presence_penalty=0.3)
    return response["choices"][0]["message"]["content"].strip()

#THE MAIN AI FUNCTION FOR PROMPT INPUT AND ROLE ASSIGNMENT
def AI(prompt):
    role=categorize_role(prompt)
    #CONDITIONAL STATEMENT TO FIND OUT THE ROLE
    if   role=="General": aspect = ["General ChatBot", 0, 0]
    elif role=="Mathematics":aspect = ["Mathematics", 0, 0.8]
    elif role=="Data Analysis":aspect= ["Data Analysis", 0.2, 0.1] 
    elif role=="Code Explainer":aspect = ["Code Explainer", 0.6, 0.7]
    elif role=="Code Generating":aspect = ["Code Generating", 0.2, 0.1]
    elif role=="Comment Generating":aspect = ["Comment Generating", 0.3, 0.2]
    elif role=="Professional ChatBot":aspect = ["Professional ChatBot", 0.5, 0.5]
    elif role=="Creative Story Writing":aspect = ["Creative Story Writing", 0.7, 0.8]
    role, temperature, top_p = aspect
    response= Chat(role, temperature, top_p, prompt=prompt)
    return response