from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/') 
def index(): 
	return 'hello'


@app.get('/about') # static routing
def about():
	return {'data':{'about page'}}


# @app.get('/blog/unpublished') 
# def show_unpublished():
# 	return {'data': 'Unpublished blogs'}

@app.get('/items/item-{item_id}') # dynamic routing
async def read_item(item_id: int):
	return {"item_id": item_id}

@app.get('/blog/{id}')
async def show_blog(id: int):
	return {'data': id}

@app.get('/blog?limit=10&published=true') # query parameters
def show_blog():
	return {'data': 'blog list'}


@app.get('/blog') # query parameters
async def show_blog(limit:int,published:bool):
	if published:
		return {'data': f'blog list of limit which are published : {limit}'}
	else:
		return {'data': f'blog list of limit: {limit}'}
	
class Blog(BaseModel): # pydantic model for blog
	title: str
	body: str
	published: Optional[bool]

@app.post('/blog') # post request
async def create_blog(blog: Blog):
	return {'bloginfo': f'Blog is created with title: {blog.title} and body: {blog.body} and published: {blog.published}','blog': blog} # returning the blog data as well