from flask_restful import reqparse,Resource
from . import api,auth
from ..models import Order
from .. import db

class Orders(Resource):
    decorators=[auth.login_required]
    
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('limit',type=int,default=128,location='values')
        self.parser.add_argument('offset',type=int, default=0,location='values')
        self.parser.add_argument('userid',type=int,default=1,location='values')
        self.parser.add_argument('pUserID',type=int,default=1,location='form')
        self.parser.add_argument('pGoodsID',type=int,default=1,locatio='form')
        self.parser.add_argument('ordernumber',type=int,default=1,localtion='form')
        self.parser.add_argument('price',type=float,defaul=0,location='form')
    def get(self):
        args=self.parser.parse_args()
        offset=args['offset']
        limit=args['limit']
        userID=args['userid']
        result=[]
        for row in Order.query.filter(Order.UserID==userID).order_by(Order.ID.desc()).limit(limit).offset(offset).all():
            result.append({
                'id':row.ID,
                'userID':row.UserID,
                'goodsID':row.GoodsID,
                'orderNumber':row.OrderNumber,
                'price':row.Price
                })
        return result  
    
    def post(self):
        args=self.parser.parser_args()
        userID=args['pUserID']
        goodsID=args['pGoodsID']
        number=args['ordernumber']
        price=args['price']
        order=Order(UserID=userID,GoodsID=goodsID,OrderNumber=number,Price=price)
        db.session.add(order)
        db.session.commit()
        return 'success'
         
    
    
api.add_resource(Orders,'/order',endpoint='order')