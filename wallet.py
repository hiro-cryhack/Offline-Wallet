import hashlib
import os
import json
import getpass
from cryptography.fernet import Fernet

# 文件路径
PASSWORD_FILE = "password.json"
WALLETS_FILE = "wallets.json"
KEY_FILE = "key.key"

# 生成或加载密钥
def load_or_generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    return key

# 加密数据
def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# 解密数据
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

# 保存钱包信息到文件
def save_wallets(wallets, key):
    encrypted_wallets = encrypt_data(json.dumps(wallets), key)
    with open(WALLETS_FILE, "wb") as wallets_file:
        wallets_file.write(encrypted_wallets)

# 验证密码
def authenticate():
    if not os.path.exists(PASSWORD_FILE):
        print("密码尚未设置，请先设置密码。")
        return False

    with open(PASSWORD_FILE, "r") as file:
        data = json.load(file)
        stored_password = data["password"]

    while True:
        password = getpass.getpass("请输入密码: ")
        # 使用哈希函数加密密码
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # 检查哈希后的密码是否匹配预设密码
        if hashed_password == stored_password:
            return True
        else:
            print("密码错误，请重试。")
            return False

# 设置密码
def set_password():
    while True:
        password = getpass.getpass("请设置密码: ")
        confirm_password = getpass.getpass("请确认密码: ")
        if password == confirm_password:
            # 使用哈希函数加密密码
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            # 将哈希后的密码保存到文件中
            with open(PASSWORD_FILE, "w") as file:
                json.dump({"password": hashed_password}, file)
            print("密码设置成功。")
            break
        else:
            print("两次输入的密码不一致，请重新设置。")

# 删除钱包信息
def delete_wallet(wallets, selected_wallet_name, key):
    del wallets[selected_wallet_name]
    print(f"钱包 '{selected_wallet_name}' 信息已删除。")
    # 更新钱包信息到文件
    save_wallets(wallets, key)

# 修改钱包信息
def modify_wallet(wallets, selected_wallet_name, key):
    print("已存在的钱包信息:")
    wallet_infos = wallets[selected_wallet_name]
    for j, wallet_info in enumerate(wallet_infos, start=1):
        print(f"\n钱包{j}:")
        print(f"链: {wallet_info.get('chain', '未设置')}")
        print(f"钱包地址: {wallet_info.get('wallet_address', '未设置')}")
        print(f"钱包助记词: {wallet_info.get('mnemonic_phrase', '未设置')}")
        print(f"钱包私钥: {wallet_info.get('private_key', '未设置')}")
    selected_wallet_info_index = int(input("请选择要修改的钱包信息编号: ")) - 1
    if 0 <= selected_wallet_info_index < len(wallet_infos):
        selected_wallet_info = wallet_infos[selected_wallet_info_index]
        print("\n1. 修改链")
        print("2. 修改钱包地址")
        print("3. 修改钱包助记词")
        print("4. 修改钱包私钥")
        choice_4_2 = input("请选择操作: ")
        if choice_4_2 == '1':
            try:
                new_chain = input("请输入新链: ")
                confirmation = input("确认修改此钱包信息？(y/n): ").strip().lower()
                if confirmation == 'y':
                    selected_wallet_info["chain"] = new_chain
                    print("链已修改。")
                    # 更新钱包信息到文件
                    save_wallets(wallets, key)
            except Exception as e:
                print("修改链时出现异常:", e)
        elif choice_4_2 == '2':
            try:
                new_wallet_address = input("请输入新的钱包地址: ")
                confirmation = input("确认修改此钱包信息？(y/n): ").strip().lower()
                if confirmation == 'y':
                    selected_wallet_info["wallet_address"] = new_wallet_address
                    print("钱包地址已修改。")
                    # 更新钱包信息到文件
                    save_wallets(wallets, key)
            except Exception as e:
                print("修改钱包地址时出现异常:", e)
        elif choice_4_2 == '3':
            try:
                new_mnemonic_phrase = getpass.getpass("请输入新的钱包助记词: ")
                confirmation = input("确认修改此钱包信息？(y/n): ").strip().lower()
                if confirmation == 'y':
                    selected_wallet_info["mnemonic_phrase"] = new_mnemonic_phrase
                    print("钱包助记词已修改。")
                    # 更新钱包信息到文件
                    save_wallets(wallets, key)
            except Exception as e:
                print("修改钱包助记词时出现异常:", e)
        elif choice_4_2 == '4':
            try:
                new_private_key = getpass.getpass("请输入新的钱包私钥: ")
                confirmation = input("确认修改此钱包信息？(y/n): ").strip().lower()
                if confirmation == 'y':
                    selected_wallet_info["private_key"] = new_private_key
                    print("钱包私钥已修改。")
                    # 更新钱包信息到文件
                    save_wallets(wallets, key)
            except Exception as e:
                print("修改钱包私钥时出现异常:", e)
        else:
            print("无效的选择，请重新输入。")
    else:
        print("输入的编号无效，请重新选择。")

# 删除钱包确认
def confirm_delete():
    while True:
        confirmation = input("确认删除此钱包信息？(y/n): ").strip().lower()
        if confirmation == 'y':
            return True
        elif confirmation == 'n':
            return False
        else:
            print("无效的输入，请重新输入。")

# 修改钱包确认
def confirm_modify():
    while True:
        confirmation = input("确认修改此钱包信息？(y/n): ").strip().lower()
        if confirmation == 'y':
            return True
        elif confirmation == 'n':
            return False
        else:
            print("无效的输入，请重新输入。")

