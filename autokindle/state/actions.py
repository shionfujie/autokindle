def Initialize(is_connected, paths):
    return dict(type='INITIALIZE', is_connected=is_connected, paths=paths)

def Connected():
    return dict(type='CONNECTED')


def Disconnected():
    return dict(type='DISCONNECTED')


def NewFile(path):
    return dict(type='NEW_FILE', path=path)

def FailedTransfer(path):
    return dict(type='TRANSFER_FAILED', path=path)
