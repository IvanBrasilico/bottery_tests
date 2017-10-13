'''Configuration of the routes, or vocabulary of the bot'''
from bottery.conf.patterns import Pattern, DefaultPattern, \
    HookableFuncPattern, HookPattern, FuncPattern
from bottery.views import pong
from views.views import help_text, consulta_conteiner, \
    two_tokens, works, consulta_lacre, say_help, report_api, \
    list_log, consulta_lacre_hook, end_hook_list
from views.tecviews import consulta_tec


conversation = HookPattern(end_hook_list)
patterns = [
    conversation,
    Pattern('ping', pong),
    Pattern('help', help_text),
    Pattern('log', list_log),
    FuncPattern('cc', consulta_conteiner, two_tokens),
    FuncPattern('ll', consulta_lacre, two_tokens),
    HookableFuncPattern('llhook', consulta_lacre_hook, two_tokens, conversation),
    HookableFuncPattern('tec', consulta_tec, two_tokens, conversation),
    FuncPattern('report', report_api, two_tokens),
    Pattern('teste', works),
    DefaultPattern(say_help)
]
