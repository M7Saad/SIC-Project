import gradio as gr
from tensorflow.keras.models import load_model
from tensorflow_hub import KerasLayer as layer


# load model
model = load_model("Models/preTrainedModel.h5", custom_objects={"KerasLayer": layer})

# load labels
labels = ["Fire", "Neutral", "Smoke"]


def classify_image(inp):
    inp = inp.reshape((-1, 224, 224, 3))
    inp = inp / 255.0
    prediction = model.predict(inp).tolist()[0]
    return {labels[i]: float(prediction[i]) for i in range(3)}


gr.Interface(
    fn=classify_image,
    inputs=gr.Image(shape=(224, 224), image_mode="RGB"),
    outputs=gr.Label(num_top_classes=3),
).launch()
