import grequests
import gevent.monkey
gevent.monkey.patch_all()
from fastapi import FastAPI, Query
from app.fetch_data import single_fetch_content
from app.evaluation import single_evaluation, do_group_evaluation
from app.data_getter import populate_dict
from typing import List, Union


app = FastAPI()

@app.get('/')
async def home():
    return {'message': 'fastapi-github-evaluator, access /docs for documentation, /evaluation/{user} to single evaluation and /group-evaluation for simultaneous evaluation'}

@app.get('/evaluation/{user}')
async def evaluation(user: str):
    return single_evaluation(populate_dict(single_fetch_content(user)))


@app.get('/group-evaluation')
async def group_evaluation(user: Union[List[str], None] = Query(default=None)):
    return do_group_evaluation(user)