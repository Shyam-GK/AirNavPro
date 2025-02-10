# AirNavPro

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Kivy](https://img.shields.io/badge/Kivy-2.1.0-green) ![MIT License](https://img.shields.io/badge/License-MIT-yellow)


**AirNavPro** is a cutting-edge navigation system designed to optimize flight paths for airplanes. It leverages the **A\* pathfinding algorithm** to calculate the most efficient routes while dynamically integrating real-time weather data using APIs. The system also supports **manual obstacle placement** in airways, enabling users to simulate and analyze flight paths under various conditions. AirNavPro provides a user-friendly interface for real-time navigation modeling, making it an essential tool for flight planning and optimization.

---
## Features
### A* Pathfinding Algorithm
- Calculates the shortest and most efficient flight paths.
- Supports dynamic recalculation based on changing conditions.

### Dynamic Weather Integration
- Fetches real-time weather data using APIs.
- Adjusts flight paths to avoid adverse weather conditions.

### Manual Obstacle Placement
- Allows users to manually place obstacles in airways for simulation and testing.
- Simulates real-world scenarios such as no-fly zones or restricted airspace.

### Real-Time Navigation Modeling
- Visualizes flight paths and weather conditions in real-time.
- Provides performance metrics such as path length and search efficiency.

### Interactive Interface
- Built with Kivy for a seamless user experience.
- Intuitive controls for placing start, end, and obstacle nodes.
---
## Installation
### Prerequisites
- Python 3.8 or later.
- Kivy 2.1.0 or later.
- OpenWeatherMap API key (sign up [here](https://openweathermap.org/)).

### Clone the Repository
```bash
git clone https://github.com/Shyam-GK/airnavpro.git
cd airnavpro
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up API Key
Replace the `api_key` variable in the `Grid` class with your OpenWeatherMap API key or any other API key.

### Run the Application
```bash
python main.py
```
---
## Usage
### Grid Interaction
- **Left-click** to place the start node (green).
- **Left-click** again to place the end node (red).
- **Left-click** to place obstacle nodes (black).
- **Weather-based barriers** (orange) are automatically placed during adverse conditions.

### Manual Obstacle Placement
- Use the grid interface to manually place obstacles in airways.
- Simulate restricted airspace or no-fly zones.

### Algorithm Controls
- **Press Spacebar** to start the A* algorithm.
- **Press Enter** to reset the grid.

### Weather Integration
- The application fetches weather data for a specified city (e.g., "New York") and adjusts flight paths dynamically.

### Performance Metrics
- After the algorithm completes, the path length and search length are displayed in the console.


---
## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---
## Acknowledgments
- Built with Kivy and Python.
- Weather data provided by OpenWeatherMap.
- Inspired by pathfinding algorithms and interactive visualizations.
---
## Contact
For questions or feedback, please contact:

- **Shyam GK**  
- **Email:** shyamgokulkrish@gmail.com  
- **GitHub:** [Shyam GK](https://github.com/Shyam-GK)

Enjoy using **AirNavPro**!
