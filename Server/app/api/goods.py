from flask_restful import reqparse,Resource
from .import api,auth
from ..models import Goods

class Goodss(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int, default=0,location='values')
        
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        result=[]
        for row in Goods.query.order_by(Goods.ID.desc()).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'name':row.Name,
                'img':row.Img,
                'prices':row.Prices,
                'number':row.Number
                })
        return result 
    
api.add_resource(Goodss,'/goods',endpoint='Goodss') 