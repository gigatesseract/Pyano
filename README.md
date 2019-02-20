# Pyano
A light weight tool that transofrms your computer keyboard to a musical keyboard


### Run    
1. `git clone https://github.com/gigatesseract/Pyano.git`    
2. `cd Pyano`    
3. `virtualenv env` (Create a virtual environment, and install dependencies there.)    
4. `source env/bin/activate`(Activate the virtual environment)    
5. `pip install -r requirements.txt` (Install dependencies)    
6. `python3 driver.py` (Launch driver.py program)    
    

* Initial key_bindings: z - Middle C (C4), x - D4 etc ...... m - B4, , - C5. 

#### Key Bindings
1. In `driver.py` add a note that you want to introduce and its corresponsing frequence as a key value pair inside notes dict    
2. In the key_bindings dict, the key should be a button you press on the keyboard and its value should be the key in notes dict, whose frequenc you need. For example, if you want the letter 'w' to sound the note 'A4', do the following steps:    
    * In notes dict, add the following key value pair: `"A":440.00` (440.00 is the frequency of A4)    
    * In key_bindings dict, add the following key value pair: `"w":"A"`
