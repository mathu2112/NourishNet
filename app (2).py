import gradio as gr

def predict(meals, hours_left, distance):
    score = 0

    if hours_left < 4:
        score += 3
    elif hours_left < 8:
        score += 2
    else:
        score += 1

    if meals > 100:
        score += 3
    elif meals > 50:
        score += 2
    else:
        score += 1

    if distance < 5:
        score += 3
    elif distance < 15:
        score += 2
    else:
        score += 1

    if score >= 7:
        return "HIGH PRIORITY - Distribute immediately"
    elif score >= 5:
        return "MEDIUM PRIORITY - Schedule soon"
    else:
        return "LOW PRIORITY - Can wait"

iface = gr.Interface(
    fn=predict,
    inputs=["number", "number", "number"],
    outputs="text"
)

iface.launch()