# App Review Sentiment Analysis

## About the Project
Choosing an application from the Google Play Store or Apple App Store can be difficult due to the large number of user reviews. Reading and analyzing hundreds or thousands of reviews manually is time-consuming and often impractical. This project aims to simplify that process by automatically analyzing user reviews and providing an overall sentiment-based evaluation of an app.

The system performs **sentiment analysis** on user reviews collected from app stores and classifies the app’s overall feedback as **Positive**, **Negative**, or **Neutral**. This helps users quickly understand the general opinion about an app without reading individual reviews.

---

## Features
- Accepts an app name as user input
- Collects reviews from:
  - Google Play Store
  - Apple App Store
- Performs sentiment analysis using NLP techniques
- Displays overall sentiment result
- Web-based interface using HTML and CSS
- Flask-based backend implementation

---

## Tech Stack
**Backend**
- Python
- Flask
- TextBlob (Sentiment Analysis)
- BeautifulSoup (Web Scraping)
- Requests

**Frontend**
- HTML
- CSS

---

## Methodology
1. User enters the app name through the web interface  
2. Reviews are fetched from Google Play Store and Apple App Store  
3. Text data is pre-processed and analyzed using sentiment analysis  
4. Individual review sentiments are aggregated  
5. Final sentiment is classified as:
   - Positive
   - Negative
   - Neutral  
6. Results are displayed to the user in a readable format

## Use Cases
- Users deciding whether to download an app
- Students learning NLP and sentiment analysis
- Beginners exploring Flask-based web applications
- Academic and mini-project demonstrations

## Future Scope
- Improve sentiment accuracy using advanced machine learning or deep learning models
- Add graphical visualization of sentiment distribution
- Support more app stores and platforms
- Enable real-time review updates

## Contributors
- Soumyadiptya Dutta
- Muskan Behera
- Dwiparna Mandal
- Aditya Chakraborty

## License
This project is intended for **educational and academic use**.

