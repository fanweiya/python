#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint, ForeignKey
from sqlalchemy.orm import sessionmaker
print(sqlalchemy.__version__)
engine = create_engine('mysql+pymysql://root:as@127.0.0.1:3306/tesql?charset=utf8', echo=True)  # echo=True输出生成的SQL语句
Base = declarative_base()  # 生成一个ORM基类
class UserInfo(Base):
    __tablename__ = 'UserInfo'  # 表名
    """
    创建字段
    index=True  普通索引
    unique=T  唯一索引
    """
    id = Column(Integer, primary_key=True, autoincrement=True)  # primary_key=主键,autoincrement=自增
    name = Column(String(32))
    password = Column(String(16))
    __table_args__ = (
        Index('id', 'name'),  # 联合索引
        UniqueConstraint('name', 'password', name='name_password')  # 联合唯一索引,name索引的名字
    )
    # 让查询出来的数据显示中文
    def __repr__(self):
        return self.name
# 把所有集成Base类的类，创建表结构
Base.metadata.create_all(engine)


#创建一对多表
class Favor(Base):
    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(50), default='red', unique=True)
class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    favor_id = Column(Integer, ForeignKey("favor.nid"))

# 创建多对多表

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)
# 服务器
class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
# 服务器组，第三张表
class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))

Base.metadata.drop_all(engine)  # 把所有集成Base类的类，删除表

MySesion = sessionmaker(bind=engine)
session = MySesion()
# 创建一条数据
users = UserInfo(name='Hello', password='World')
# 把数据添加到表内
session.add(users)
# 提交生效
session.commit()


session.add_all([
    UserInfo(name='A', password='1'),
    UserInfo(name='B', password='2')
])
# 提交
session.commit()


session.query(UserInfo).filter(UserInfo.name == 'a').delete()
session.commit()


result = session.query(UserInfo).all()
print(result)


session.query(UserInfo).filter(UserInfo.id == 8).update({"name": "ffff"})
session.commit()

result = session.query(UserInfo).filter_by(name='b').all()
# 返回的是一个列表

result = session.query(UserInfo).filter_by(name='b').first()
# 获取值中的某个属性
result.name

result = session.query(UserInfo).filter_by(name='b').count()

from sqlalchemy import and_, or_


for row in session.query(UserInfo).filter(and_(UserInfo.name == 'A', UserInfo.password == 1)):
    print(row)

for row in session.query(UserInfo).filter(or_(UserInfo.name == 'Hello', UserInfo.password == 1)):
    print(row)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationships
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql+pymysql://root:as@127.0.0.1:3306/tesql')
Base = declarative_base()
class Son(Base):
    __tablename__ = 'son'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    father = relationship('Father')
    # 创建外键
    father_id = Column(Integer, ForeignKey('father.id'))
class Father(Base):
    __tablename__ = 'father'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    son = relationship('Son')
    # son = relationship('Son', backref='Father') 相当于上面两个relationship
# 生成表
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# 添加父亲的数据
F = Father(name='as')
session.add(F)
session.commit()
# 添加儿子的数据
S1 = Son(name='Son1', father_id=1)
S2 = Son(name='Son2', father_id=1)
session.add_all([S1, S2])
session.commit()
# 另外一种添加数据的方式
F = session.query(Father).filter_by(id=1).first()
S3 = Son(name='Son3')
# 要用追加的方式进行添加，F.son是一个列表，如果不用append将会把之前的数据对应的值进行删除
F.son.append(S3)
session.add(F)
session.commit()

Session = sessionmaker(bind=engine)
session = Session()
# 添加父亲的数据
F = Father(name='as')
session.add(F)
session.commit()
# 添加儿子的数据
S1 = Son(name='Son1', father_id=1)
S2 = Son(name='Son2', father_id=1)
session.add_all([S1, S2])
session.commit()
# 另外一种添加数据的方式
F = session.query(Father).filter_by(id=1).first()
S3 = Son(name='Son3')
# 要用追加的方式进行添加，F.son是一个列表，如果不用append将会把之前的数据对应的值进行删除
F.son.append(S3)
session.add(F)
session.commit()


result = session.query(Father).filter_by(name='as').first()
for n in result.son:
    print(n.name)


result = session.query(Son).filter_by(name='Son2').first()
print(result.father.name, result.name)
# son = relationship('Son', backref='Father')
# print(result.father.name, result.name)

result = session.query(Father.name.label('kkk'), Son.name.label('ppp')).join(Son)
# label('kkk')相当于起了一个别名，等于sql中的as
print(result)

g = relationship("Group", secondary=ServerToGroup.__table__, backref='s')

G1 = Group(name='G1', port=22)
G2 = Group(name='G2', port=22)
S1 = Server(hostname='Linux-node1')
S2 = Server(hostname='Linux-node2')
session.add_all([G1, G2, S1, S2])
session.commit()


GS1 = ServerToGroup(server_id=1, group_id=1)
GS2 = ServerToGroup(server_id=2, group_id=2)
session.add_all([GS1, GS2])
session.commit()

# 获取ID=1的主机
S = session.query(Server).filter_by(id=1).first()
# 获取所有主机组
G = session.query(Group).all()
S.g = G
# 添加数据
session.add_all([S, ])
# 提交到数据库中
session.commit()
