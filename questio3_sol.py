try:
    n = int(input())
except ValueError:
    raise ValueError("value error occurd")
except KeyboardInterrupt:
    raise KeyboardInterrupt("keyboard interrupt error occurd")
except EOFError:
    raise EOFError("end of file error occured")