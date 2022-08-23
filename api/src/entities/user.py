from sqlalchemy import Column, String


from .entity import Entity, Base


class User(Entity, Base):
    __tablename__ = 'Users'

    Username = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False, unique=True)
    Email = Column(String, nullable=False, unique=True)
    Description = Column(String)
    Image = Column(String)

    def __init__(self, username, password, email, image=None, created_by="server", description=None):
        Entity.__init__(self, created_by)
        self.Username = username
        self.Password = password
        self.Email = email
        self.Description = description
        self.Image = image

    def json(self):
        return {
            "Id": self.Id,
            "Username": self.Username,
            "Email": self.Email,
            "Description": self.Description,
            "Image": self.Image,
            "CreatedAt": self.CreatedAt.strftime("%y-%m-%d"),
            "UpdatedAt": self.UpdatedAt.strftime("%y-%m-%d"),
            "LastUpdatedBy": self.LastUpdatedBy,
        }
