from flask_restful import Resource,reqparse
from ..models import Tags
from .import api,auth

class Tagss(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        result=[]
        for row in Tags.query.limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'title':row.Title,
                'url':row.href
                })
        return result
        
        
api.add_resource(Tagss,'/tags',endpoint='tags')
        