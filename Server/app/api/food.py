#coding=utf-8
from flask_restful import reqparse,Resource
from .import auth,api
from ..models import FoodItem,FoodItemContent,FoodItemImg,FoodItemMethod

import sys
reload(sys)

sys.setdefaultencoding('utf-8') 

class FoodItems(Resource):
    decorator=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('typeItemId',type=int,default=1,location='values')
        self.parser.add_argument('typeItemName',type=str,default='',location='values')
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        typeItemId=args['typeItemId']
        typeItemName=args['typeItemName']
        result=[]
        if typeItemName is None or typeItemName=='':
            for row in FoodItem.query.filter(FoodItem.TypeItemID==typeItemId).limit(limit).offset(offset).all():
                result.append({
                    'id':row.ID,
                    'typeItemID':row.TypeItemID,
                    'name':row.Name,
                    'url':row.Url,
                    'img':row.Img
                    })
            return result
        else:
            for row in FoodItem.query.filter(FoodItem.Name==typeItemName).limit(limit).offset(offset).all():
                result.append({
                    'id':row.ID,
                    'typeItemID':row.TypeItemID,
                    'name':row.Name,
                    'url':row.Url,
                    'img':row.Img
                    })
            return result
    
class FoodItemContents(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('foodItemId',type=int,default=1,location='values')
    
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        foodItemId=args['foodItemId']
        result=[]
        for row in FoodItemContent.query.filter(FoodItemContent.FoodItemID==foodItemId).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'content':row.Content,
                'ingredients':row.Ingredients,
                'accessories':row.Accessories,
                'foodItemID':row.FoodItemID
                })
        return result 

class FoodItemMethods(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('foodItemId',type=int,default=1,location='values')
    
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        foodItemId=args['foodItemId']
        result=[]
        for row in FoodItemMethod.query.filter(FoodItemMethod.FoodItemID==foodItemId).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'method':row.Method,
                'foodItemID':row.FoodItemID
                })
        return result 
    
    
class FoodItemImgs(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('foodItemId',type=int,default=1,location='values')
    
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        foodItemId=args['foodItemId']
        result=[]
        for row in FoodItemImg.query.filter(FoodItemImg.FoodItemID==foodItemId).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'img':row.Img,
                'foodItemID':row.FoodItemID
                })
        return result
           
api.add_resource(FoodItems,'/fooditem',endpoint='FoodItems')
api.add_resource(FoodItemContents,'/fooditem/content',endpoint='FoodItemContents')
api.add_resource(FoodItemMethods,'/fooditem/method',endpoint='FoodItemMethods')
api.add_resource(FoodItemImgs,'/fooditem/img',endpoint='FoodItemImgs')

