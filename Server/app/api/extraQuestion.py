from flask_restful import reqparse,Resource
from . import api,auth
from ..models import ExtraQuestion,ExtraQuestionItem


class ExtraQuestions(Resource):
    decorator=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        result=[]
        for row in ExtraQuestion.query.limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'url':row.Url,
                'img':row.Img,
                'title':row.Title,
                'brief':row.Brief
                })
        return result


class ExtraQuestionItems(Resource):
    decorator=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('extraQuestionId',type=int,default=1,location='values')
        
        
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        extraQuestionID=args['extraQuestionId']
        result=[]
        for row in ExtraQuestionItem.query.filter(ExtraQuestionItem.ExtraQuestionID==extraQuestionID).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'content':row.Content,
                'extraQuestionId':row.ExtraQuestionID
                })
        return result

api.add_resource(ExtraQuestions,'/extraQuestion',endpoint='ExtraQuestions')
api.add_resource(ExtraQuestionItems,'/extraQuestionItem',endpoint='ExtraQuestionItems')
