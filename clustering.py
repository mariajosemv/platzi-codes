import random 
import math
import itertools

from bokeh.plotting import figure, show, output_file
from bokeh.models import LabelSet, ColumnDataSource
from bokeh.palettes import Category20 as palette

 
def get_random_coordinates():
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        return (x, y)
    
def get_euclidean_distance(vector_1, vector_2):
        d = math.sqrt((vector_2[0]-vector_1[0])**2 + \
                      (vector_2[1] - vector_1[1])**2)
        return round(d, 2) 
       
def list_of_random_vectors(n_vectors):
    '''
    Generate a list of random vectors
    list_of_random_vectors = [(x1,y1), (x2,y2), (x3,y3)...]
    '''
    list_of_random_vectors = []
    for _ in range(n_vectors):
        list_of_random_vectors.append(get_random_coordinates()) 
    return list_of_random_vectors

def archive(lista):
    '''
    Input: list_of_random_vectors
    Generate a dictionary
    Returns:
    archive = {((x1, y1), (x2, y2)): m, ((x3, y3), (x4, y4)): n}
    where n is given by get_euclidean_distance()
    '''
    archive = {}

    for vector_1, vector_2 in itertools.combinations(lista, 2):
        archive[vector_1,vector_2] = get_euclidean_distance(vector_1,vector_2) 

    return archive    

def closest_vectors(dictionary):
    """
    Input: the dictionary archive
    Generate a tuple with the most closest vectors
    returns ((x1,y1),(x2,y2))
    in here, vector_1 = (x1,y1) and vector_2 = (x2,y2)
    """
    min_value = min(dictionary.values())

    key_for_min_value = [key for key in dictionary if dictionary[key] == min_value] 
    vector_1 = key_for_min_value[0][0]
    vector_2 = key_for_min_value[0][1]
    return (vector_1, vector_2)

def middle_vector(vector1, vector2):
    """
    input: vector_1: (x1,y1); vector_2: (x2,y2)
    returns the middle vector (x,y)
    """
    x1 = vector1[0]
    x2 = vector2[0]
    y1 = vector1[1]
    y2 = vector2[1]
    x_medio = round((x1+x2)*0.5, 2)
    y_medio = round((y1+y2)*0.5, 2)
    middle_vector = (x_medio, y_medio)
    return middle_vector

def from_tuple_to_list(list_of_tuples):
    """
    input: list of tuples [(x1,y1), (x2,y2), (x3,y3)...]
    output: ([x1,x2,x3...],[y1,y2,y3...])
    """
    x = []
    for i in range(len(list_of_tuples)):
        x.append(list_of_tuples[i][0])

    y = []
    for i in range(len(list_of_tuples)):
        y.append(list_of_tuples[i][1])

    return x, y

n = 0

def clustering(random_list):
    '''
    1. Take the_closest_vectors of random_list and agroup them into cluster
    2. Replace the closest_vectors for the_middle_point 
    3. the_middle_point is now a vector and represents a cluster
    4. Repeat 1 till there is no more vectors to agroup
    '''

    global n
    vectors_dict = dict(zip(random_list, range(len(random_list))))
    list_xy = from_tuple_to_list(random_list)
    x = list_xy[0] # list_x_random
    y = list_xy[1] # list_y_random
    names = ['0','1','2','3','4']
   
    # plotting the random vectors
    graph = figure(title = 'Hierarchical clustering', x_axis_label = 'x', y_axis_label = 'y')
    graph.circle(x, y)
    source = ColumnDataSource(data=dict(x=x, y=y, names=names))
    labels = LabelSet(x='x', y='y', text='names', level='glyph', x_offset=5, y_offset=5, source=source, render_mode='canvas')
    graph.add_layout(labels)

    # keep clustering till there is no more items to agroup
    while len(random_list) != 1:
        archive_of_distances = archive(random_list)
        
        if len(vectors_dict) > 1:
            cluster = []

            # get the_closest_vectors
            the_closest_vectors = closest_vectors(archive_of_distances)
            vector_1 = the_closest_vectors[0]
            vector_2 = the_closest_vectors[1]

            print(' ' *80)
            print(f"The closest vectors are: {vector_1}, {vector_2}")
            print(f"So they are part of the cluster {n+1}")

            # add them into the cluster
            cluster.append(vector_1)
            cluster.append(vector_2)
            
            # calculate the middle point of these vectors (cluster)
            the_middle_vector = middle_vector(vector_1, vector_2)

            print(f"And the cluster {n+1} is: {the_middle_vector}")
            print(' ' *80)

            # delete the_closest_vectors from the random_list
            random_list.remove(vector_1) 
            random_list.remove(vector_2)

            # add the middle vector to the random_list
            random_list.append(the_middle_vector)

            # plot that middle vector (cluster)
            ratio = get_euclidean_distance(vector_1, vector_2)
            graph.circle(the_middle_vector[0], the_middle_vector[1], radius= ratio, color = palette[11][(len(vectors) - len(vectors_dict)) % len(palette[11])], fill_alpha = 0.1 ,legend_label= f"cluster {n+1}")
            n = n+1
        else:
            break
        
    show(graph)
    
if __name__ == '__main__':
    print('*' * 80)
    number = int(input("Choose the number of vectors: "))
    print(' ' * 80)

    vectors = list_of_random_vectors(number)
    print(f"The random vectors are: {vectors}")

    clustering(vectors)
