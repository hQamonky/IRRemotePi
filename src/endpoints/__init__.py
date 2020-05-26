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


# Devices --------------------------------------------------------------------------------------------------------------


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
    def get(device):
        return {'message': 'Success', 'data': con.get_device(device)}, 200

    @staticmethod
    def post(device):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        return {'message': 'Device has been updated', 'data': con.edit_device(device, args.name)}, 201

    @staticmethod
    def delete(device):
        return {'message': 'device has been removed.', 'data': con.delete_device(device)}, 200


# Commands -------------------------------------------------------------------------------------------------------------


class Commands(Resource):
    @staticmethod
    def get(device):
        return {'message': 'Success', 'data': con.get_commands(device)}, 200


class Record(Resource):
    @staticmethod
    def get():
        con.start_recording()
        return "Ready to record"

    @staticmethod
    def post(device):

        parser = reqparse.RequestParser()
        parser.add_argument('command_name', required=True)
        args = parser.parse_args()

        return {'message': 'Command has been added', 'data': con.end_recording(device, args.name)}, 201


class Command(Resource):
    @staticmethod
    def get(device, command):
        return {'message': 'Success', 'data': con.get_command(device, command)}, 200

    @staticmethod
    def post(device, command):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        return {'message': 'Command has been updated', 'data': con.edit_command(device, command, args.name)}, 201

    @staticmethod
    def delete(device, command):
        return {'message': 'command has been removed.', 'data': con.delete_command(device, command)}, 200


class Send(Resource):
    @staticmethod
    def get(device, command):
        con.send_command(device, command)
        return "Command sent"


api.add_resource(Devices, '/devices')
api.add_resource(Device, '/device/<device>')
api.add_resource(Commands, '/device/<device>/commands')
api.add_resource(Record, '/device/<device>/commands/record')
api.add_resource(Command, '/device/<device>/command/<command>')
api.add_resource(Send, '/device/<device>/command/<command>/send')
