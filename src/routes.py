from flask import Blueprint, jsonify, request
from src.wiki_analysis import fetch_wikipedia_text, analyze_text, add_data, get_search_history , format_search_history , clear_history
import wikipedia
import logging

bp = Blueprint("main", __name__)


# welcom page
@bp.route('/')
def index():
    return "Welcome to Wikipedia Text Analysis API!"


#api to fetch all the articles related to specific topic
@bp.route('/list', methods=['POST'])
def article_list():
    try:
        data = request.json
        query = data.get('query')
        if not query:
            return jsonify({"error": "Query parameter is missing"}), 400

        # Search for articles related to the query
        articles = wikipedia.search(query)

        return jsonify({"articles": articles})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#this api analyzes text from Wikipedia related to a given topic and returns the top words with their frequencies
@bp.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        topic = data.get('topic')
        n = int(data.get('n'))

        logging.info(f"Received request to analyze topic: {topic}")

        if (n<=0 or n>10):
            return jsonify({"error": "Please ensure that n value is between 1 - 10"}), 404


        text = fetch_wikipedia_text(topic)
        if text is not None:
            logging.info("Text retrieved successfully from Wikipedia.")
            top_n_words = analyze_text(text, n)
            result = {"topic": topic, "top_words": top_n_words}

            # Extract the word with the maximum count from top_words
            word, count = top_n_words[0]

            # Add data to the database
            add_data(topic, word, count)

            return jsonify(result)
        else:
            logging.warning(f"Topic '{topic}' not found in Wikipedia.")
            return jsonify({"error": "Topic not found"}), 404
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


# api to fetch all the search history with the most freequent word

@bp.route('/history')
def history():
    try:
        logging.info("Retrieving search history from the database.")
        search_history = get_search_history()
        formatted_history = format_search_history(search_history)
        return jsonify({"search_history": formatted_history})
    except Exception as e:
        logging.error(f"An error occurred while retrieving search history: {str(e)}")
        return jsonify({"error": "Failed to retrieve search history"}), 500


# api to clear all the search history
@bp.route('/ClearSearchHistory', methods=['POST'])
def clear_search_history():
    try:
        logging.info("Clearing search history from the database.")
        clear_history()
        return jsonify({"message": "Search history cleared successfully"})
    except Exception as e:
        logging.error(f"An error occurred while clearing search history: {str(e)}")
        return jsonify({"error": "Failed to clear search history"}), 500


    

