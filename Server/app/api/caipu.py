#coding:utf8
from flask_restful import reqparse,Resource
from . import api,auth
from ..models import Caipu,Material,Methods

"""
类：Caipus
类方法：get(int limit,int offset)
return :json
"""
class Caipus(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
    """
    method:get
    :param limit:数量
    :param offset:偏移量
    :return:json数据
    """   
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        result=[]
        for row in Caipu.query.order_by(Caipu.ID).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'url':row.Url,
                'title':row.Title,
                'img':row.Img,
                'effect':row.Effect
                })
        return result

"""
类：Materials
类方法：get(int limit,int offset,int CaipuID)
return :json
""" 
class Materials(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('caipuID',type=int,default=1,location='values')
        
        
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        caipuID=args['caipuID']
        result=[]
        for row in Material.query.filter(Material.ID==caipuID).order_by(Material.ID).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'name':row.Name,
                'number':row.Number,
                'caipuId':row.CaipuID
                })
        return result 
    
 
"""
类：Methodss
类方法：get(int limit,int offset,int CaipuID)
return :json
"""  
class Methodss(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int,default=0,location='values')
        self.parser.add_argument('caipuID',type=int,default=1,location='values')
        
        
    def get(self):
        args=self.parser.parse_args()
        limit=args['limit']
        offset=args['offset']
        caipuID=args['caipuID']
        result=[]
        for row in Methods.query.filter(Methods.ID==caipuID).order_by(Methods.ID).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'src':row.Src,
                'gif':row.Gif,
                'title':row.Title,
                'content':row.Content,
                'caipuId':row.CaipuID
                })
        return result 

"""
web调用的api资源
:param ../caipu:this is a url ,return class caipus method get
:returns:json数据:
"""
api.add_resource(Caipus,'/caipu')
api.add_resource(Methodss,'/caipu/method')
api.add_resource(Materials,'/caipu/material')