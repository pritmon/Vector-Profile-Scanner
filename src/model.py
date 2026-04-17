import tensorflow as tf

def build_model(input_shape):
    """
    Builds a more robust Sequential model for text classification.
    Incorporates a hidden layer and dropout to prevent overfitting.
    """
    model = tf.keras.Sequential([
        tf.keras.Input(shape=(input_shape,)),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dropout(0.2), # Randomly disables 20% of neurons to ensure robustness
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer='adam', 
        loss='binary_crossentropy', 
        metrics=['accuracy']
    )
    return model

