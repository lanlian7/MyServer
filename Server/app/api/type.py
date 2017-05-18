#coding=utf-8
from flask_restful import Resource,reqparse
from .import auth,api
from ..models import Type,TypeItem

class Types(Resource):
    decorator=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        result=[]
        for row in Type.query.limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'item':row.Item,
                'name':row.Name,
                'img':row.Img,
                'url':row.Url
                })
        return result
      
class TypeItems(Resource):
    decorator=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('typeid',type=int,default=1,location='values')
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        typeid=args['typeid']
        result=[]
        for row in TypeItem.query.filter(TypeItem.typeID==typeid).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'typeID':row.typeID,
                'url':row.Url,
                'name':row.Name,
                'img':row.Img,
                'introduction':row.Introduction,
                'virtue':row.Virtue,
                'taboo':row.Taboo
                })
        return result    


api.add_resource(Types,'/type',endpoint='type')  
api.add_resource(TypeItems,'/type/typeitem',endpoint='typeitem')
