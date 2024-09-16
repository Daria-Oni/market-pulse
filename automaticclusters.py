import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import openai

openai.api_key = 'secret'


def load_data(csv_file):
    """ Loading data from a CSV file. """
    return pd.read_csv(csv_file)

def find_optimal_clusters(X, max_k=10):
    """ Finds the optimal number of clusters based on silhouette coefficient. """
    silhouette_scores = []
    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(X)
        score = silhouette_score(X, labels)
        silhouette_scores.append(score)
    
    # Find the index of the maximum value of the silhouette coefficient
    optimal_k = silhouette_scores.index(max(silhouette_scores)) + 2 
    return optimal_k

def generate_cluster_names(labels, data):
    """ Generating cluster names using OpenAI. """
    cluster_names = {}
    for i in set(labels):
        cluster_keywords = " ".join(data[data['cluster_id'] == i]['keywords'])
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a clustering assistant. Please generate a concise name for a cluster based on these keywords."},
                {"role": "user", "content": f"{cluster_keywords}"}
            ],
            temperature=0.5
        )
        cluster_names[i] = response['choices'][0]['message']['content'].strip()
    return cluster_names

def cluster_data(data):
    """ Data clustering and name generation. """
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data['keywords'])
    optimal_k = find_optimal_clusters(X)
    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    labels = kmeans.fit_predict(X)
    data['cluster_id'] = labels
    cluster_names = generate_cluster_names(labels, data)
    return labels, cluster_names

def main(csv_file, output_csv_file):
    data = load_data(csv_file)
    labels, cluster_names = cluster_data(data)
    data['cluster_title'] = [cluster_names[label] for label in labels]
    data.to_csv(output_csv_file, index=False)
    print("Updated data with cluster IDs and titles saved to", output_csv_file)

if __name__ == "__main__":
    main('test.csv', 'output_with_clusters_auto.csv')
