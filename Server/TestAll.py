#coding=utf-8


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'I Love C++!',
    'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:041166@localhost:3306/myserver',
    'SQLALCHEMY_COMMIT_ON_TEARDOW': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': True
})


from datetime import date  
from datetime import datetime  
  
class JsonExtendEncoder(json.JSONEncoder):  
    """  
        This class provide an extension to json serialization for datetime/date.  
    """  
    def default(self, o):  
        """  
            provide a interface for datetime/date  
        """  
        if isinstance(o, datetime):  
            return o.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(o, date):  
            return o.strftime('%Y-%m-%d')  
        else:  
            return json.JSONEncoder.default(self, o)  
        
        
db = SQLAlchemy(app,use_native_unicode="utf8")
Base=db.Model

"""
======
class Ciapu mode
======
:param id
:param url
:param img
"""
class Caipu(Base):
    __tablename__='caipu'
    
    ID=db.Column(db.Integer,primary_key=True)
    Url=db.Column(db.String(200))
    Title=db.Column(db.String(200))
    Img=db.Column(db.String(200))
    Effect=db.Column(db.String(300))
    kinds=db.Column(db.String(100))
    Materials = db.relationship('Material', backref='Caipu', lazy='dynamic')
    Methodss=db.relationship('Methods',backref='Caipu',lazy='dynamic')

class Material(Base):
    __tablename__='Material'    
    
    ID = db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(50))
    Number=db.Column(db.String(50))
    CaipuID=db.Column(db.Integer,db.ForeignKey(Caipu.ID))
    
class Methods(Base):
    __tablename__='methods'
    
    ID=db.Column(db.Integer,primary_key=True)
    Src=db.Column(db.String(200))
    Gif=db.Column(db.String(200))
    Title=db.Column(db.String(200))
    Content=db.Column(db.String(200))
    CaipuId=db.Column(db.Integer,db.ForeignKey(Caipu.ID))

class Login(Base):
    __tablename__='login'
    
    ID=db.Column(db.Integer,primary_key=True)
    Tel=db.Column(db.String(20), nullable=False)
    Code=db.Column(db.String(10),nullable=False)

class User(Base):
    __tablename__='user'
    
    ID=db.Column(db.Integer,primary_key=True)
    HeadImg=db.Column(db.String(100))
    NickName=db.Column(db.String(50))
    Gender=db.Column(db.String(10))
    Addr=db.Column(db.String(500))
    ContributionValue=db.Column(db.String(100))
    Collection=db.Column(db.String(500))
    ShoppingCart=db.Column(db.String(500))
    Publish=db.Column(db.String(500))
    Questions = db.relationship('Question', backref='User', lazy='dynamic')
    Experiences = db.relationship('Experience', backref='User', lazy='dynamic')
    Orders=db.relationship('Order',backref='User',lazy='dynamic')


class HealthAssessment(Base):
    __tablename__='health_assessment'
    
    ID=db.Column(db.Integer,primary_key=True)
    Age=db.Column(db.Integer,nullable=False)
    Gender=db.Column(db.String(10),nullable=False)
    Other=db.Column(db.String(200))
    
class FoodTherapy(Base):
    __tablename__='food_therapy'
    
    ID=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(50),nullable=False)
    Efficacy=db.Column(db.String(200),nullable=False)
    Ingredients=db.Column(db.String(200),nullable=False)
    Practice=db.Column(db.String(200),nullable=False)
    
class Question(Base):
    __tablename__='question'
    
    ID=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(50),nullable=False)
    Contents=db.Column(db.String(200),nullable=False)
    UserID=db.Column(db.Integer,db.ForeignKey(User.ID))
    
  
class Answer(Base):
    __tablebname__='answer'
    
    ID=db.Column(db.Integer,primary_key=True)
    Body=db.Column(db.String(200),nullable=False)
    Timestamp=db.Column(db.Date,nullable=False)
    Question_id=db.Column(db.Integer,db.ForeignKey(Question.ID))
    User_id=db.Column(db.Integer,db.ForeignKey(User.ID))

class Experience(Base):
    __tablename__='experience'
    
    ID=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(50),nullable=False)
    Contents=db.Column(db.String(200),nullable=False)
    UserID=db.Column(db.Integer,db.ForeignKey(User.ID))
   
