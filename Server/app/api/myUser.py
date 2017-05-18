from .import api,auth
from ..models import User,Login
from flask_restful import  reqparse, Resource
from .. import db


class Users(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int ,default=0,location='values')
        
        self.parser.add_argument('headImg',type=str,default='',location='form')
        self.parser.add_argument('nickName',type=str,default='',location='form')
        self.parser.add_argument('gender',type=str,default='',location='form')
        self.parser.add_argument('addr',type=str,default='',location='form')
        self.parser.add_argument('contributionValue',type=str,default='',location='form')
        self.parser.add_argument('collection',type=str,default='',location='form')
        self.parser.add_argument('shoppingCart',type=str,default='',location='form')
        self.parser.add_argument('publish',type=str,default='',location='form')
        
    def get(self):
        args=self.parser.parse_args()
        result=[]
        offset=args['offset']
        limit=args['limit']
        for row in User.query.order_by(User.ID.desc()).offset(offset).limit(limit).all():
            result.append({
            'id':row.ID,
            'headImg':row.HeadImg,
            'nickName':row.NickName,
            'gender':row.Gender,
            'addr':row.Addr,
            'contributionValue':row.ContributionValue,
            'collection':row.Collection,
            'shoppingCart':row.ShoppingCart,
            'publish':row.Publish,
             })
        return result
    
    def post(self):
        args=self.parser.parse_args()
        headImg=args['headImg']
        nickName=args['nickName']
        gender=args['gender']
        addr=args['addr']
        contributionValue=args['contributionValue']
        collection=args['collection']
        shoppingCart=args['shoppingCart']
        publish=args['publish']
        user=User(HeadImg=headImg,NickName=nickName,Gender=gender,Addr=addr,ContributionValue=contributionValue,Collection=collection,ShoppingCart=shoppingCart,Publish=publish)
        db.session.add(user)
        db.session.commit()
        return 'success'
    
 
    
class Logins(Resource):
    decoretors=[auth.login_required]
    
    def get(self):
        result=[]
        for row in Login.query.all():
            result.append({
                'id':row.ID,
                'tel':row.Tel,
                'code':row.Code
                })
        print result
        return result
    
api.add_resource(Users, '/user', endpoint='user')
api.add_resource(Logins,'/login',endpoint='login')
