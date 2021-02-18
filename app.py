
from flask import Flask, jsonify, request, Response
from database.db import initialize_db
from database.models import Song, Podcast, AudioBook
from flask_api import status
from flask.views import MethodView
from database.serializers import SongSerializer, PodcastSerializer, AudioBookSerializer
from marshmallow.exceptions import ValidationError
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/audio-db'
}

initialize_db(app)

@app.route('/')
def hello():
    return {'hello': 'world'}



class AudioAPI(MethodView):

    def validate_this(self, data):
        if not data.get('audioFileType') and not data.get('audioFileMetadata'):
            return (False, {'error':'audioFileType and audioFileMetadata Not provided'})

        if not data.get('audioFileType'):
            return (False, {'error':'audioFileType Not provided'})

        if not data.get('audioFileMetadata'):
            return (False, {'error':'audioFileMetadata Not provided'})
        
        return (True,{})

    def post(self):
        try:
            data = request.json
            validated = self.validate_this(data)
            if not validated[0]:
                return (validated[1], status.HTTP_400_BAD_REQUEST)
            audio_type = data['audioFileType'].lower()
            audio_data = data['audioFileMetadata']

            if audio_type == 'song':
                try:
                    s = SongSerializer().load(audio_data)
                    audio = Song(**s).save()
                    id = audio.id
                    return ({'id': id}, status.HTTP_200_OK)

                except ValidationError as e:
                    context = dict(e.messages)
                    return (context, status.HTTP_400_BAD_REQUEST)

                except Exception as e:
                    context = {'error':str(e)}
                    return (context, status.HTTP_400_BAD_REQUEST)

            elif audio_type == 'podcast':
                try:
                    p = PodcastSerializer().load(audio_data)
                    audio = Podcast(**p).save()
                    id = audio.id
                    return ({'id': id}, status.HTTP_200_OK)

                
                except ValidationError as e:
                    context = dict(e.messages)
                    return (context, status.HTTP_400_BAD_REQUEST)

                except Exception as e:
                    context = {'error':str(e)}
                    return (context, status.HTTP_400_BAD_REQUEST)

            elif audio_type == 'audiobook':
                try:
                    a = AudioBookSerializer().load(audio_data)
                    audio = AudioBook(**a).save()
                    id = audio.id
                    return ({'id': id}, status.HTTP_200_OK)

                except ValidationError as e:
                    context = dict(e.messages)
                    return (context, status.HTTP_400_BAD_REQUEST) 

                except Exception as e:
                    context = {'error':str(e)}
                    return (context, status.HTTP_400_BAD_REQUEST)      
                
            else:
                context = {"error":"Invalid Audio type"}
                return (context, status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            context = {'error':str(e)}
            return (context, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, audioFileType, id=None):

        try:
            if audioFileType == 'song':
                if id:
                    audios = Song.objects(id=id).to_json()
                else:
                    audios = Song.objects().to_json()
            
            elif audioFileType == 'podcast':
                if id:
                    audios = Podcast.objects(id=id).to_json()
                else:
                    audios = Podcast.objects().to_json()
            
            elif audioFileType == 'audiobook':
                if id:
                    audios = AudioBook.objects(id=id).to_json()
                else:
                    audios = AudioBook.objects().to_json()  
        
            else:
                context = {"error":"Invalid Audio type"}
                return (context, status.HTTP_400_BAD_REQUEST)
            
            if audios == '[]':
                context = {'error':'Audio matching ID does not exist'}
                return (context, status.HTTP_400_BAD_REQUEST)
            
            return Response(audios, mimetype="application/json", status=status.HTTP_200_OK)

        except Exception as e:
            context = {'error':str(e)}
            return (context, status.HTTP_500_INTERNAL_SERVER_ERROR)

        


    def delete(self, audioFileType, id):
        try:
            if audioFileType == 'song':
                try:
                    Song.objects.get(id=id).delete()
                    return ({'message': 'Successfully Deleted'}, status.HTTP_200_OK)

                except Exception as e:
                    context = {'error':str(e)}
                    return (context, status.HTTP_400_BAD_REQUEST)

            elif audioFileType == 'podcast':
                try:
                    Podcast.objects.get(id=id).delete()
                    return ({'message': 'Successfully Deleted'}, status.HTTP_200_OK)

                except Exception as e:
                    context = {'error':str(e)}
                    return (context, status.HTTP_400_BAD_REQUEST)

            elif audioFileType == 'audiobook':
                try:
                    AudioBook.objects.get(id=id).delete()
                    return ({'message': 'Successfully Deleted'}, status.HTTP_200_OK)

                except Exception as e:
                    context = {'error':str(e)}
                    return (context, status.HTTP_400_BAD_REQUEST)      
                
            else:
                context = {"error":"Invalid Audio type"}
                return (context, status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            context = {'error':str(e)}
            return (context, status.HTTP_500_INTERNAL_SERVER_ERROR) 
    

    def put(self, audioFileType, id):
        body = request.get_json()
        try:
            if audioFileType == 'song':
                try:
                    s = SongSerializer().load(body)
                    Song.objects.get(id=id).update(**s)
                    return ({'message': 'Successfully Updated'}, status.HTTP_200_OK)

                except ValidationError as e:
                    context = dict(e.messages)
                    return (context, status.HTTP_400_BAD_REQUEST)

                except Exception as e:
                    context = {'error':str(e)}
                    return (context, status.HTTP_400_BAD_REQUEST)

            elif audioFileType == 'podcast':
                try:
                    p = PodcastSerializer().load(body)
                    Podcast.objects.get(id=id).update(**p)
                    return ({'message': 'Successfully Updated'}, status.HTTP_200_OK)

                
                except ValidationError as e:
                    context = dict(e.messages)
                    return (context, status.HTTP_400_BAD_REQUEST)

                except Exception as e:
                    context = {'error':str(e)}
                    return (context, status.HTTP_400_BAD_REQUEST)

            elif audioFileType == 'audiobook':
                try:
                    a = AudioBookSerializer().load(body)
                    AudioBook.objects.get(id=id).update(**a)
                    return ({'message': 'Successfully Updated'}, status.HTTP_200_OK)

                except ValidationError as e:
                    context = dict(e.messages)
                    return (context, status.HTTP_400_BAD_REQUEST) 

                except Exception as e:
                    context = {'error':str(e)}
                    return (context, status.HTTP_400_BAD_REQUEST)      
                
            else:
                context = {"error":"Invalid Audio type"}
                return (context, status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            context = {'error':str(e)}
            return (context, status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
# handle 404
@app.errorhandler(404)
def page_not_found(e):
    return ("<h1>404</h1><p>The resource could not be found.</p>", status.HTTP_404_NOT_FOUND) 


app.add_url_rule('/audio/','createaudio', AudioAPI.as_view('api'), methods=['POST'])
app.add_url_rule('/audio/<audioFileType>/','readaudio',AudioAPI.as_view('api'), methods=['GET'])
app.add_url_rule('/audio/<audioFileType>/<id>/','readaudioid',AudioAPI.as_view('api'), methods=['GET'])
app.add_url_rule('/updateaudio/<audioFileType>/<id>/','updateaudio',AudioAPI.as_view('api'), methods=['PUT'])
app.add_url_rule('/deleteaudio/<audioFileType>/<id>/','deleteaudio',AudioAPI.as_view('api'), methods=['DELETE'])


# launch if run, not when imported. 
if __name__ == "__main__":
    app.run()

