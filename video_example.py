from dash import *

app = dash.Dash(__name__)

src = 'assets/GoogleChrom.mp4'


app.layout = html.Div([
            html.Video(
                id='video-player1',
                src='assets/GoogleChrom.mp4',
                autoPlay=False,
                loop=False,
                controls=True,
                style={'width': '45%'}
            ),
            html.Button("Start", id="start-button", n_clicks=0),

            html.Video(
                id="video-player2",
                src='assets/GoogleChrom.mp4',
                autoPlay=False,
                loop=False,
                controls=True,
                style={'width': '45%'}
            ),
            html.Button("Stop", id="stop-button", n_clicks=0)
    ])


@callback(
    Output('video-player1', 'autoPlay'),
    Output('video-player1', 'loop'),
    # Output('video-player2', 'autoPlay'),
    # Output('video-player2', 'loop'),
    # Output('video-player2', 'src'),
    Input('start-button', 'n_clicks'),
    # Input('start-button', 'n_clicks'),
    State('video-player1', 'autoPlay'),
    State('video-player1', 'loop'),
    # State('video-player2', 'autoPlay'),
    # State('video-player2', 'loop'),
)
def update_video(start_clicks, stop_clicks, auto_play1, loop1):
    auto_play1, loop1 = False
    if start_clicks > 0 and stop_clicks < 1:
        print(start_clicks)
        auto_play1, loop1 = True
        return auto_play1, loop1
    else:
        auto_play1, loop1 = False
        return auto_play1, loop1


if __name__ == '__main__':
    app.run_server(debug=True)
