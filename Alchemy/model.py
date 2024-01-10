from sqlalchemy.orm import declarative_base,validates,sessionmaker

from sqlalchemy import Column,BigInteger,Integer,String,DateTime,Boolean,Enum,text

from sqlalchemy import create_engine

from datetime import datetime

Base=declarative_base()

db_uri="postgresql://postgres:VAgUbmuGahd07njl@db.pssbujkmzspdgqugjdzv.supabase.co:5432/postgres"


engine=create_engine(db_uri)

Session=sessionmaker(bind=engine)



session=Session()


class Student(Base):

    __tablename__ = 'student'

    id=Column(Integer,primary_key=True)
    name=Column(String(50),nullable=False)
    email=Column(String(250),nullable=False,unique=True)
    phone=Column(Integer,nullable=False)
    is_married=Column(Boolean,nullable=False,default=False)
    gender=Column(String(50),nullable=True)

    @classmethod
    def get_male_students(cls,session):
        return session.query(cls).filter(cls.gender=='male').all()
    
    @validates('name')
    def validate_name(self,key,name):
        if len(name) <=4:
            raise ValueError("Name must be at least 4 characters")
        return name
    
    @validates('email')
    def validate_email(self,key,email):
        if len(email) <=4:
            raise ValueError("Name must be at least 4 characters")
        return email
    
    @validates('gender')
    def validate_gender(self,key,gender):
        genders=['male','female','other']

        if gender in genders:
            return gender
        else:
            raise ValueError('Gender is not valid')
        


# new_user=Student(name='hellow',email='hellow@gmail.com',phone=324332,is_married=True,
#                  gender='male'
#                  )

# session.add(new_user)
# session.commit()
        
# query=text('SELECT * FROM student')

# result=session.execute(query)

# for row in result:
#     print(row)

# session.close()
        
male_students=Student.get_male_students(session)

for student in male_students:
    print(student.name," ",student.email)

session.close()

# self ptyhon == this
# cls == Class itself