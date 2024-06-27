import os
c=get_config()
c.ServerApp.ip = "0.0.0.0"
c.ServerApp.port = 8888
c.ContentsManager.allow_hidden = False
c.ServerApp.password_required = False
c.ServerApp.terminado_settings = {"shell_command": ["/bin/bash"]}
# c.ServerApp.root_dir = f"/home/{os.getenv('SAMPL_USER')}"
c.ServerApp.token = ""
# c.ServerApp.base_url = f'/{os.getenv("HOSTNAME")}-ide/'

# if os.getenv('MEMORY_LIMIT'):
#     c.ResourceUseDisplay.mem_limit = int(os.getenv('MEMORY_LIMIT')) * 1*1024*1024

# if os.getenv('CPU_LIMIT'):
#     c.ResourceUseDisplay.cpu_limit = int(os.getenv('CPU_LIMIT'))
#     c.ResourceUseDisplay.trach_cpu_percent = True
