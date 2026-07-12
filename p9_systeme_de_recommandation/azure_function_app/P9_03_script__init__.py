
import azure.functions as func
import json
import pickle
import numpy as np
import pandas as pd


def main(req: func.HttpRequest, model, artcf, newart, artemb, click) -> func.HttpResponse:
    
    user_id = req.get_json()["userId"]

    global algo
    global list_articles
    global list_new_articles
    global articles_embeddings
    global clicks
    global list_users_clicks


    algo = pickle.loads(model.read())['algo']
    list_articles = pickle.loads(artcf.read()).tolist()
    list_new_articles = pickle.loads(newart.read())
    articles_embeddings = pickle.loads(artemb.read())
    clicks = pickle.loads(click.read())
    list_users_clicks = create_list_users_clicks()


    # recommend = get_recommendations(user_id, algo, list_articles)
    recommend = hybrid_recommend(user_id)

    resp = json.dumps(recommend)

    return func.HttpResponse(resp)

def hybrid_recommend(user_id):
    
    if is_new_user(user_id):
        recommend = get_popular_articles()
    elif is_recent_user(user_id):
        recommend = content_based_recommend(user_id)
    else:
        recommend = user_based_recommend(user_id)
        recommend = check_new_articles(recommend, user_id)

    return recommend


def user_based_recommend(user_id, top_n = 5):
    user_articles_preds=[]
    for article_id in list_articles:
        user_articles_preds.append((algo.predict(user_id,article_id).est, article_id))
    user_articles_preds.sort(reverse=True)
    recommend = [item[1] for item in user_articles_preds[:top_n]]
    return recommend


# recommendations with mean embedding, last article or random article from one user
def content_based_recommend(user_id, top = 5):
    embedding = get_embedding_from_user(user_id)
    scores = cos_sim(embedding, user_id)
    best_scores = find_top_n_indices(scores, top)
    return best_scores



# get all clicked articles for one user 
def get_articles_from_user(user_id):
    return clicks[clicks['user_id']==user_id]['click_article_id'].to_list()


# get mean embedding from all embeddings for one user
def get_embedding_from_user(user_id):
    user_articles = get_articles_from_user(user_id)
    user_embeddings = get_embeddings_from_articles(user_articles)
    user_embedding = user_embeddings.mean(axis=0)
    return user_embedding


def get_embeddings_list_articles():
    return [ele[0] for ele in articles_embeddings]

def get_embeddings_from_articles(list_articles):
    if not isinstance(list_articles, list):
        list_articles = [list_articles]
    embeddings_array = np.array([ele[1] for ele in articles_embeddings if ele[0] in list_articles])
    if len(list_articles) == 1:
        embeddings_array = embeddings_array[0]
    return embeddings_array
    
# compute cosinus similarity between given embedding and others articles embedding
def cos_sim(embedding, user_id):
    user_articles = get_articles_from_user(user_id)
    scores = []
    
    for i in get_embeddings_list_articles():
        if i not in user_articles:
            curr_embedding = get_embeddings_from_articles(i)
            cos_sim = np.dot(embedding, curr_embedding)/(np.linalg.norm(embedding)*np.linalg.norm(curr_embedding))
            scores.append((cos_sim, i))
    return scores



# find top indices in the scores list 
def find_top_n_indices(scores, top=5):
    scores.sort(reverse=True)
    return [item[1] for item in scores[:top]]
    


def check_new_articles(recommend, user_id, new_articles_nb = 2):    
    user_embedding = get_embedding_from_user(user_id)
    df_scores_new = create_df_scores(list_new_articles, user_embedding)
    df_scores_recommend = create_df_scores(recommend, user_embedding)
    best_articles = get_best_articles_from_dfs_scores(df_scores_new, df_scores_recommend, new_articles_nb)
    return best_articles

def get_best_articles_from_dfs_scores(df1, df2, new_articles_nb = 2):
    df = df1.sort_values(
        by=['score'], ascending=False
    )[:new_articles_nb].append(
        df2, ignore_index=True
    ).sort_values(
        by=['score'], ascending=False
    )["article_id"][:5].to_list()
    return [int(x) for x in df]

def create_df_scores(list_articles, embedding_ref):
    df_scores = pd.DataFrame(list_articles)
    df_scores = df_scores.rename(columns={0:'article_id'})
    
    embeddings = get_embeddings_from_articles(list_articles)
    f = lambda x: np.dot(x, embedding_ref)/(np.linalg.norm(x)*np.linalg.norm(embedding_ref))
    scores = [f(xi) for xi in embeddings]
    
    df_compute = pd.DataFrame(scores)
    df_compute = df_compute.rename(columns={0:'score'})

    df_scores = df_scores.join(df_compute)
    
    return df_scores

def get_popular_articles(top=5):
    clicks_articles = clicks.groupby(['click_article_id']).size()
    return clicks_articles.sort_values(ascending=False)[:top].index.tolist()

def is_new_user(user_id):
    list_new_user = list_users_clicks['user_id'].tolist()
    return not user_id in list_new_user

def is_recent_user(user_id, threshold = 2):
    list_recent_user = list_users_clicks[list_users_clicks[0]<=2]['user_id'].tolist()
    return user_id in list_recent_user

def create_list_users_clicks():
    list_users_clicks = clicks.groupby(['user_id']).size().reset_index()
    return list_users_clicks