class Comment(Base):
    __tablebname__='comment'
    
    ID=db.Column(db.Integer,primary_key=True)
    Body=db.Column(db.String(200),nullable=False)
    Timestamp=db.Column(db.Date,nullable=False)
    Experience_id=db.Column(db.Integer,db.ForeignKey(Experience.ID))
    User_id=db.Column(db.Integer,db.ForeignKey(User.ID)) 

    
class Goods(Base):
    __tablename__='goods'
    
    ID=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(100),nullable=False)
    Img=db.Column(db.String(100))
    Prices=db.Column(db.Float,nullable=False)
    Number=db.Column(db.Integer,nullable=False)
    
    
class Order(Base):
    __tablename__='order'
    
    ID=db.Column(db.Integer,primary_key=True)
    UserID=db.Column(db.Integer,db.ForeignKey(User.ID))
    GoodsID=db.Column(db.Integer,db.ForeignKey(Goods.ID))
    OrderNumber=db.Column(db.Integer)
    Price=db.Column(db.Float)

class Video(Base):
    __tablename__='video'
    
    ID=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(100),nullable=False)
    Contents=db.Column(db.String(200),nullable=False)
    Url=db.Column(db.String(300),nullable=False)
    Img=db.Column(db.String(200))
    Count=db.Column(db.String(40))
    ReleaseTime=db.Column(db.String(50))


class Tags(Base):
    __tablename__='tags'
    
    ID=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(200))
    Url=db.Column(db.String(200))        

from flask_restful import Api
from flask_httpauth import HTTPBasicAuth

api=Api(app)
auth=HTTPBasicAuth()

session=db.session

developers={
    'Doris':'Doris'
    }

@auth.get_password
def get_password(username):
    return None if username not in developers else developers[username]


from flask_restful import reqparse,Resource

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
                'ID':row.ID,
                'Age':row.Age,
                'Gender':row.Gender,
                'Other':row.Other
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
                'ID':row.ID,
                'Title':row.Title,
                'Efficacy':row.Efficacy,
                'Ingredients':row.Ingredients,
                'Practice':row.Practice
                })
        return result
    
class Questions(Resource):
    decorators=[auth.login_required]
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('user_id',type=int,default=0,location='values')
        
    
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        userID=args['user_id']
        result=[]
        for row in Question.query.filter(Question.UserID==userID).order_by(Question.ID).limit(limit).offset(offset).all():
            result.append({
                'ID':row.ID,
                'Title':row.Title,
                'Contents':row.Contents
                })
        return result


class Experiences(Resource):
    
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int ,default=0,location='values')
        self.parser.add_argument('user_id',type=int,default=0,location='values')
    
    def get(self):
        args=self.parser.parse_args()
        result=[]
        offset=args['offset']
        limit=args['limit']
        userID=args['user_id']
        for row in Experience.query.filter(Experience.UserID==userID).order_by(Experience.ID).limit(limit).offset(offset).all():
            result.append({
                'ID':row.ID,
                'Title':row.Title,
                'Contents':row.Contents
                })
        return result  
            
