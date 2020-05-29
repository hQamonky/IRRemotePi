import markdown
import os
from src.controller import Controller
from flask import Flask
from flask_restful import Resource, Api, reqparse

con = Controller()

app = Flask(__name__)
api = Api(app)


# Route shows the user guide file.
@app.route('/')
def index():
    # Open file
    with open(os.path.dirname(app.root_path) + "/../docs/API User Guide.md", 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)


class ClearDatabase(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.clear_database()}, 200


class Devices(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_devices()}, 200

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        return {'message': 'Device has been added', 'data': con.new_device(args.name)}, 201


class Device(Resource):
    @staticmethod
    def get(device_id):
        return {'message': 'Success', 'data': con.get_device(device_id)}, 200

    @staticmethod
    def post(device_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        return {'message': 'Device has been updated', 'data': con.edit_device(device_id, args.name)}, 201

    @staticmethod
    def delete(device_id):
        return {'message': 'device has been removed.', 'data': con.delete_device(device_id)}, 200


class Record(Resource):
    @staticmethod
    def get(device_id):
        return "Ready to record a new command for " + con.start_recording(device_id)

    @staticmethod
    def post(device_id):
        parser = reqparse.RequestParser()
        parser.add_argument('command_name', required=True)
        args = parser.parse_args()

        return {'message': 'Command has been saved', 'data': con.end_recording(device_id, args.command_name)}, 201


class Command(Resource):
    @staticmethod
    def post(device_id, command_id):
        parser = reqparse.RequestParser()
        parser.add_argument('command_name', required=True)
        args = parser.parse_args()
        return {
                   'message': 'Command has been updated',
                   'data': con.edit_command(device_id, command_id, args.command_name)
               }, 201

    @staticmethod
    def delete(device_id, command_id):
        return {'message': 'command has been removed.', 'data': con.delete_command(device_id, command_id)}, 200


class Send(Resource):
    @staticmethod
    def get(device_id, command_id):
        return {'message': 'Command has been sent', 'data': con.send_command(device_id, command_id)}, 200


api.add_resource(ClearDatabase, '/database/clear')
api.add_resource(Devices, '/devices')
api.add_resource(Device, '/device/<device_id>')
api.add_resource(Record, '/device/<device_id>/record')
api.add_resource(Command, '/device/<device_id>/command/<command_id>')
api.add_resource(Send, '/device/<device_id>/send/<command_id>')
