import gradio as gr

def calc_vo2(run_time, age, weight, height, gender):
    if gender == "Male":
        gender_multiplier = 1
    else:
        gender_multiplier = 0
    bmi = 703*(weight/(height**2))
    time_sec = run_time/60
    vo2 = (0.21 * age * gender_multiplier) - 0.84*(bmi) - 8.41*(time_sec) + 0.34*(time_sec**2) + 108.94
    return vo2

age1= gr.Number(label= "Age")
weight1 = gr.Number(label = "Weight in Pounds")
height1 = gr.Number(label = "Height in Inches")
run_time1 = gr.Number(label = "Time spent running mile in seconds")
gender1 = gr.CheckboxGroup(["Male", "Female"], label="Gender")

demo= gr.Interface(calc_vo2, [run_time1, age1, weight1, height1, gender1], ["number"])
demo.launch()