#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import joblib
app = Flask(__name__) #dunder name

#The @ is for funning a generator
@app.route("/", methods=["GET","POST"])
def index():
    if request.method=='POST':
        #Get things from the front end
        num = float(request.form.get("rate")) #make this float. Double confirm
        print(num)
        
        model = joblib.load("python_lm")
        pred = model.predict([[num]])
        pred_float = round(pred[0][0],2)
        print(pred)
        
        s = str(pred_float)
        return(render_template('index.html', result = s))

    #What to do before pressing the button?
    else:
        return render_template('index.html', result = '...')


# In[ ]:


#Need this in the cloud because Heroku need to verify this is your program
if __name__=='__main__':
    app.run()
    
#I can calso change the host number
# app.run(host="127.0.0.1", port=int("80"))

