from . import db  
class Myprofile(db.Model):     
    id = db.Column(db.Integer, primary_key=True)     
    first_name = db.Column(db.String(80))     
    last_name = db.Column(db.String(80))     
    username = db.Column(db.String(80), unique=True)     

    def is_authenticated(self):
        return True
      
    def is_anoymous(self):
        return False
    
    def is_active(self):
        return True
    
    def get_id(self):
        return "1001"
    
   # @classmethod
   # def get(cls,id):
   #     import pdb;pdb.set_trace()
   #     return cls.user_database.get(id)