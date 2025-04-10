# Turtle Art Generator

A creative Python program that uses the Turtle graphics module to generate various artistic patterns, including geometric shapes, random walks, spirographs, and a dot painting inspired by color extraction.
![dotsPainting](https://github.com/user-attachments/assets/22567bd1-f8eb-48a0-b1ba-b679ec6ce90e)

## 🎨 Overview

This project demonstrates the use of Python's Turtle graphics library to create different forms of generative art. The program sequentially draws multiple visual elements, showcasing different algorithmic approaches to creating digital art.

## ✨ Features

### 1. Geometric Pattern Generator
- Creates a sequence of regular polygons from triangles to decagons
- Each shape rendered in random RGB colors
- Consistent size with varying angles based on the number of sides

### 2. Random Walk
- Implements a randomized walking pattern with 90-degree turns
- Creates an unpredictable maze-like structure
- Uses bold lines with randomly generated colors

### 3. Spirograph
- Generates a spirograph pattern of overlapping circles
- Creates a complex, symmetrical design
- Uses thin lines with continuously changing colors

### 4. Dot Painting
- Produces a grid of colored dots inspired by pointillism
- Uses a color palette extracted from an image (commented code shows extraction process)
- Demonstrates algorithmic art creation with predefined colors

## 🛠️ Requirements

- Python 3.x
- turtle module (standard library)
- colorgram.py (for color extraction functionality)

## 📋 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/turtle-art-generator.git
cd turtle-art-generator
```

2. Install required packages:
```bash 
pip install colorgram.py
```

## 🚀 Usage

Run the program with:
```bash
python turtle_art.py
```

The program will:
1. Draw a series of geometric shapes
2. Create a random walk pattern
3. Generate a spirograph
4. Produce a dot painting

When all drawings are complete, click anywhere on the screen to exit.

## 🧩 Code Structure

The code is organized into distinct sections:

- **Setup**: Initializes the turtle and screen settings
- **Random Color Function**: Generates random RGB colors
- **Shape Drawing**: Creates a sequence of regular polygons
- **Random Walk**: Implements a randomized walking algorithm
- **Spirograph**: Creates a pattern of overlapping circles
- **Dot Painting**: Produces a grid of colored dots

## 💡 How It Works

### Random Color Generation
```python
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return turtle.pencolor(r,g,b)
```

### Drawing Regular Polygons
The program calculates the appropriate angles for each regular polygon:
```python
shape_degrees = 360 / shape
```

### Color Extraction (Commented)
The code includes a commented section showing how to extract colors from an image using colorgram.py:
```python
# colors = colorgram.extract("painting.jpg", 40)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r,g,b)
#     rgb_colors.append(color_tuple)
```

## 🔍 Customization

You can customize the art by modifying:
- Screen dimensions in the setup section
- Shape sizes and pen widths
- Number of iterations in the random walk and spirograph
- Dot size and spacing in the dot painting
- Color palette (either by using your own image or modifying the color list)

## 📝 Future Enhancements

- Add command-line arguments to select which patterns to generate
- Implement more turtle art algorithms
- Add option to save generated art as image files
- Create an interactive mode to adjust parameters in real-time
- Implement animation controls (pause/play)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
