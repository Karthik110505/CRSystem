# CRSystem

## Workflows

1. Update `config.yaml`.
2. Update `schema.yaml`.
3. Update the entity.
4. Update the configuration manager in `src/config`.
5. Update the components.
6. Update the pipeline.
7. Update `main.py`.
8. Update `crsystem.py`.

## Overview

The CRSystem is an end-to-end project that includes the development of a web application, implementation of Dockerization, CI/CD pipeline setup, and deployment to Render. The application assists users in finding suitable educational programs based on their preferences and requirements. It leverages machine learning algorithms to analyze various factors such as tuition cost, program duration, GRE requirements, institution type, and city preference to generate personalized recommendations.

## Features

- **Personalized Recommendations:** Users can input their preferences regarding program mode (online or offline), total tuition cost, program duration, GRE requirements, institution type, and city preference to receive customized recommendations.
- **User-friendly Interface:** The web application features a user-friendly interface with easy-to-use input fields and intuitive navigation.
- **Integration with External Platforms:** Users can easily connect with the developer via GitHub and LinkedIn through integrated icons provided in the footer section of the application.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask framework
- **Machine Learning:** Scikit-learn library for building recommendation models
- **Deployment:** Docker for containerization, GitHub Actions for continuous integration and deployment, Render for hosting the application

## Usage

1. Clone the repository to your local machine.
2. Create a new Python environment using `conda create --name crsystem python=3.8`.
3. Activate the newly created environment using `conda activate crsystem`.
4. Navigate to the project directory and install the required dependencies using `pip install -r requirements.txt`.
5. Set up the MLProject packages using `python setup.py install`.
6. You are now ready to run `crsystem.py`, which is the main application file.

## Author

Karthik@1155 - [GitHub](https://github.com/Karthik110505) | [LinkedIn](https://www.linkedin.com/in/barrenkala-veera-venkata-karthik-b58b9a285) | [Link for 
hosted website](https://crsystem.onrender.com)
