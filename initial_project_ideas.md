# Capstone 1 Project Ideas

**Ed Sandler**
*December 2023*

## US Economic Dashboard

**Summary:**
This dashboard would provide a current snapshot of the US Economy by displaying key Economic and Market Data. The dashboard would access data from multiple free APIs including:

- All major Stock Market Indices
- Key global interest Rate, Currency, and Commodity Data
- All Major cryptocurrencies
- All US Key Economic Indicators
- Real-Time Financial Headline News

Users would be able to input individual stock tickers to access realtime price data. In addition, users would have the ability to build a portfolio of securities to be tracked in real time. Historical price data would be stored in a Postgres database and displayed via various charts on the webpage.

## Automated Resume Writer and Job Application Tool

**Summary:**
This website would allow users to create a profile of relevant skills and experience, to be matched with job openings sourced by various job site aggregator APIs. The following data would be stored in a Postgres Database and be searchable for future reference:

- Job title
- Job Description
- Company name
- Contact information of the poster
- Date Applied

The site would leverage Chat GPT to create individual, customized, keyword-rich, SEO-optimized resume and cover letter for each job posting. The user could then apply to the position via API if allowed or via an email/messaging API such as Twilio.

## Nutrition Coaching Website

**Summary:**
This website would be designed for a nutrition coach to provide clients with resources and tools to assist with meal planning, exercise, and a successful mindset to achieve a client’s nutrition and fitness goals.

The sections of the website would include:

- Online scheduling tool to book a consultation with a nutrition coach
- A meal planner - meal ideas/recipes can be accessed via API based on personal preferences and recommended %Protein/Carb/fat and Daily recommended Calorie Count
- Recipes would be stored in a Postgres db and searchable for future meals
- Carefully curating a list of exercise videos sourced by Youtube API
- Daily inspirational quotes sourced by API
- Section of the webpage to record and store progress and to view progress relative to stated goals.


