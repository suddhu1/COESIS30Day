from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# intro.py

# Introduction to Machine Learning and Artificial Intelligence

# Machine Learning (ML) is a subset of artificial intelligence (AI) that focuses on the development of algorithms 
# and statistical models that enable computers to perform tasks without explicit instructions. 
# Instead, ML systems learn from data and improve their performance over time.

# Artificial Intelligence (AI) is a broader concept that encompasses the simulation of human intelligence in machines. 
# AI systems are designed to perform tasks that typically require human intelligence, such as visual perception, 
# speech recognition, decision-making, and language translation.

# Key Concepts in Machine Learning:
# 1. Supervised Learning: The model is trained on labeled data, where the input-output pairs are provided.
# 2. Unsupervised Learning: The model is trained on unlabeled data and must find patterns and relationships in the data.
# 3. Reinforcement Learning: The model learns by interacting with an environment and receiving feedback in the form of rewards or penalties.

# Key Concepts in Artificial Intelligence:
# 1. Natural Language Processing (NLP): The ability of machines to understand and generate human language.
# 2. Computer Vision: The ability of machines to interpret and understand visual information from the world.
# 3. Robotics: The design and creation of robots that can perform tasks autonomously or semi-autonomously.

# Example of a simple ML model using scikit-learn:

# Load the iris dataset
data = load_iris()
X = data.data
y = data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

