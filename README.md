
# Wikipedia Analyzer

The goal of this project is to develop a Python-based API that interacts with Wikipedia to perform specific text analysis tasks.


## Run Locally

Clone the project

```bash
  git clone https://github.com/Muhammadnihalc/WikipediaAnalyzer

```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the Application

```bash
  python app.py

```


## API Reference

#### Get all items

```http
    POST /analyze
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `topic` | `string` | **Required**. Your API key |
 ' n '    | 'integer' | **Required**. Your API key

 sample request 

 {
    "topic": "Python",
    "n": 3
}

 sample response 

 {
    "top_words": [

        [
            "Python",
            20
        ],
        [
            "a",
            19
        ],
        [
            "of",
            10
        ]
    ],
    "topic": "Python "
}


#### Get item

```http
    POST /list
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `query`      | `string` | **Required**. Id of item to fetch |


sample request

{

    "query": "Python "

}

sample response

{

    "articles": [
        "Python",
        "Python (programming language)",
        "Monty Python",
        "Ball python",
        "Python (codename)"
    ]
}

#### Get item

```http
    GET /history
```

sample response

{
    
    "search_history": [
        {
            "Article": "Python",
            "most_frequent_word": {
                "Python": 20
            },
            "search_time": "2024-02-07 18:27:04.218638"
        },
        {
            "Article": "Python",
            "most_frequent_word": {
                "Python": 20
            },
            "search_time": "2024-02-07 18:26:39.875783"
        }
    ]
}



## Features

- /analyze  
  This API will fetch the text of the Wikipedia article corresponding to the provided topic, analyze the text to determine the frequency of each word, and then return the top n most frequent words in a structured format.
- /history 
   This endpoint will list the past search results, including the topics searched and the corresponding top frequent words returned by the API.
- /list 
  
  This api Retrieves a list of Wikipedia articles related to a specific query , this api is helpful to find topic
- /ClearSearchHistory
 
  Clears all data stored in the search history database, allowing users to remove thier search history as needed. 

- Logging

  Logs important events, such as requests received, errors encountered, and database interactions, to the app.log file for monitoring and debugging purposes.
