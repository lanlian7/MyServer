from flask_restful import Resource,reqparse
from app.models import Medicine
from .import api,auth

class Medicines(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,locations='values')
        self.parser.add_argument('offset',type=int,default=0,locations='values')
        
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        result=[]
        for row in Medicine.query.limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'title':row.Title,
                'img':row.Img,
                'url':row.href
                })
        return result
        
api.add_resource(Medicines,'/medicines',endpoint='medicines')      