# Nikud

This project contains an LSTM Language-Model trained to predict what "nikud" should be assigned to Arabic Text that is written in Hebrew letters, and a web server with UI to use the model. 

**Example:**

for the input
   ```
   צבאח אלח'יר
   ```
   the expected output is
   ```
   צַבַּאח אִלְחֵ׳יר
   ```
   


## To run the Flask Server: 
1. cd into the 'web/' folder.
2. Run the following commands:
```
   set FLASK_APP=myApp.py
   flask run
  ```

## To create an Anaconda environment:
1. Clone the repository:
    ```
    git clone https://github.com/LihiHadjb/nikud.git
    ```
2. Create the environment by running:
    ```
    conda env create -f environment.yml
    ```
    The resulting environment name is "**nikud_env**"
     
     
## To create an environment using pip:
1. Clone the repository:
    ```
    git clone https://github.com/LihiHadjb/nikud.git
    ```
2. Create the environment by running:
    ```
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```