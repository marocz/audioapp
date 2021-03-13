from flask import flash, redirect, render_template, url_for

from forms import AudioForm
from . import db
from .models import Song, Podcast, Audiobook


#Create Request
@auth.route('/create', methods=['POST'])
def create():
    """
    Handle requests to the /create route
    Add an audio file to the database 
    """
    
    requestdata = request.get_json()

    audioFileType = requestdata['audioFileType']

       
    name = requestdata['audioFileMetadata']['name']
    duration = requestdata['audioFileMetadata']['duration']
    host = requestdata['audioFileMetadata']['host']
    initators = requestdata['audioFileMetadata']['initators']

    try:
        if audioFileType == 'song':
            try:
                song = Song(name=name, duration=duration)
                db.session.add(song)
                db.session.commit()
                content = "You have added the song successfully."
                return jsonify(content), 200
            except Exception as e1:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400

        if audioFileType == 'audiobook':
            try:
                audiobook = Audiobook(name=name, duration=duration, host=host, Narrator=initators)
                db.session.add(audiobook)
                db.session.commit()
                content = "You have added the audiobook successfully."
                return jsonify(content), 200
            except Exception as e2:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400

        if audioFileType == 'podcast':
            try:
                podcast = Podcast(name=name, duration=duration, host=host, Participants=initators)
                db.session.add(podcast)
                db.session.commit()
                content = "You have added the audiobook successfully."
                return jsonify(content), 200
            except Exception as e3:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400

    except Exception as e:
        content = "Could not add object successfully"
        print(e)
        return jsonify(content), 500
    
    

#Delete Request
@auth.route('<audioFileType>/<int:audioFileID>', methods=['DELETE'])
def delete():
    """
    Handle requests to the route using path variable 
    Delete a audio to the database 
    """
    form = RegistrationForm()

    audioFileID = request.view_args['audioFileID']
    audioFileType = request.view_args['audioFileType']

    try:
        if audioFileType == 'song':
            try:
                db.execute('delete from song where id =?'[audioFileID])
                db.session.commit()
                content = "You have deleted the audiobook successfully."
                return jsonify(content), 200
            except Exception as e1:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400

        if audioFileType == 'podcast':
            try:
                db.execute('delete from podcast where id =?'[audioFileID])
                db.session.commit()
                content = "You have deleted the podcast successfully."
                return jsonify(content), 200
            except Exception as e2:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400

        if audioFileType == 'audiobook':
            try:
                db.execute('delete from audiobook where id =?'[audioFileID])
                db.session.commit()
                content = "You have deleted the audiobook successfully."
                return jsonify(content), 200
            except Exception as e3:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400 

    except Exception as e:
        content = "Could not delete object successfully"
        print(e)
        return jsonify(content), 500



#Update Request
@auth.route('<audioFileType>/<int:audioFileID>', methods=['POST'])
def updatadata():
    """
    Handle requests to the route using path variable 
    Update an audio to the database 
    """

    requestdata = request.get_json()
    audioFileID = request.view_args['audioFileID']
    audioFileType = request.view_args['audioFileType']

    name = requestdata['audioFileMetadata']['name']
    duration = requestdata['audioFileMetadata']['duration']
    host = requestdata['audioFileMetadata']['host']
    initators = requestdata['audioFileMetadata']['initators']
    try:
        if audioFileType == 'song':
            try:
                song = Song.query.filter_by(id=audioFileID)
                song.name = name
                song.duration = duration
                db.session.commit()
                content = "You have updated the song successfully."
                return jsonify(content), 200
            except Exception as e1:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400  

        if audioFileType == 'audiobook':
            try:
                audiobook = Audiobook.query.filter_by(id=audioFileID)
                audiobook.name = name
                audiobook.duration = duration
                audiobook.host = host
                audiobook.Narrator = initators
                db.session.commit()
                content = "You have updated the audiobook successfully."
                return jsonify(content), 200
            except Exception as e2:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400

        if audioFileType == 'podcast':
            try:
                podcast = Podcast.query.filter_by(id=audioFileID)
                podcast.name = name
                podcast.duration = duration
                podcast.host = host
                podcast.Participants = initators
                db.session.commit()
                content = "You have updated the podcast successfully."
                return jsonify(content), 200
            except Exception as e3:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400

    except Exception as e:
        content = "Could not update object successfully"
        print(e)
        return jsonify(content), 500

#GET Request
@auth.route('<audioFileType>/<int:audioFileID>', methods=['GET'])
def getdata():
    """
    Handle requests to the route using path variable 
    Get an audio from the database 
    """

    requestdata = request.get_json()

    audioFileID = request.view_args['audioFileID']
    audioFileType = request.view_args['audioFileType']

    try:
        if audioFileType == 'song':
            try:
                song = Song.query.filter_by(id=audioFileID)
                content = song
                return jsonify(content), 200
            except Exception as e1:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400

        if audioFileType == 'audiobook':
            try:
                audiobook = Audiobook.query.filter_by(id=audioFileID)
                content = audiobook
                return jsonify(content), 200
            except Exception as e2:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400

        if audioFileType == 'podcast':
            try:
                podcast = Podcast.query.filter_by(id=audioFileID)
                content = podcast
                return jsonify(content), 200
            except Exception as e3:
                content = "Bad Request"
                print(e)
                return jsonify(content), 400
            
    except Exception as e:
        content = "Could not update object successfully"
        print(e)
        return jsonify(content), 500

  
