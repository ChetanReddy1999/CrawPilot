from bs4 import BeautifulSoup
import tensorflow_hub as hub
import numpy as np
import pymongo,requests
from transformers import BartForConditionalGeneration, BartTokenizer
from sklearn.metrics.pairwise import cosine_similarity

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

# Connect to Mongo
client = pymongo.MongoClient("mongodb://localhost:27018/")
database = client["crawler"]
collection = database["url_collection"]

ans = {}

# This function is used to scrap the page
def get_data(urls,rand_id):

    ans[rand_id] = []
    for url in urls:

        #Add url into db
        db_element = collection.find_one({'url':url})
        if db_element is None:
            collection.insert_one({'url':url})

        response = requests.get(url=url)
        content = response.content
        
        if response.status_code == 200:
            content = BeautifulSoup(content, 'html.parser')
            
            # Find h1 tag from the page.
            head = content.find('h1')

            if head:
                header = head.text
            
            links = content.find_all('a')

            link_list = []
            for link in links:
                if link.get('href') and 'http' in link.get('href'):
                    link_list.append(link.get('href').strip(' \t\n'))

            text = get_summary(content)
            
            ans[rand_id].append({'url':url,'header':header,'link_list':link_list,'summary':text})
        else:
            print("Failed to retrieve page:", response.status_code)

    print("Scrapping is completed!!")
    

def get_summary(content):
    paragraphs = content.find_all('p')

    large_text = ''

    for para in paragraphs:
        large_text = large_text +'\n' + para.text

    if large_text == "":
        return large_text

    # Tokenize the text
    inputs = tokenizer([large_text], max_length=1024, return_tensors="pt", truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs.input_ids, max_length=int(len(large_text) * 0.3), min_length=1, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary


def return_urls():
    urls = collection.find({})
    ans = []
    for url in urls:
        ans.append(url['url'])

    return ans

def vector_embeddings(id):
    text_contents = []
    text_list = ans[id]
    for text in text_list:
        text_contents.append(text['summary'])

    use_model = hub.KerasLayer("https://tfhub.dev/google/universal-sentence-encoder-large/5")
    embeddings = use_model(text_contents)
    embeddings = np.array(embeddings)
    cosine_sim_matrix = cosine_similarity(embeddings)
    
    print("Cosine Similarity Matrix:")
    print(cosine_sim_matrix)

    return cosine_sim_matrix

