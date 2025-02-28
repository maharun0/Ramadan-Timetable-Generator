from PIL import Image, ImageDraw, ImageFont
import pandas as pd

template_path = "./input/template.png"
csv_path = "./input/ramadan_timetable.csv"

# Font Path
font_path_bold = "./input/fonts/tt_interphases_pro/TT Interphases Pro Trial Bold.ttf"
font_path_regular = "./input/fonts/tt_interphases_pro/TT Interphases Pro Trial Regular.ttf"

def generate():
    # Load the template image
    image = Image.open(template_path)

    # Load the CSV data
    df = pd.read_csv(csv_path)

    # Define font sizes
    font_bold = ImageFont.truetype(font_path_bold, 28)
    font_regular = ImageFont.truetype(font_path_regular, 26)

    # Define text positions
    start_x = 100  # Starting X position
    start_y = 508  # Starting Y position
    row_height = 49  # Space between rows

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Iterate over the data and add it to the image
    for index, row in df.iterrows():
        y_position = start_y + (index * row_height)
        
        draw.text((start_x + 10, y_position), str(row["No"]), font=font_bold, fill="black")
        draw.text((start_x + 130, y_position), row["Date"], font=font_regular, fill="black")
        draw.text((start_x + 325, y_position), row["Day"], font=font_regular, fill="black")
        draw.text((start_x + 550, y_position), row["Sahri_End"], font=font_bold, fill="black")
        draw.text((start_x + 815, y_position), row["Fajr_Start"], font=font_regular, fill="black")
        draw.text((start_x + 1070, y_position), row["Iftar_Time"], font=font_regular, fill="black")

    # Save the modified image
    output_path = "./output/ramadan_schedule_filled.png"
    image.save(output_path)

    print(f"Image saved as {output_path}")

generate()