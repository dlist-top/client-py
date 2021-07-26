# DList.top Python client
Official [dlist.top](https://dlist.top) gateway client for Go.


## Installation

`pip install dlist-top`

## Setup

To get your token please refer to the [DList.top documentation](https://github.com/dlist-top/docs/wiki/Getting-started).


## Usage

```
from dlist_top import Client

dlist = Client(token='YOUR DLIST TOKEN')
dlist.connect()

@dlist.on('rate')
def on_rate(data):
    print(data)
    
@dlist.on('vote')
def on_vote(data):
    print(data)
```