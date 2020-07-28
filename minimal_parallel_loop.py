# parallelize any for loop with a cool progress bar XD
__author__ = 'Rohan Rajpal'

from p_tqdm import p_map

def chunks(l,n):
  for i in range(0,len(l),n):
    yield l[i:i+n]

def your_function(chunk):
    unique_ids = {}
    for i in chunk:
        unique_ids[i] = True
    return unique_ids

total_posts = 1000
n_processors = 28
chunk_size = total_posts // n_processors
result = p_map(your_function,list(chunks(list(range(total_posts)),chunk_size)),num_cpus=n_processors)
result = {k:v for element in result for k,v in element.items()}
print(result)
