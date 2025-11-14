'''
python --version
-b     : emitir avisos sobre conversões de bytes/bytearray para str e sobre comparações
         de bytes/bytearray com str ou bytes com int. (-bb: emitir erros)
-B     : não gravar arquivos .pyc durante a importação; também definido por PYTHONDONTWRITEBYTECODE=x
-c cmd : executar o programa passado como string (encerra a lista de opções)
-d     : ativar a saída de depuração do analisador sintático (apenas para especialistas,
         funciona somente em versões de depuração); também definido por PYTHONDEBUG=x
-E     : ignorar variáveis de ambiente PYTHON* (como PYTHONPATH)
-h     : exibir esta mensagem de ajuda e sair (também -? ou --help)
-i     : entrar no modo interativo após executar o script; força um prompt mesmo
         que a entrada padrão (stdin) não pareça ser um terminal; também PYTHONINSPECT=x
-I     : isolar o Python do ambiente do usuário (implica -E, -P e -s)
-m mod : executar um módulo da biblioteca como script (encerra a lista de opções)
-O     : remover instruções `assert` e dependentes de __debug__; adiciona .opt-1 antes
         da extensão .pyc; também definido por PYTHONOPTIMIZE=x
-OO    : faz as mudanças de -O e também descarta docstrings; adiciona .opt-2 antes
         da extensão .pyc
-P     : não adicionar um caminho potencialmente inseguro ao sys.path; também
         definido por PYTHONSAFEPATH
-q     : não exibir mensagens de versão e direitos autorais ao iniciar interativamente
-s     : não adicionar o diretório do usuário (site-packages) ao sys.path; também
         definido por PYTHONNOUSERSITE=x
-S     : não executar 'import site' na inicialização
-u     : forçar os fluxos stdout e stderr a não terem buffer;
         essa opção não afeta o stdin; também definido por PYTHONUNBUFFERED=x
-v     : modo detalhado (mostra os imports executados); também definido por PYTHONVERBOSE=x
         pode ser usado várias vezes para aumentar a verbosidade
-V     : exibir o número da versão do Python e sair (também --version)
         quando usado duas vezes, exibe mais informações sobre a compilação
-W arg : controle de avisos; o argumento é action:message:category:module:lineno
         também definido por PYTHONWARNINGS=arg
-x     : pular a primeira linha do código-fonte, permitindo o uso de formas não-Unix de #!cmd
-X opt : definir opções específicas da implementação
--check-hash-based-pycs always|default|never:
         controlar como o Python invalida arquivos .pyc baseados em hash
--help-env: exibir ajuda sobre variáveis de ambiente do Python e sair
--help-xoptions: exibir ajuda sobre opções específicas da implementação (-X) e sair
--help-all: exibir todas as informações de ajuda e sair

Argumentos:
file   : programa lido de um arquivo de script
-      : programa lido da entrada padrão (stdin) (padrão; modo interativo se for um terminal)
arg ...: argumentos passados ao programa em sys.argv[1:]

'''