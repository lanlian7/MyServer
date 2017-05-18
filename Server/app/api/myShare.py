from flask_restful import reqparse,Resource
from . import api,auth
from ..models import Question,Experience,Comment,Answer,User
from ..import db
from datetime import datetime,date

import json 
  
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


class Questions(Resource):
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('user_id',type=int,default=0,location='values')
        self.parser.add_argument('title',type=str,default='',location='form')
        self.parser.add_argument('content',type=str,default='',location='form')
        self.parser.add_argument('quser_id',type=int,default=0,location='form')
        
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        userID=args['user_id']
        result=[]
        for row in Question.query.filter(Question.UserID==userID).order_by(Question.ID).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'title':row.Title,
                'contents':row.Contents
                })
        return result
    
    def post(self):
        args=self.parser.parse_args()
        quser_id=args.get('quser_id')
        if User.query.filter(User.ID==quser_id).first() is None:
            return 'cannot find user please register first'
        title=args.get('title')
        content=args.get('content')
        question=Question(Title=title,Contents=content,UserID=quser_id)
        db.session.add(question)
        db.session.commit()
        return "success"

class Experiences(Resource):
    
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int ,default=0,location='values')
        self.parser.add_argument('user_id',type=int,default=0,location='values')
        self.parser.add_argument('title',type=str,default='',location='form')
        self.parser.add_argument('content',type=str,default='',location='form')
        self.parser.add_argument('quser_id',type=int,default=0,location='form')
        
    def get(self):
        args=self.parser.parse_args()
        result=[]
        offset=args['offset']
        limit=args['limit']
        userID=args['user_id']
        for row in Experience.query.filter(Experience.UserID==userID).order_by(Experience.ID).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'title':row.Title,
                'contents':row.Contents
                })
        return result  
    
    def post(self):
        args=self.parser.parse_args()
        quser_id=args.get('quser_id')
        if User.query.filter(User.ID==quser_id).first() is None:
            return 'cannot find user please register first'
        title=args.get('title')
        content=args.get('content')
        experience=Experience(Title=title,Contents=content,UserID=quser_id)
        db.session.add(experience)
        db.session.commit()
        return "success"  
      
class Comments(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('user_id',type=int,default=0,location='values')
        self.parser.add_argument('experience_id',type=int,default=0,location='values')
        self.parser.add_argument('body',type=str,default='',location='form')
        self.parser.add_argument('Puser_id',type=int, default=0,location='form')
        
        
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
                'id':row.ID,
                'body':row.Body,
                'timestamp':time  
                })
        return result
    def post(self):
        args=self.parser.parse_args()
        body=args['body']
        Puser_id=args['Puser_id']
        comment=Comment(Body=body,Timestamp=datetime.utcnow(),User_id=Puser_id)
        db.session.add(comment)
        db.session.commit()
        return 'success'
          
        
class Answers(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('user_id',type=int,default=0,location='values')
        self.parser.add_argument('question_id',type=int,default=0,location='values')
        self.parser.add_argument('body',type=str,default='',location='form')
        self.parser.add_argument('Puser_id',type=int, default=0,location='form')
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
                'id':row.ID,
                'body':row.Body,
                'timestamp':time   
                })
        return result  
    
    def post(self):
        args=self.parser.parse_args()
        body=args['body']
        Puser_id=args['Puser_id']
        answer=Answer(Body=body,Timestamp=datetime.utcnow(),User_id=Puser_id)
        db.session.add(answer)
        db.session.commit()
        return 'success'
                   
api.add_resource(Questions,'/question',endpoint='question')
api.add_resource(Experiences,'/experience',endpoint='experience')
api.add_resource(Comments,'/comment',endpoint='comment')
api.add_resource(Answers,'/answer',endpoint='anwser')