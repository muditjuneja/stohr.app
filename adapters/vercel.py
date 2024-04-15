import subprocess

def deploy_site(vercelToken,is_production=True):
    subprocess.run('cd my-store && vercel --token ' + vercelToken + (' --prod' if is_production else '') + ' --yes', shell=True)