# 主函数，程序入口
def main():
    if not os.path.exists(PASSWORD_FILE):
        set_password()

    while True:
        if authenticate():
            key = load_or_generate_key()

            # 加载已存储的钱包信息
            if os.path.exists(WALLETS_FILE):
                with open(WALLETS_FILE, "rb") as wallets_file:
                    encrypted_wallets = wallets_file.read()
                decrypted_wallets = decrypt_data(encrypted_wallets, key)
                wallets = json.loads(decrypted_wallets)
            else:
                wallets = {}

            while True:
                print("\n1. 存储钱包信息")
                print("2. 查看已存储的钱包信息")
                print("3. 删除已存储的钱包信息")
                print("4. 修改已存储的钱包信息")
                print("5. 退出")
                choice = input("请选择操作: ")

                if choice == '1':
                    # 存储钱包信息的代码
                    while True:
                        print("\n1. 新建钱包名")
                        print("2. 选择钱包并存储信息")
                        print("3. 返回上一级")
                        choice_1 = input("请选择操作: ")

                        if choice_1 == '1':
                            wallet_name = input("请输入新建的钱包名: ")
                            if wallet_name not in wallets:
                                wallets[wallet_name] = []
                                print(f"已成功新建钱包名 '{wallet_name}'。")
                                # 保存钱包信息到文件
                                save_wallets(wallets, key)
                            else:
                                print(f"钱包名 '{wallet_name}' 已存在，请输入其他名称。")

                        elif choice_1 == '2':
                            print("已存在的钱包名:")
                            for i, wallet_name in enumerate(wallets, start=1):
                                print(f"{i}. {wallet_name}")
                            print(f"{i+1}. 返回上一级")
                            selected_index = int(input("请选择要存储信息的钱包编号: ")) - 1
                            wallet_names = list(wallets.keys())
                            if 0 <= selected_index < len(wallet_names):
                                selected_wallet_name = wallet_names[selected_index]
                                chain = input("请输入链: ")
                                wallet_address = input("请输入钱包地址: ")
                                mnemonic_phrase = getpass.getpass("请输入钱包助记词: ")
                                private_key = getpass.getpass("请输入钱包私钥: ")
                                wallets[selected_wallet_name].append({
                                    "chain": chain,
                                    "wallet_address": wallet_address,
                                    "mnemonic_phrase": mnemonic_phrase,
                                    "private_key": private_key
                                })
                                print(f"钱包信息已存储到钱包名 '{selected_wallet_name}'。")
                                # 保存钱包信息到文件
                                save_wallets(wallets, key)
                            elif selected_index == i:
                                break
                            else:
                                print("输入的编号无效，请重新选择。")

                        elif choice_1 == '3':
                            break

                        else:
                            print("无效的选择，请重新输入。")

                elif choice == '2':
                    # 查看钱包信息的代码
                    print("已存储的钱包信息:")
                    while True:
                        print("\n已存在的钱包名:")
                        for i, wallet_name in enumerate(wallets, start=1):
                            print(f"{i}. {wallet_name}")
                        print(f"{i+1}. 返回上一级")
                        selected_index = int(input("请选择要查看的钱包编号: ")) - 1
                        wallet_names = list(wallets.keys())
                        if 0 <= selected_index < len(wallet_names):
                            selected_wallet_name = wallet_names[selected_index]
                            wallet_infos = wallets[selected_wallet_name]
                            print(f"\n钱包名: {selected_wallet_name}")
                            for j, wallet_info in enumerate(wallet_infos, start=1):
                                print(f"\n钱包{j}:")
                                print(f"链: {wallet_info.get('chain', '未设置')}")
                                print(f"钱包地址: {wallet_info.get('wallet_address', '未设置')}")
                                print(f"钱包助记词: {wallet_info.get('mnemonic_phrase', '未设置')}")
                                print(f"钱包私钥: {wallet_info.get('private_key', '未设置')}")
                            print()
                        elif selected_index == i:
                            break
                        else:
                            print("输入的编号无效，请重新选择。")

                elif choice == '3':
                    # 删除钱包信息的代码
                    print("已存在的钱包名:")
                    for i, wallet_name in enumerate(wallets, start=1):
                        print(f"{i}. {wallet_name}")
                    selected_index = int(input("请选择要删除的钱包编号: ")) - 1
                    wallet_names = list(wallets.keys())
                    if 0 <= selected_index < len(wallet_names):
                        selected_wallet_name = wallet_names[selected_index]
                        if confirm_delete():
                            delete_wallet(wallets, selected_wallet_name, key)
                    else:
                        print("输入的编号无效，请重新选择。")

                elif choice == '4':
                    # 修改钱包信息的代码
                    print("已存在的钱包名:")
                    for i, wallet_name in enumerate(wallets, start=1):
                        print(f"{i}. {wallet_name}")
                    selected_index = int(input("请选择要修改的钱包编号: ")) - 1
                    wallet_names = list(wallets.keys())
                    if 0 <= selected_index < len(wallet_names):
                        selected_wallet_name = wallet_names[selected_index]
                        if confirm_modify():
                            modify_wallet(wallets, selected_wallet_name, key)
                    else:
                        print("输入的编号无效，请重新选择。")

                elif choice == '5':
                    print("谢谢使用，再见！")
                    break

                else:
                    print("无效的选择，请重新输入。")

            break

if __name__ == "__main__":
    main()
