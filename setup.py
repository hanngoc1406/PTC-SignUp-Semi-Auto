userName = input('Nhap ten muon tao: ')
password = input('Nhap password muon tao: ')
n = input('Nhap so tai khoan muon tao: ')

for i in range(1, int(n)):
    exec(open('createAccounts.py').read())