class Comments(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('user_id',type=int,default=0,location='values')
        self.parser.add_argument('experience_id',type=int,default=0,location='values')
        
    def get(self):
        args=self.parser.parse_args()
        result=[]
        offset=args['offset']
        limit=args['limit']
        userID=args['user_id']
        ExperienceID=args['experience_id']
        for row in Comment.query.filter(Comment.User_id==userID).filter(Comment.Experience_id==ExperienceID).order_by(Comment.ID).limit(limit).offset(offset).all():
            ds = json.dumps(row.Timestamp, cls=JsonExtendEncoder)  
            time=json.loads(ds)
            result.append({
                'ID':row.ID,
                'Body':row.Body,
                'Timestamp':time
                })
        return result  
        
class Answers(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('user_id',type=int,default=0,location='values')
        self.parser.add_argument('question_id',type=int,default=0,location='values')
        
    def get(self):
        args=self.parser.parse_args()
        result=[]
        offset=args['offset']
        limit=args['limit']
        userID=args['user_id']
        QuestionID=args['question_id'] 
        for row in Answer.query.filter(Answer.User_id==userID).filter(Answer.Question_id==QuestionID).order_by(Answer.ID).limit(limit).offset(offset).all():
            ds = json.dumps(row.Timestamp, cls=JsonExtendEncoder)  
            time=json.loads(ds)
            result.append({
                'ID':row.ID,
                'Body':row.Body,
                'Timestamp':time   
                })
        return result 
    
class Users(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int ,default=0,location='values')

    def get(self):
        args=self.parser.parse_args()
        result=[]
        offset=args['offset']
        limit=args['limit']
        for row in User.query.order_by(User.ID.desc()).offset(offset).limit(limit).all():
            result.append({
            'ID':row.ID,
            'HeadImg':row.HeadImg,
            'NickName':row.NickName,
            'Gender':row.Gender,
            'Addr':row.Addr,
            'ContributionValue':row.ContributionValue,
            'Collection':row.Collection,
            'ShoppingCart':row.ShoppingCart,
            'Publish':row.Publish,
             })
        return result
 
    
class Logins(Resource):
    decoretors=[auth.login_required]
    
    def get(self):
        result=[]
        for row in Login.query.all():
            result.append({
                'ID':row.ID,
                'Tel':row.Tel,
                 'Code':row.Code
                })
        print result
        return result
    
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
                'ID':row.ID,
                'Title':row.Title,
                'Contents':row.Contents,
                'Url':row.Url,
                'Img':row.Img,
                'Count':row.Count,
                'ReleaseTime':row.ReleaseTime
                })
        return result 
    

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
                'ID':row.ID,
                'Name':row.Name,
                'Img':row.Img,
                'Prices':row.Prices,
                'Number':row.Number
                })
        return result  
    
class Orders(Resource):
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
        for row in Order.query.order_by(Order.ID.desc()).limit(limit).offset(offset).all():
            result.append({
                'ID':row.ID,
                'userID':row.UserID,
                'GoodsID':row.GoodsID,
                'OrderNumber':row.OrderNumber,
                'Price':row.Price
                })
        return result  

class Caipus(Resource):
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
        for row in Caipu.query.order_by(Caipu.ID).limit(limit).offset(offset).all():
            result.append({
                'ID':row.ID,
                'Url':row.Url,
                'Title':row.Title,
                'Img':row.Img,
                'Effect':row.Effect
                })
        return result
    
class Materials(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('CaipuID',type=int,default=1,location='values')
        
        
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        caipuID=args['CaipuID']
        result=[]
        for row in Material.query.filter(Material.CaipuID==caipuID).order_by(Material.ID).limit(limit).offset(offset).all():
            result.append({
                'ID':row.ID,
                'Name':row.Name,
                'Number':row.Number,
                'CaipuId':row.CaipuID
                })
        return result 
    
    
class Methodss(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('CaipuID',type=int,default=1,location='values')
        
        
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        caipuID=args['CaipuID']
        result=[]
        for row in Methods.query.filter(Methods.CaipuId==caipuID).order_by(Methods.ID).limit(limit).offset(offset).all():
            result.append({
                'ID':row.ID,
                'Src':row.Src,
                'Gif':row.Gif,
                'Title':row.Title,
                'Content':row.Content,
                'CaipuId':row.CaipuId
                })
        return result 

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
                'ID':row.ID,
                'Title':row.Title,
                'Url':row.Url
                })
        return result
        
        
api.add_resource(Tagss,'/tags',endpoint='tags')
        
api.add_resource(Caipus,'/caipu',endpoint='caipu')
api.add_resource(Methodss,'/caipu/method',endpoint='method')
api.add_resource(Materials,'/caipu/material',endpoint='material')   
    
api.add_resource(HealthAssessments,'/health',endpoint='health')
api.add_resource(FoodTherapys,'/therapy',endpoint='therapy')

api.add_resource(Questions,'/question',endpoint='question')
api.add_resource(Experiences,'/experience',endpoint='experience')
api.add_resource(Comments,'/comment',endpoint='comment')
api.add_resource(Answers,'/answer',endpoint='anwser')

api.add_resource(Users, '/user', endpoint='user')
api.add_resource(Logins,'/login',endpoint='login')



api.add_resource(Videos,'/video',endpoint='video')
api.add_resource(Goodss,'/goods',endpoint='goods')
api.add_resource(Orders,'/order',endpoint='order')


if __name__ == '__main__':
    app.run(debug=True)
    