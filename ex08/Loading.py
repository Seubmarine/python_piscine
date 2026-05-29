import os

def ft_tqdm(lst: range) -> None:
    
    fake = range(lst.stop + 1)
    for i in fake:
        # percent: int = int((i / lst.stop) * 100)
        percent: int = i * 100 // lst.stop
        size: int = os.get_terminal_size().columns - 40
        bar: str = ""
        
        bar_size: int = size
        arrow_size: int = int(bar_size * (percent / 100))
        empty_size: int = bar_size - arrow_size
        for _ in range(arrow_size):
            bar += '='
        bar += '>'
        bar += ']'
        for _ in range(empty_size):
            bar += ' '
        print(f"{percent:3}%|[{bar}| {i}/{lst.stop}", end='\r')
        # print("", end='\r')
        yield
    float