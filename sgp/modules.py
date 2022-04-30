from datetime import datetime
from enum import unique
from sgp import db


# Database Model (user's table)
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), unique=True, nullable=False)
    userFirstName = db.Column(db.String(20), unique=True, nullable=False)
    userLastName = db.Column(db.String(20))
    userEmail = db.Column(db.String(120), unique=True, nullable=False)
    user_phone_number = db.Column(db.String(10), unique=True)
    userProfilePic = db.Column(db.String(20), nullable=False, default='default.jpg')
    userPassword = db.Column(db.String(60), nullable=False)
    userStatus = db.Column(db.Boolean(), default=False)
    userGender = db.Column(db.Enum('male', 'femal', 'other', name='varcher'))
    userDateOfBirth = db.Column(db.Date())
    userLoginAt = db.Column(db.DateTime())
    userCreationDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    userRoles = db.Column(db.Enum('superAdmin', 'admin', 'student'))
    
    # Magical method for representing a class object
    def __repr__(self):
        return f"User('{self.username}, {self.userFirstName}, {self. userLastName}, {self.userEmail}, {self. user_phone_number}, {self. userProfilePic},{self.userPassword}, {self. userStatus}, {self. userGender} {self. userDateOfBirth}')"


# Database Model (Student table)
class Student(db.Model):
    studentMatricule = db.Column(db.Integer, preimary_key=True)
    studentFaculty = db.Column(db.String(20))
    studentPromotion = db.Column(db.String(20))
    studentDepartment = db.Column(db.String(20))

# Database Model (SuperAdmin table)
class SuperAdmin(db.Model):
    superAdminId = db.Column(db.Integer, primary_key=True)

# Database Model (Admin table)
class SuperAdmin(db.Model):
    adminId = db.Column(db.Integer, primary_key=True)

# Database Model (Bordereau table)
class SuperAdmin(db.Model):
    bordereauId = db.Column(db.Integer, primary_key=True)
    bordereauCode = db.Column(db.Text(), nullable=True),
    bordereauImg = db.Column(db.String(20), nullable=False, default='bordereau.jpg')
    paymentMotif = db.Column(db.String(20), nullable=False)
    timeSterp = db.Column(db.DateTime()) # Will be determined 
    accdemicYear = db.Column(db.String, nullable=False) # ForeignKey
    SendingTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


# Database Model (PaymentPlan table)
class PaymentPlan(db.Model): 
    paymentId =  db.Column(db.Integer, preimary_key=True)
    paymentName = db.Column(db.String(20), nullable=False)
    paymentAmount = db.Column(db.Integer, nullable=False)
    paymentSchadule =  db.Column(db.DateTime, nullable=False) # Will be determined 
    timeSterp = db.Column(db.DateTime, nullable=False) # Will be determined 
    accdemicYear = db.Column(db.String, nullable=False) # ForeignKey

# Database Model (Payment table)
class Payment(db.Model): 
    bordereauId = db.Column() # ForeignKey
    studentId = db.Column() # ForeignKey
    amount = db.Colun(db.Numeric(), nullable=False)
    paymentMotif  = db.Column(db.String(20), nullable=False)
    carancy = db.Column(db.String())
    timeSterp = db.Column(db.DateTime, nullable=False)
    accdemicYear = db.Column(db.String, nullable=False) # ForeignKey

# Database Model (Payment table)
class Payment(db.Model): 
    yearId = db.Column(db.Integer, preimary_key=True)
    yearName =  db.Column(db.String(20), nullable=False)
    timeSterp = db.Column(db.DateTime, nullable=False)