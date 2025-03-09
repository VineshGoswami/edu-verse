import pymongo
from datetime import datetime

try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["course_db"]

    collections = {
        "users": db["users"],
        "tutors": db["tutors"],
        "playlist": db["playlist"],
        "content": db["content"],
        "comments": db["comments"],
        "likes": db["likes"],
        "bookmark": db["bookmark"],
        "contact": db["contact"],
        "userdata": db["users_data"],
        "chatbot": db["chats"]
    }

    users_data = {
        "id": "1",
        "name": "Alice",
        "email": "alice@example.com",
        "password": "hashed_password",
        "image": "profile.jpg"
    }
    collections["users"].insert_one(users_data)

    # Tutors Collection
    tutors_data = {
        "id": "tutor_1",
        "name": "John Tutor",
        "profession": "Math Teacher",
        "email": "john@example.com",
        "password": "hashed_password",
        "image": "tutor_profile.jpg"
    }
    collections["tutors"].insert_one(tutors_data)

    # Playlist Collection
    playlist_data = {
        "id": "playlist_1",
        "tutor_id": "tutor_1",
        "title": "Math 101",
        "description": "Basic math concepts",
        "thumb": "playlist_thumb.jpg",
        "date": datetime.now(),
        "status": "active"
    }
    collections["playlist"].insert_one(playlist_data)

    # Content Collection
    content_data = {
        "id": "content_1",
        "tutor_id": "tutor_1",
        "playlist_id": "playlist_1",
        "title": "Algebra Basics",
        "description": "Introduction to Algebra",
        "video": "algebra_basics.mp4",
        "thumb": "algebra_thumb.jpg",
        "date": datetime.now(),
        "status": "active"
    }
    collections["content"].insert_one(content_data)

    # Comments Collection
    comments_data = {
        "id": "comment_1",
        "content_id": "content_1",
        "user_id": "1",
        "tutor_id": "tutor_1",
        "comment": "Great introduction to algebra!",
        "date": datetime.now()
    }
    collections["comments"].insert_one(comments_data)

    # Likes Collection
    likes_data = {
        "user_id": "1",
        "tutor_id": "tutor_1",
        "content_id": "content_1"
    }
    collections["likes"].insert_one(likes_data)

    # Bookmark Collection
    bookmark_data = {
        "user_id": "1",
        "playlist_id": "playlist_1"
    }
    collections["bookmark"].insert_one(bookmark_data)

    # Contact Collection
    contact_data = {
        "name": "Alice",
        "email": "alice@example.com",
        "number": 1234567890,
        "message": "I would like more information about the courses."
    }
    collections["contact"].insert_one(contact_data)

    users_data_entry = {
        "user_id": "1",
        "preferences": ["math", "science"],
        "progress": {"math": 80, "science": 70}
    }
    collections["userdata"].insert_one(users_data_entry)

    chatbot_entry = {
        "user_id": "1",
        "message": "Hello, how can I help you?",
        "response": "You can ask me anything about the course.",
        "timestamp": datetime.now()
    }
    collections["chatbot"].insert_one(chatbot_entry)

    print(" Database and collections created successfully!")

except Exception as e:
    print(f" Error connecting to MongoDB: {e}")
