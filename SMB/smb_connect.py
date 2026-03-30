from smb.SMBConnection import SMBConnection

def authenticate_smb(server, username, password, domain=''):
    smb_connection = SMBConnection(username, password, 'python_script', server, domain=domain, use_ntlm_v2=True, is_direct_tcp=True)

    try:
        # Establish an SMB connection
        smb_connection.connect(server, 445)
        shares = smb_connection.listShares()
        print("VALID CREDENTIALS: " + username + ":" + password)
    except Exception as e:
        print("Error:", e)
    finally:
        if smb_connection:
            smb_connection.close()

if __name__ == "__main__":
    # Replace these values with your SMB server details
    smb_server = "192.168.3.241"
    smb_username = "WinTest"
    smb_password = "Password123"

    authenticate_smb(smb_server, smb_username, smb_password)