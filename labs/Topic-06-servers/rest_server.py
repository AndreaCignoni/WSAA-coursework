# The API here implemented allows users to perform CRUD (Create, Read, Update, Delete) operations on music tracks, albums, artists, and playlists.
# The JSON (JavaScript Object Notation) format is used for data exchange between the client and server.
# Author : Andrea Cignoni

from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Initialize an empty list to store tracks
tracks = []

# Get all tracks
@app.route('/tracks', methods=['GET'])
def getAllTracks():
    return "Getting all tracks"

# Find track by ID
@app.route('/tracks/<int:id>', methods=['GET'])
def findTrackById(id):
    return f"This is track id number {id}"

# Create a new track
@app.route('/tracks', methods=['POST'])
def createTrack():
    json_data = request.json
    tracks.append(json_data)  # Add the new track to the list
    return jsonify({"message": "Track created successfully", "track": json_data})

# Update an existing track
@app.route('/tracks/<int:id>', methods=['PUT'])
def updateTrack(id):
    json_data = request.json
    # Add logic to handle the update of the track with the given ID using the provided JSON data
    return jsonify({"message": f"Track with id {id} updated successfully"})

# Delete a track
@app.route('/tracks/<int:id>', methods=['DELETE'])
def deleteTrack(id):
    # Add logic to handle the deletion of the track with the given ID
    return jsonify({"message": f"Track with id {id} deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)