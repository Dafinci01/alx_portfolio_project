from devchirp import db 
from devchirp.model import User




#delete all records rom user model

User.query.delete()

#commit update 
db.session.commit()
