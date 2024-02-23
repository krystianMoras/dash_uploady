from dash import Dash, html, Output, Input, dcc
from dash_uploady.DashUploady import DashUploady
from dash_uploady.DashUploadyTarget import DashUploadyTarget
from dash_uploady.configure_upload import configure_upload
from flask import request, abort, Response
from dash_uploady.http_request_handler import HttpRequestHandler
import time 
app = Dash(__name__)

class MyHttpRequestHandler(HttpRequestHandler):
    def post(self):
        print("post")
        time.sleep(1)
        # simulate error
        return Response("Error", status=501)

    def get(self):
        print("get")
        return "OK"
    
configure_upload(app, folder="uploads", use_upload_id=True, http_request_handler=MyHttpRequestHandler)

app.layout = html.Div([
    
    DashUploady(
        id="uploady",
        webkitdirectory=True,
        multiple=True,
        children=[
            DashUploadyTarget([
            html.Button("Upload Files", id="upload-button"),
        ]),
        html.Div(id="output"),
        html.Div(id="output2"),
        html.Div(id="output3")
        
        ]
    ),
])

@app.callback(
    Output("output", "children"),
    Output("upload-button", "disabled"),
    Input("uploady", "finished"),
)
def update_output(finished):
    if finished is None or finished:
        return "Upload finished!" , False
    
    return "Upload not finished yet", True

@app.callback(
    Output("output2", "children"),
    Input("uploady", "progress")
)
def update_output(progress):
    print(progress)
    return f"Progress: {progress*100}%" if progress else "No progress yet"

@app.callback(
    Output("output3", "children"),
    Input("uploady", "errors")
)
def update_output(errors):
    print(errors)
    return f"Errors: {errors}" if errors else "No errors yet"

if __name__ == "__main__":
    app.run_server(debug=True)
