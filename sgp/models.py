
from datetime import datetime
from enum import unique
from lib2to3.pytree import Base
from operator import index
from tokenize import String

from sqlalchemy import Column, ForeignKey
from sgp import db


# Database Model (user's table)
class User(Base):
    __tablename__= 'user'
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20),index=True, unique=True, nullable=False)
    userFirstName = db.Column(db.String(20), nullable=False)
    userLastName = db.Column(db.String(20))
    userEmail = db.Column(db.String(120), unique=True, index=True, nullable=False)
    user_phone_number = db.Column(db.String(10), unique=True)
    userProfilePic = db.Column(db.String(20), nullable=False, default='default.jpg')
    userPassword = db.Column(db.String(128))
    userStatus = db.Column(db.Boolean(), default=False)
    userGender = db.Column(db.Enum('male', 'femal', 'other', name='varcher'))
    userDateOfBirth = db.Column(db.Date())
    userLoginAt = db.Column(db.DateTime())
    userCreationDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usertype = db.Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'user',
        'polymorphic_on':usertype
    }
    
    # Magical method for representing a class object
    def __repr__(self):
        return f"User('{self.userName}, {self.userEmail}, {self. user_phone_number}')"


# Database Model (Student table)
class Student(User):
    __tablename__= 'student'
    studentId = db.Column(db.Integer, ForeignKey('user.userId'), preimary_key=True)
    studentMatricule = db.Column(db.Integer, unique=True)
    studentFaculty = db.Column(db.String(20))
    studentPromotion = db.Column(db.String(20))
    __mapper_args__ = {
       'polymorphic_identity':'Student',
    }


# Database Model (SuperAdmin table)
class SuperAdmin(User):
    superAdminId = db.Column(db.Integer, ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
       'polymorphic_identity':'SuperAdmin',
    }


# Database Model (Admin table)
class admin(User):
    adminId =  db.Column(db.Integer, ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
       'polymorphic_identity':'admin',
    }

# # Database Model (Bordereau table)
# class bordereau(db.Model):
#     bordereauId = db.Column(db.Integer, primary_key=True)
#     bordereauCode = db.Column(db.Text(), nullable=True),
#     bordereauImg = db.Column(db.String(20), nullable=False, default='bordereau.jpg')
#     paymentMotif = db.Column(db.String(20), nullable=False)
#     timeSterp = db.Column(db.DateTime()) # Will be determined 
#     accdemicYear = db.Column(db.String, nullable=False) # ForeignKey
#     SendingTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


# # Database Model (PaymentPlan table)
# class PaymentPlan(db.Model): 
#     paymentId =  db.Column(db.Integer, preimary_key=True)
#     paymentName = db.Column(db.String(20), nullable=False)
#     paymentAmount = db.Column(db.Integer, nullable=False)
#     paymentSchadule =  db.Column(db.DateTime, nullable=False) # Will be determined 
#     timeSterp = db.Column(db.DateTime, nullable=False) # Will be determined 
#     accdemicYear = db.Column(db.String, nullable=False) # ForeignKey

# # Database Model (Payment table)
# class Payment(db.Model): 
#     bordereauId = db.Column() # ForeignKey
#     studentId = db.Column() # ForeignKey
#     amount = db.Colun(db.Numeric(), nullable=False)
#     paymentMotif  = db.Column(db.String(20), nullable=False)
#     carancy = db.Column(db.String())
#     timeSterp = db.Column(db.DateTime, nullable=False)
#     accdemicYear = db.Column(db.String, nullable=False) # ForeignKey

# # Database Model (AccademicYear table)
# class accademicYear(db.Model): 
#     yearId = db.Column(db.Integer, preimary_key=True)
#     yearName =  db.Column(db.String(20), nullable=False)
#     timeSterp = db.Column(db.DateTime, nullable=False)