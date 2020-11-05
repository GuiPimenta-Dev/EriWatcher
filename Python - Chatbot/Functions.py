from telebot import TeleBot,types
import os
from time import sleep

bot = TeleBot("578019812:AAFCuN6_fgcxRJmsnkYULmRoVPHHmdeTIFI")

def controlMarkup(init,end,array=[]):
    print("Início: "+ str(init),"Fim: " + str(end))
    iter = 0
    markup = types.InlineKeyboardMarkup()
    for value in array:
        if iter>=init and iter <= end:
            Id = value.split(",")[0]
            Funcao = value.split(",")[1]

            if Funcao == "COLETAR ESTATÍSTICAS DE OBJETO\n":
                markup.add(types.InlineKeyboardButton(text=Id + " \u2611\ufe0f", callback_data=Id + " ExtractTrue"))

            else:
                markup.add(types.InlineKeyboardButton(text=Id, callback_data=Id))
        iter += 1

    return markup


def SrControl(state,exec = False):
    #Estado 0 --> Página principal da SR
    #Estado 1 --> Dados do solicitante
    h = open("Files\OperacaoSR.txt", "r", encoding="utf-8").readlines()[1:]
    #status = h.read()
    print(h)

    markup = types.InlineKeyboardMarkup()

    for value in h:
        if value == "Alterar Atribuição\n":
            markup.add(types.InlineKeyboardButton(text="Alterar Atribuição",callback_data='AlterarAtribuicao'))

        if value == "Trabalhar Ticket\n":
            markup.add(types.InlineKeyboardButton(text="Trabalhar Ticket", callback_data='TrabalharTicket'))

        if value == "Cancelar Ticket\n":
            markup.add(types.InlineKeyboardButton(text="Cancelar Ticket", callback_data='CancelarTicket'))

        if value == "Sugerir Fechamento\n":
            markup.add(types.InlineKeyboardButton(text="Sugerir Fechamento", callback_data='SugerirFechamento'))

    if exec :
        markup.add(types.InlineKeyboardButton(text="Executar RPA", callback_data='ExecutarRPA'))

    if state == 0:
        markup.add(types.InlineKeyboardButton(text="Voltar para fila", callback_data="Voltar"),
                   types.InlineKeyboardButton(text="Dados do solicitante",
                                              callback_data="Dados_solicitante"))
    elif state == 1:
        markup.add(types.InlineKeyboardButton(text="Voltar para fila",callback_data="Voltar"),
                   types.InlineKeyboardButton(text="Dados do ticket", callback_data="Dados_ticket"))


    return markup


def CleanMessage(msg,text):
    sleep(1)
    bot.send_chat_action(chat_id=msg.from_user.id, action='typing')
    sleep(3)

    botmsg = bot.send_message(chat_id=msg.from_user.id,
                              text=text)
    sleep(1)
    bot.send_chat_action(chat_id=msg.from_user.id, action='typing')
    return botmsg

def CleanCallBack(call,text):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    botmsg = bot.send_message(chat_id=call.from_user.id,
                              text=text,parse_mode='markdown')
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')

    return botmsg

def YesNoQuery(callbackdata1,callbackdata2):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Sim", callback_data=callbackdata1),
               types.InlineKeyboardButton(text="Não",
                                          callback_data=callbackdata2))

    return markup

def exec_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Extrair usuário", callback_data="ExtrairUsuario"))
    markup.add(types.InlineKeyboardButton(text="Dados do ticket", callback_data="Dados_ticket"))

    return markup

def extract_user():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Coliseu", callback_data="Extract_COLISEU"),
               types.InlineKeyboardButton(text="Spazio",callback_data="Extract_SPAZIO"),
               types.InlineKeyboardButton(text="Test Factory",callback_data="Extract_TESTFACTORY"))
    markup.add(types.InlineKeyboardButton(text="Dados do ticket", callback_data="Dados_ticket"))

    return markup






