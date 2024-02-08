import yahooquery as yq
import unittest
from unittest import TestCase
from fredapi import Fred
import requests
import openai
from openai import OpenAI
from urllib.parse import quote
from flask_cors import CORS
from flask import Flask, request, render_template, jsonify,redirect,flash, session
from secret import OPENAI_API_KEY,FRED_API_KEY,WEATHER_API_KEY
from models import db, User,Watchlist # Import the models
from forms import RegisterForm,LoginForm # Import the form

from app import app, db

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///test_dashboard"  # Using in-memory SQLite database for testing
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        # Test user registration
        response = self.app.post('/register', data=dict(username="user", password="userpwd"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Economic', response.data)

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Economic', response.data)

    def test_login(self):
        # Assuming a user is already registered
        response = self.app.post('/login', data=dict(username="esandler", password='eddieboy'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

    def test_get_quote(self):
        with app.test_client() as client:

            response = client.get('/quote/AAPL')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Apple', response.data)

    def test_get_market_summary(self):
        with app.test_client() as client:
            response= client.get('/market_summary')


            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Bitcoin', response.data)
            self.assertIn(b'NASDAQ', response.data)
            self.assertIn(b'Gold', response.data)




    def test_show_economic_data(self):
        with app.test_client() as client:
            response= client.get('/economic_data')


            self.assertEqual(response.status_code, 200)
            self.assertIn(b'GDP', response.data)
            self.assertIn(b'FED FUNDS', response.data)
            self.assertIn(b'GNP', response.data)

    def test_get_eco_calendar_and_link(self):
        with app.test_client() as client:
            response= client.get('/calendar')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'https://', response.data)
            self.assertIn(b'Release', response.data)

    def test_get_news(self):
        with app.test_client() as client:
            response= client.get('/us_news')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'https://', response.data)

    def test_get_horoscope(self):
        with app.test_client() as client:
            response= client.get('/horoscope/Gemini')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Gemini', response.data)

    def test_joker(self):
        with app.test_client() as client:
            response= client.get('/joke')
            self.assertEqual(response.status_code, 200)

    def test_get_weather(self):
        with app.test_client() as client:
            response= client.get('/weather/Brooklyn')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Kings County', response.data)

