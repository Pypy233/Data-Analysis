import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('/Users/py/Downloads/pydata-book-2nd-edition/'
                      'datasets/movielens/users.dat', sep='::', header=None,
                      names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('/Users/py/Downloads/pydata-book-2nd-edition/'
                        'datasets/movielens/ratings.dat', sep='::', header=None,
                        names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('/Users/py/Downloads/pydata-book-2nd-edition/'
                      'datasets/movielens/movies.dat', sep='::', header=None,
                       names=mnames, engine='python')


def print_table():
    print(users[:5])
    print()
    print(ratings[:5])
    print()
    print(movies[:5])


# merge
def merge_table():
    data = pd.merge(pd.merge(users, ratings), movies)
    return data


# A bug occurs that the new panda version uses key words 'index' and 'columns', so I changed the code
def mean_ratings():
    data = merge_table().pivot_table('rating', index='title', columns='gender', aggfunc='mean')
    return data


# print(mean_ratings())

def get_active_movie(active_number):
    ratings_by_title = merge_table().groupby('title').size()
    # print(ratings_by_title)
    active_titles = ratings_by_title.index[ratings_by_title >= active_number]
    active_mean_ratings = mean_ratings().ix[active_titles]
    return active_mean_ratings


# print(get_active_movie(250))

def get_top_ratings(top_number):
    top_female_ratings = mean_ratings().sort_index(by='F', ascending=False)
    return top_female_ratings[:top_number]


# print(get_top_ratings(10))

def get_mean_diff():
    mean_ratings_list = mean_ratings()
    mean_ratings_list['diff'] = mean_ratings_list['M'] - mean_ratings_list['F']
    sort_by_diff = mean_ratings_list.sort_index(by='diff')
    return sort_by_diff


# print(get_mean_diff()[:15])
