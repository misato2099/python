# 啟動虛擬機器執行python腳本用，要同時配合RSA加密的私鑰檔(在虛擬機器生成RSA密碼組後，下載私鑰檔與腳本放一起，然後將公鑰密碼(連用戶名)新增至虛擬機器的公鑰欄)及一份記有安裝本腳本所需套件的requirements.txt檔(如下)

# Function dependencies, for example:
# package>=version
# google-api-python-client
# oauth2client
# google-cloud-storage
# paramiko
# google-auth


from googleapiclient import discovery
from google.cloud import storage
from oauth2client.client import GoogleCredentials
import paramiko
import subprocess

def start_vm(request):
    # 虛擬機器的名稱和專案 ID
    project = 'webcrawler-XXXXXXX'
    zone = 'asia-east1-a'
    vm_name = 'instance-1'

    # 建立 Compute Engine API 的客戶端
    credentials = GoogleCredentials.get_application_default()
    compute = discovery.build('compute', 'v1', credentials=credentials)

    # 呼叫 Compute Engine API 開始虛擬機器
    request = compute.instances().start(project=project, zone=zone, instance=vm_name)
    response = request.execute()

    # return '虛擬機器已啟動'


    # SSH 連線設定
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key_path = './private_key.pem'
    with open(private_key_path, 'r') as f:
        private_key = f.read()
    ssh_client.connect(hostname='IP', username='XXXXXXX', key_filename=private_key_path)

    # 執行指定的腳本
    stdin, stdout, stderr = ssh_client.exec_command('python3 news_crawler_cloud_us.py')

    # 取得執行結果
    output = stdout.read().decode()

    # 關閉虛擬機器
    # ssh_client.exec_command('sudo shutdown now')

    # 關閉 SSH 連線
    ssh_client.close()

    return f'腳本執行結果：\n{output}'
