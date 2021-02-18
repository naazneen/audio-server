import unittest
from app import app
import json
from database.models import Song


class MyTestCase(unittest.TestCase):
    tester = app.test_client()
    create_url = '/audio/'
    read_url = '/audio/song'


    def test_audioFileType_required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileMetadata":{
                "name":"mysong",
                "duration": "4",
                "uploaded_time": "2021-02-19 11:11" }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data,b'{"error":"audioFileType Not provided"}\n')


    def test_audioFileMetadata_required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"song",
                "audioFiledata":{
                "name":"mysong",
                "duration": "4",
                "uploaded_time": "2021-02-19 11:11" }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"error":"audioFileMetadata Not provided"}\n')


    def test_SongName_required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"song",
                "audioFileMetadata":{
                "duration": "4",
                "uploaded_time": "2021-02-19 11:11" }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data,b'{"name":["Missing data for required field."]}\n')
        

    def test_SongName_len100(self):
        headers = {'Content-type': 'application/json'}
        str_name = "N"*200
        test_data = json.dumps({
                "audioFileType":"song",
                "audioFileMetadata":{
                "name":str_name,
                "duration":"4",
                "uploaded_time": "2021-02-19 11:11" }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"name":["Length must be between 1 and 100."]}\n')


    def test_SongDuration_required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"song",
                "audioFileMetadata":{
                "name":"mysong",
                "uploaded_time": "2021-02-19 11:11" }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data,b'{"duration":["Missing data for required field."]}\n')

    def test_SongDuration_positive(self):
        headers = {'Content-type': 'application/json'}
        str_name = "N"*200
        test_data = json.dumps({
                "audioFileType":"song",
                "audioFileMetadata":{
                "name":"mysong",
                "duration":"-4",
                "uploaded_time": "2021-02-19 11:11" }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"duration":["Value must be greater than 0"]}\n')

    def test_SongDuration_integer(self):
        headers = {'Content-type': 'application/json'}
        str_name = "N"*200
        test_data = json.dumps({
                "audioFileType":"song",
                "audioFileMetadata":{
                "name":"mysong",
                "duration":"D",
                "uploaded_time": "2021-02-19 11:11" }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"duration":["Not a valid integer."]}\n')
    

    def test_SongUplaodTime_required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"song",
                "audioFileMetadata":{
                "name":"mysong",
                "duration":"4"
                }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data,b'{"uploaded_time":["Missing data for required field."]}\n')


    def test_SongUplaodTime_notpast(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"song",
                "audioFileMetadata":{
                "name":"mysong",
                "duration":"4",
                "uploaded_time": "2021-01-19 11:11"
                }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"uploaded_time":["Invalid value."]}\n')


    def test_PodcastHost_Required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"podcast",
                "audioFileMetadata":{
                "name":"mysong",
                "duration":"4",
                "uploaded_time": "2021-02-19 11:11"
                }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"host":["Missing data for required field."]}\n')


    def test_PodcastHost_Required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"podcast",
                "audioFileMetadata":{
                "name":"mysong",
                "duration":"4",
                "uploaded_time": "2021-02-19 11:11"
                }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"host":["Missing data for required field."]}\n')


    def test_Podcastparticipants_Length(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"podcast",
                "audioFileMetadata":{
                "name":"mysong",
                "duration":"4",
                "uploaded_time": "2021-02-19 11:11",
                "host":"naazneen",
                "participants":['a','a','a','a','a','a','a','a','a','a','a']
                }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)

    def test_AudiobookAuthor_required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"audiobook",
                "audioFileMetadata":{
                "title":"mysong",
                "duration":"4",
                "uploaded_time": "2021-02-19 11:11",
                "narrator":"naaz"
                }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"author":["Missing data for required field."]}\n')
        

    def test_AudiobookNarrator_required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"audiobook",
                "audioFileMetadata":{
                "title":"mysong",
                "duration":"4",
                "uploaded_time": "2021-02-19 11:11",
                "author":"naaz"
                }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"narrator":["Missing data for required field."]}\n')

    def test_AudiobookTitle_required(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"audiobook",
                "audioFileMetadata":{
                "duration":"4",
                "uploaded_time": "2021-02-19 11:11",
                "narrator":"naaz",
                "author":"naazz"
                }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        #print("respon", response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"title":["Missing data for required field."]}\n')
        

    def test_SongCreate(self):
        headers = {'Content-type': 'application/json'}
        test_data = json.dumps({
                "audioFileType":"song",
                "audioFileMetadata":{
                "name":"mysong",
                "duration":"4",
                "uploaded_time": "2021-02-19 11:11" }})
        response = self.tester.post(self.create_url,data=test_data,headers=headers)
        self.assertEqual(response.status_code, 200)
        
    
    def test_Read_Songs(self):
        id = Song.objects()[0].id
        response = self.tester.get('/audio/song/'+str(id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0]['_id'], id)
        

    def test_Update_Songs(self):
        headers = {'Content-type': 'application/json'}
        id = Song.objects()[0].id
        test_data = json.dumps({
                "name":"new_name",
                "duration":"4",
                "uploaded_time": "2021-02-19 11:11",
                })
        response = self.tester.put('/updateaudio/song/'+str(id)+'/', data=test_data, headers=headers)
        self.assertEqual(response.status_code, 200)
        #print("r", response.status_code, response.data)
        self.assertEqual(response.data, b'{"message":"Successfully Updated"}\n')

    
    def test_Delete_Songs(self):
        headers = {'Content-type': 'application/json'}
        id = Song.objects()[0].id
        response = self.tester.delete('/deleteaudio/song/'+str(id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"message":"Successfully Deleted"}\n')
        
    
    def test_Get_AllSongs(self):
        response = self.tester.get('/audio/song/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)


    def test_404(self):
        response = self.tester.get('/not_exist')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b"<h1>404</h1><p>The resource could not be found.</p>")

    

if __name__ == '__main__':
    unittest.main()
