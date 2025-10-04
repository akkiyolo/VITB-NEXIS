# VITB NEXIS: News Aggregator & Recommendation System

<img width="1897" height="946" alt="image" src="https://github.com/user-attachments/assets/2686312c-0404-492e-8535-cd0b148b2db2" />


## 1. Introduction

[cite_start]In a fast-paced academic environment, keeping the college community informed and connected is essential[cite: 11]. [cite_start]Traditional communication methods such as notice boards and emails can be inefficient, leading to missed updates[cite: 13]. [cite_start]VITB Nexis is a news aggregator and recommendation system tailored for a college setting that solves this problem. [cite_start]It curates relevant news, events, and announcements into a single, accessible platform, aiming to foster a more connected and engaged academic community[cite: 15, 17].

[cite_start]The motivation behind this project is to bridge the communication gap in academic institutions by delivering timely and targeted information in modern, interactive formats that students prefer[cite: 18, 22].

## 2. Features

### User Features
* [cite_start]**Personalized News Delivery**: Recommends content based on user preferences and engagement history[cite: 24].
* [cite_start]**Centralized Platform**: Offers a single source for all college-related news, including academic events, campus activities, and administrative notices[cite: 25, 27].
* [cite_start]**Engaging Visual Formats**: Presents news using modern formats like stories, reels, infographics, and videos[cite: 26, 96].
* [cite_start]**User Profiles**: Allows users to create profiles, save their preferences (like favorite categories), and bookmark articles[cite: 109].
* [cite_start]**Interactive Elements**: Includes a search bar with filters, a comment section, social sharing options, and news polls[cite: 91, 112, 113, 114].
* [cite_start]**Feedback System**: A contact page with a FormSpree-integrated form allows users to submit feedback and suggestions[cite: 50, 99].

### Admin Features
* [cite_start]**Secure Admin Dashboard**: An intuitive dashboard for administrators to manage content[cite: 16, 51].
* [cite_start]**Content Management**: Admins can easily upload, edit, and delete news articles[cite: 105, 106].
* [cite_start]**Category Management**: Functionality to manage news categories[cite: 107].
* [cite_start]**Engagement Analytics**: Tools to track key metrics like most-read articles and popular categories[cite: 107].
* [cite_start]**Role-Based Access Control**: Secure access with distinct permissions for different admin roles[cite: 115].

## 3. Proposed Methodology

The system uses a content-based filtering approach to recommend news.
1.  [cite_start]**Data Collection**: Administrators manually upload news articles and their attributes (title, content, category) via the admin dashboard, which are then stored in CSV files[cite: 33].
2.  [cite_start]**Feature Extraction**: The textual data from news titles and descriptions is processed using TF-IDF (Term Frequency-Inverse Document Frequency) to extract and weigh key terms[cite: 35, 36].
3.  [cite_start]**Similarity Calculation**: Cosine similarity is used to measure the relationship between articles and a user's selected categories[cite: 44].
4.  [cite_start]**Recommendation Engine**: Python scripts process the data to recommend articles that closely align with a user's preferences[cite: 47]. [cite_start]The system's performance is evaluated using Precision, Recall, and F1-Score[cite: 48].

## 4. Technology Stack

[cite_start]The project is built using a lightweight and efficient technology stack[cite: 54].

* **Front-End**:
    * [cite_start]**HTML**: For structuring web page content[cite: 57].
    * [cite_start]**CSS & Bootstrap**: For responsive styling and layouts[cite: 58].
    * [cite_start]**JavaScript**: For interactivity and dynamic content[cite: 59].
* **Back-End**:
    * [cite_start]**Python**: Powers the recommendation engine and filtering logic[cite: 61].
    * [cite_start]**Flask**: Lightweight web framework for server-side operations[cite: 62].
* **Data Storage**:
    * [cite_start]**CSV Files**: Serve as the primary data storage for news articles[cite: 65].
* **Other Tools**:
    * [cite_start]**Scikit-learn**: Used for TF-IDF vectorization and cosine similarity calculations[cite: 68].
    * [cite_start]**Pandas**: For efficient data manipulation and analysis[cite: 69].
    * [cite_start]**FormSpree**: To integrate the user feedback form[cite: 67].
    * [cite_start]**Figma**: For UI/UX design and prototyping[cite: 70].
    * [cite_start]**GitHub**: For version control and project collaboration[cite: 71].

## 5. Expected Outcomes

* [cite_start]**Improved Communication**: A streamlined, centralized platform for all college news[cite: 75].
* [cite_start]**Enhanced User Engagement**: Increased interaction with content through personalization and engaging formats[cite: 76].
* [cite_start]**High Recommendation Accuracy**: The system targets an 80% accuracy rate, with initial tests showing 85%[cite: 77].
* [cite_start]**Efficient Content Management**: A simplified workflow for administrators to manage news[cite: 78].
* [cite_start]**Scalability**: A modular design that supports a growing user base and future features[cite: 79].
* [cite_start]**Continuous Improvement**: A feedback loop enables ongoing refinement of the recommendation model[cite: 80, 82].

