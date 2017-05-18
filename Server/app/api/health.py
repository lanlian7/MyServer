from flask_restful import reqparse,Resource
from . import api,auth
from ..models import HealthAssessment,FoodTherapy

class HealthAssessments(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        
    
    
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        result=[]
        for row in HealthAssessment.query.order_by(HealthAssessment.ID).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'age':row.Age,
                'gender':row.Gender,
                'other':row.Other
                })
        return result

class FoodTherapys(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        
    
    
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        result=[]
        for row in FoodTherapy.query.order_by(FoodTherapy.ID).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'title':row.Title,
                'efficacy':row.Efficacy,
                'ingredients':row.Ingredients,
                'practice':row.Practice
                })
        return result
    
    


api.add_resource(HealthAssessments,'/health',endpoint='health')
api.add_resource(FoodTherapys,'/therapy',endpoint='therapy')