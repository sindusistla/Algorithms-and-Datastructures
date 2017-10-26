from numpy import *

def normalize_ratings(ratings,did_rate):
    '''We need to normalize the data by first finding out the mean of the rows individually and subracting
    the row_mean from each and every non zero value in that particular row'''

    num_movies=ratings.shape[0];

    ratings_mean=zeros(shape =(num_movies,1)); '''10 X 1'''
    ratings_norm=zeros(shape = ratings.shape); '''Same as shape of ratings'''
    for i in range(num_movies):
        # Get all the indexes where there is 1
        idx=where(did_rate[i]==1)[0];
        ratings_mean[i]=mean(ratings[i,idx]);
        ratings_norm[i,idx]=ratings[i,idx]-ratings_mean[i];
    return ratings_norm,ratings_mean


def main():
    num_movie=10
    num_users=6
    ratings_norm=0;
    ratings_mean=0;
    num_features=3; # A user likes comedy then any movie which has comedy is liked by him

    ratings=random.randint(11,size=(num_movie,num_users));
    print (ratings);

    '''Form  a matrix which depicts wether a movie is rated or not '''

    did_rate=(ratings != 0)*1;
    print (did_rate)

    jaya_ratings=zeros((num_movie,1))

    jaya_ratings[0]=8;
    jaya_ratings[4]=7;
    jaya_ratings[7]=3;

    #print (jaya_ratings);
    '''We get a sparsed matrix it is practically not possible for all the movie to give rating'''

    '''append jaya ratings to ratings matrix'''

    ratings=append(jaya_ratings,ratings,axis=1);
    did_rate=append(((jaya_ratings !=0)*1),did_rate,axis=1);
    print (ratings);
    print (did_rate);

    '''Now we need to normalize the data '''
    ratings_norm,ratings_mean=normalize_ratings(ratings, did_rate)
    print(ratings_norm, ratings_mean);

    '''Add features'''
    movie_features=random.randn(num_movie,num_features);
    user_prefs=random.randn(num_users,num_features);
    '''movie and user features are flattened and appended to form a column matrix'''
    intial_X_and_theta=r_[movie_features.T.flatten(),user_prefs.T.flatten()]
    print (movie_features)
main();