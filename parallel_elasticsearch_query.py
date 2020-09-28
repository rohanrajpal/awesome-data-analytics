from multiprocessing import Pool
from pprint import pprint

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, connections
from p_tqdm import p_map
import os

body = { 
    "query": {
      "bool": {
        "must": [
            {
              "query_string" : {
              "query" : "*",
              "default_field" : "image_path"
              }
            },
            {
              "range": {
                "last_modified": {
                  "gte": "2014-11-01T00:00:00Z",
                  "lte": "2020-06-02T00:00:00Z"
                }
              }
              
            }
        ],
        "must_not": [
          {
            "query_string" : {
              "query" : "*thumb*",
              "default_field" : "image_path"
              }
          }
        ]
      }
    }
}

SLICES = 100
def dump_slice(slice_no):
    client=Elasticsearch([{'host':'localhost','port':9200}])
    s = Search(using=client,index='cdn_cmsuploads').from_dict(body)
    s = s.extra(slice={"id": slice_no, "max": SLICES})
    s = s.params(scroll='25m',request_timeout=120)
    es = connections.get_connection()

    totbytes = 0
    cnt = 0
    for d in s.scan():
        # print(d.to_dict())
        # break
        totbytes += d.size
        cnt += 1
    return totbytes,cnt

connections.create_connection(hosts=['localhost'])
result = p_map(dump_slice,list(range(SLICES)),num_cpus=SLICES)