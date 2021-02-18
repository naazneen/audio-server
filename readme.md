# Flask Audio-Server API

## Introduction
This is an api to simulates the behavior of an audio file server while using a MongoDB database.

## To run the app:

#### Pre-requisite:
To install requirements for this project, go to cmd and run:
```console
pip install -r requirements.txt
```


Go to root directory from cmd and type
```console
python app.py
```

**POSTMAN** example:  
  
POST : http://127.0.0.1:5000/  
Body:    
{   
    "audioFileType":"song",   
    "audioFileMetadata":{   
        "name":"mysong",   
        "duration":"4",  
        "uploaded_time": "2021-02-19 11:11"   
    }    
}   

  
Expected Output:    
Body:  
{"id":1}  
  
## To test the app
Go to root directory from cmd and type
```console
python test.app.py  
```

## Thank you for the test.
