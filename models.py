from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base   # <-- use the Base from dbp.py


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(String(50))
    full_name = Column(String(100))
    age = Column(Integer)


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    age = Column(Integer)
    gender = Column(String(10))


class HealthRecord(Base):
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True, index=True)
    heart_rate = Column(Integer)
    spo2 = Column(Integer)
    glucose = Column(Integer, nullable=True)
    temperature = Column(Float, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    patient_id = Column(Integer, ForeignKey("patients.id"))


class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    heart_rate = Column(Float)
    spo2 = Column(Float)
    ir = Column(Integer)
    red = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
