# VITB NEXIS: News Aggregator & Recommendation System

<img width="1897" height="946" alt="image" src="https://github.com/user-attachments/assets/2adb09a1-480e-4724-a124-97434c6e2739" />


## 1. Introduction

In a fast-paced academic environment, keeping the college community informed and connected is essential. Traditional communication methods such as notice boards and emails can be inefficient, leading to missed updates. VITB Nexis is a news aggregator and recommendation system tailored for a college setting that solves this problem. It curates relevant news, events, and announcements into a single, accessible platform, aiming to foster a more connected and engaged academic community.

The motivation behind this project is to bridge the communication gap in academic institutions by delivering timely and targeted information in modern, interactive formats that students prefer.

---

## 2. Features

### User Features
* **Personalized News Delivery**: Recommends content based on user preferences and engagement history.
* **Centralized Platform**: Offers a single source for all college-related news, including academic events, campus activities, and administrative notices.
* **Engaging Visual Formats**: Presents news using modern formats like stories, reels, infographics, and videos.
* **User Profiles**: Allows users to create profiles, save their preferences (like favorite categories), and bookmark articles.
* **Interactive Elements**: Includes a search bar with filters, a comment section, social sharing options, and news polls.
* **Feedback System**: A contact page with a FormSpree-integrated form allows users to submit feedback and suggestions.

### Admin Features
* **Secure Admin Dashboard**: An intuitive dashboard for administrators to manage content.
* **Content Management**: Admins can easily upload, edit, and delete news articles.
* **Category Management**: Functionality to manage news categories.
* **Engagement Analytics**: Tools to track key metrics like most-read articles and popular categories.
* **Role-Based Access Control**: Secure access with distinct permissions for different admin roles.

---

## 3. Proposed Methodology

The system uses a content-based filtering approach to recommend news.
1.  **Data Collection**: Administrators manually upload news articles and their attributes (title, content, category) via the admin dashboard, which are then stored in CSV files.
2.  **Feature Extraction**: The textual data from news titles and descriptions is processed using TF-IDF (Term Frequency-Inverse Document Frequency) to extract and weigh key terms.
3.  **Similarity Calculation**: Cosine similarity is used to measure the relationship between articles and a user's selected categories.
4.  **Recommendation Engine**: Python scripts process the data to recommend articles that closely align with a user's preferences. The system's performance is evaluated using Precision, Recall, and F1-Score.

---

## 4. Technology Stack

The project is built using a lightweight and efficient technology stack.

* **Front-End**:
    * **HTML**: For structuring web page content.
    * **CSS & Bootstrap**: For responsive styling and layouts.
    * **JavaScript**: For interactivity and dynamic content.
* **Back-End**:
    * **Python**: Powers the recommendation engine and filtering logic.
    * **Flask**: Lightweight web framework for server-side operations.
* **Data Storage**:
    * **CSV Files**: Serve as the primary data storage for news articles.
* **Other Tools**:
    * **Scikit-learn**: Used for TF-IDF vectorization and cosine similarity calculations.
    * **Pandas**: For efficient data manipulation and analysis.
    * **FormSpree**: To integrate the user feedback form.
    * **Figma**: For UI/UX design and prototyping.
    * **GitHub**: For version control and project collaboration.

---

## 5. Expected Outcomes

* **Improved Communication**: A streamlined, centralized platform for all college news.
* **Enhanced User Engagement**: Increased interaction with content through personalization and engaging formats.
* **High Recommendation Accuracy**: The system targets an 80% accuracy rate, with initial tests showing 85%.
* **Efficient Content Management**: A simplified workflow for administrators to manage news.
* **Scalability**: A modular design that supports a growing user base and future features.
* **Continuous Improvement**: A feedback loop enables ongoing refinement of the recommendation model.
