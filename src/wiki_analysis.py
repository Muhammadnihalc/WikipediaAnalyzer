import wikipediaapi
import sqlite3
from collections import Counter
from datetime import datetime
import logging


def fetch_wikipedia_text(topic):
    try:
        logging.info(f"Fetching Wikipedia text for topic: {topic}")
        wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
        page = wiki_wiki.page(topic)
        if page.exists():
            logging.info(f"Page for topic '{topic}' exists. Retrieving text.")
            return page.text
        else:
            logging.warning(f"Page for topic '{topic}' does not exist.")
            return None
    except Exception as e:
        logging.error(f"An error occurred while fetching Wikipedia text: {str(e)}")
        return None



def analyze_text(text, n):
    try:
        words = text.split()
        word_freq = Counter(words)
        top_n_words = word_freq.most_common(n)
        return top_n_words
    except Exception as e:
        return []



def add_data(topic, word, count):
    try:
        logging.info(f"Adding search history data to the database: topic='{topic}', word='{word}', count={count}")

        conn = sqlite3.connect('search_history.db')
        c = conn.cursor()

        # Insert search history data into database
        c.execute("INSERT INTO search_history (topic, word, count, time) VALUES (?, ?, ?, ?)", 
                  (topic, word, count, datetime.now()))
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        logging.info("Search history data added successfully.")
    except Exception as e:
        logging.error(f"An error occurred while adding data to the database: {str(e)}")




def get_search_history():
    try:
        conn = sqlite3.connect('search_history.db')
        c = conn.cursor()
        c.execute("SELECT topic, word, count, time FROM search_history ORDER BY time DESC")
        search_history = c.fetchall()
        conn.close()
        return search_history
    except Exception as e:
        logging.error(f"Error retrieving search history from the database: {str(e)}")
        return []


def format_search_history(search_history):
    formatted_history = []
    for entry in search_history:
        topic, word, count, time = entry
        formatted_entry = {
            "Article": topic.strip(),  # Remove leading/trailing whitespace
            "most_frequent_word": {word: count},  # Include most frequent word and its count
            "search_time": str(time)  # Converting time to string for better readability
        }
        formatted_history.append(formatted_entry)
    return formatted_history



def clear_history():
    try:
        conn = sqlite3.connect('search_history.db')
        c = conn.cursor()
        c.execute("DELETE FROM search_history")
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f"Error clearing search history from the database: {str(e)}")