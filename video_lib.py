from flask import  Flask, abort
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

videos = {}
video_args = reqparse.RequestParser()
video_args.add_argument("name", type=str, help='Name is missing', required=True)
video_args.add_argument("likes", type=int, help='Likes are missing', required=True)
video_args.add_argument("views", type=int, help='Views are missing', required=True)


def abort_if_vid_id_not_found(vid_id):
    if vid_id not in videos:
        #abort(404, "Video not found with given video id: " + str(vid_id))       # OK
        abort(404, "Video not found with given video id: " + str(vid_id))

def abort_if_vid_already_exists(vid_id):
    if vid_id in videos:
        #abort(404, "Video not found with given video id: " + str(vid_id))       # OK
        abort(400, "Video already exists video id: " + str(vid_id))


class Video(Resource):

    def get(self):
        return videos


    def get(self, vid_id):
        abort_if_vid_id_not_found(vid_id)
        return videos[vid_id]

    def post(self, vid_id):
        abort_if_vid_already_exists(vid_id)
        args = video_args.parse_args()
        videos[vid_id] = args
        return args, 201

    def delete(self, vid_id):
        abort_if_vid_id_not_found(vid_id)
        vid = videos.pop(vid_id)
        print("--", vid)
        return vid, 204


api.add_resource(Video, "/videos/<int:vid_id>" )


if __name__ == '__main__':
    app.run(debug=True)

