from dulwich import porcelain
from dulwich.repo import Repo
import os

LOCAL_REPO = os.getcwd()
REMOTE_REPO = 'https://github.com/melinuxsistemas/sistemaweb'
HEADS = '.git\\refs\\heads\\master'


def check_update():

    ref = Repo('.')
    local_ref = ref.head().decode('utf-8')
    print('Versão local: ',local_ref)
    #log = porcelain.log(LOCAL_REPO)
    #print(log)
    #status = porcelain.status(LOCAL_REPO)
    #print(status)
    remote_commint = porcelain.ls_remote(REMOTE_REPO)[b"HEAD"].decode('utf-8')
    print('\nVersão remota: ',remote_commint)

    #r = porcelain.fetch(LOCAL_REPO,REMOTE_REPO)
    #print(r)
    if local_ref != remote_commint:
        print('\nNOVA VERSÃO DISPONÍVEL,INSTALANDO...')
        update()
    else:
        pass
        print('\nVC JÁ ESTÁ COM A ÚLTIMA VERSÃO INSTALADA.')
def update():

    try:
        porcelain.pull(LOCAL_REPO, REMOTE_REPO)
        print('\nCONSEGUI...')
    except:
        print('\nPUTSS,DEU ERRO,VOU TENTAR DE NOVO...')
        pass
        try:
            print('\nREMOVENDO ARQUIVO MASTER...')
            os.remove(HEADS)
            porcelain.pull(LOCAL_REPO, REMOTE_REPO)
            print('\nCONSEGUI...')
        except:
            pass

if __name__=='__main__':
    import sys
    arguments = sys.argv
    if "update" in arguments:
        check_update()
