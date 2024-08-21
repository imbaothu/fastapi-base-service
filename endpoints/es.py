from typing import List, Optional
from fastapi import FastAPI, HTTPException
from elasticsearch import AsyncElasticsearch, NotFoundError

app = FastAPI()


class ESClient:
    def __init__(self):
        self.server = ""
        self.client: AsyncElasticsearch = None

    def init_config(self, config: dict):
        self.server = config["uri"]

    async def connect(self):
        self.client = AsyncElasticsearch(self.server)

    async def index_document(
        self, index_name: str, document: dict, doc_id: Optional[str] = None
    ):
        response = await self.client.index(index=index_name, body=document, id=doc_id)
        return response

    async def get_document(self, index_name: str, doc_id: str):
        try:
            response = await self.client.get(index=index_name, id=doc_id)
            return response
        except NotFoundError:
            raise HTTPException(status_code=404, detail="Document not found")

    async def search_documents(self, index_name: str, query: dict):
        response = await self.client.search(index=index_name, body=query)
        return response

    async def delete_document(self, index_name: str, doc_id: str):
        try:
            response = await self.client.delete(index=index_name, id=doc_id)
            return response
        except NotFoundError:
            raise HTTPException(status_code=404, detail="Document not found")
