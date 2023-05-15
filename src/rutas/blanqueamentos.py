from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
# from model.paciente import pacientes


routes_blanqueamentos = Blueprint("routes_blanqueamentos", __name__)

