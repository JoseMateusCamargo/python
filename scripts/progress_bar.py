from tqdm import tqdm

if __name__ == '__main__':
    numbers = range(int(10e6))
    for i in tqdm(numbers, colour='blue', desc="Progress"):
        pass
