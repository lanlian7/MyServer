from flask_restful import reqparse,Resource
from . import api,auth
from ..models import Video

"""

"""
class Videos(Resource):
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
        for row in Video.query.order_by(Video.ID.desc()).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'title':row.Title,
                'contents':row.Contents,
                'url':row.Url,
                'img':row.Img,
                'count':row.Count,
                'releaseTime':row.ReleaseTime
                })
        return result 
    


    




api.add_resource(Videos,'/video',endpoint='video')


