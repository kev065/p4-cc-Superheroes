from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CheckConstraint

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    super_name = db.Column(db.String(50))
    powers = relationship('HeroPower', back_populates='hero')

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(120), nullable=False)
    heroes = relationship('HeroPower', back_populates='power')
    __table_args__ = (CheckConstraint(length(description) >= 20, name='description_length'),)

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.Enum('Strong', 'Weak', 'Average'), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    hero = relationship('Hero', back_populates='powers')
    power = relationship('Power', back_populates='heroes')
