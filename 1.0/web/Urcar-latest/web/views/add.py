import dash
from dash import Dash, dcc, html, callback
import dash_bootstrap_components as dbc
from init import tool
from dash.dependencies import Input, Output, State
import time

layout = html.Div(
    [
        html.Br(),  # 换行

        dbc.Container(
            [
                dbc.Container(
                html.Img(
                    src='assets/car.jpg',
                    style={
                        'width': '100%',
                        'height': '100%',
                        'margin-left': '0px',
                    }    
                ),
                style={
                    'max-width': '500px'
                }
            ),
                dbc.Container(
                    html.H1('添加车辆信息',className="display-4 "),
                    style={
                        'max-width': '270px'
                    }
                ),

                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('1. 您的身份')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "工厂", "value": 1},
                                    {"label": "销售处", "value": 2},
                                    {"label": "验车员", "value": 3}
                                ],
                                inline=True
                            )
                        )
                    ]
                ),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('2. 记录类型')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "出厂", "value": 1},
                                    {"label": "维修", "value": 2},
                                    {"label": "交易", "value": 3},
                                    {"label": "核实", "value": 4},
                                    {"label": "报废", "value": 5},
                                ],
                                inline=True
                            )
                        )
                    ]
                ),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('3. 查询信息')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Checklist(
                                options=[
                                    {"label": "初始信息", "value": 1},
                                    {"label": "价格", "value": 2},
                                    {"label": "行驶里程", "value": 3},
                                    {"label": "评分", "value": 4},
                                    {"label": "其他", "value": 5}
                                ],
                                inline=True
                            ),
                        )
                    ]
                ),
                html.Hr(),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Form(
                                [
                                    dbc.Label('车辆ID: ', html_for='input-carID'),
                                    dbc.Input(type="text", id='input-carID'),
                                ]
                            ),
                            width=6
                        ),
                        dbc.Col(
                            dbc.Form(
                                [
                                    dbc.Label('添加内容: ', html_for='input-content'),
                                    dbc.Input(type="text", id='input-content'),
                                ]
                            ),
                            width=6
                        ),
                        
                    ],
                ),

                html.Hr(),
                html.Br(),

                dbc.Container(
                    dbc.Button(
                        '添加',
                        id='add-button',
                        size='lg',
                        color="primary",
                        className="d-grid gap-4 col-12 ",
                        # style={'margin-left': '260px',}
                    ),
                    style={
                        'max-width': '300px'
                    }
                ),

                html.Hr(),
                dbc.Spinner(html.Div(id="loading-add",style={'margin-top': '0px',})),
  

            ],
            style={
            'margin-top': '0px',
            'max-width': '800px'
            }
        )
    ]
)

@callback(
    Output("loading-add", "children"),
    Input('add-button', 'n_clicks'),
    State('input-carID', 'value'),
    State('input-content', 'value'),
    prevent_initial_call=True
)
def refresh_output(n_clicks, carID, content):

    if n_clicks:

        time.sleep(0.5)

        if carID:
            if content:
                address = tool.new(content)
                if carID not in tool.addresses.keys():
                    tool.addresses[carID] = [address]
                    res =  carID + ' add init info'
                else:
                    tool.addresses[carID].append(address)
                    res =  carID + ' add more info'

                return dbc.Alert(res, color="success" ,style={'margin-top': '0px',})
                
            else:
                res =  'Please input content'
        else:
            res =  'Please input Car ID'
        
        return dbc.Alert(res, color="danger" ,style={'margin-top': '0px',})

    return dash.no_update


