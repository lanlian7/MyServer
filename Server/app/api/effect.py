#coding=utf-8
from flask_restful import Resource,reqparse
from .import auth,api
from ..models import Effect,EffectItem

class Effects(Resource):
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
        for row in Effect.query.limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'type':row.Type,
                'name':row.Name,
                'img':row.Img,
                'url':row.Url
                })
        return result
      
class EffectItems(Resource):
    decorator=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('effectid',type=int,default=1,location='values')
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        effectid=args['effectid']
        result=[]
        for row in EffectItem.query.filter(EffectItem.EffectID==effectid).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'effectID':row.EffectID,
                'url':row.Url,
                'name':row.Name,
                'img':row.Img,
                'introduction':row.Introduction,
                'virtue':row.Virtue,
                'flag':row.Flag,
                'taboo':row.Taboo
                })
        return result    


api.add_resource(Effects,'/effect',endpoint='effect')  
api.add_resource(EffectItems,'/effect/effectitem',endpoint='effectitem')
