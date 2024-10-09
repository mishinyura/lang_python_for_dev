

def main():
    with open('data/source.txt', 'r', encoding='utf-8') as i_file:
        with open('results/destination.txt', 'w', encoding='utf-8') as o_file:
            o_file.write(i_file.read())

if __name__ == '__main__':
    main()