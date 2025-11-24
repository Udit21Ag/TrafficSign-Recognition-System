# Traffic Sign Recognition System

This project implements a Traffic Sign Recognition System using a Convolutional Neural Network (CNN) trained on the GTSRB (German Traffic Sign Recognition Benchmark) dataset.

**Downloading the Dataset**

Kaggle Link: `https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign`.
Rename the ZIP file to "German Dataset.zip" and place the ZIP file inside the project directory, at the same level as notebook.

**Setting up Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows
```
Then install packages:
```bash
pip install fastapi uvicorn numpy pillow tensorflow pandas matplotlib scikit-learn
```

**Running the Model**

Open the notebook: `FODS_Advanced_Model_CNN.ipynb` and run all the cells. It will extract the dataset, train the CNN model and save the best CNN model locally.

**Running the Backend**
```bash
cd backend
uvicorn app:app --reload
```

**Running the Web Interface**

The project includes a simple frontend interface for testing the trained model.

Steps:
1. Go to the frontend folder.
2. Right-click `index.html`.
3. Click **“Open with Live Server”** (VS Code extension: Live Server).
4. Upload a traffic sign image and test predictions.
