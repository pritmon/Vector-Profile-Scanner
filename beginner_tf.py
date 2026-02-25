import tensorflow as tf

# 1. Dataset containing target (1) and non-target (0) skills
data = ["Python", "TensorFlow", "Vertex AI", "NLP", "BigQuery", 
        "Cooking", "Dancing", "Photoshop", "Excel", "Marketing"]
labels = tf.constant([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

# TextVectorization converts text to a multi-hot encoded tensor
vectorizer = tf.keras.layers.TextVectorization(output_mode='multi_hot')
vectorizer.adapt(data)
X = vectorizer(data)

# 2. Basic Sequential model with one Dense layer
model = tf.keras.Sequential([
    tf.keras.Input(shape=(X.shape[1],)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 3. Compile and train the model 
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X, labels, epochs=500, verbose=0)

# 4. Test on a Google skill and a non-relevant skill
tests = ["Vertex AI", "Carpentry"]
predictions = model.predict(vectorizer(tests), verbose=0)

for skill, p in zip(tests, predictions):
    print(f"'{skill}' -> {'Google Skill' if p[0]>0.5 else 'Non-relevant'} ({p[0]:.2f})")
