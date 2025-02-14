##  Newborn-Care-bot  

A chatbot designed to support new mothers by providing expert guidance on newborn care, including feeding, sleep, vaccinations, baby behavior, and health.  

##  Getting Started  

Follow these steps to set up and run the project locally.  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/mennaafi/Infant-Care-AI.git
cd Infant-Care-AI/mini-rag
```
### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv venv
```
### **Activate the Virtual Environment:**  

#### **Windows:**  
```bash
venv\Scripts\activate
```
#### **Mac/Linux:**  
```bash
source venv/bin/activate
```
### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables  
Create a `.env` file inside `mini-rag/` and add the following (similar to .env.example)

### 5️⃣ Run the Application  

Run the following command to start the FastAPI server:  

```bash
uvicorn src.main:app --reload