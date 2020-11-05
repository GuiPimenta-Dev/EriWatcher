from telebot import TeleBot,types
import os
from time import sleep
import Functions as Fc
import MyStorage
import MyStates as MS


bot = TeleBot("578019812:AAFCuN6_fgcxRJmsnkYULmRoVPHHmdeTIFI")

fileContent = open("Files\BD-N1.txt", "r",encoding="utf-8").readlines()[1:]

Init = 5
@bot.message_handler(commands=['start'])
def start_handler(msg):
    global Init
    Init = 5

    BOASVINDAS="Bem vindo!\n\nNeste momento estou analisando a fila Analyser-OSS INFRA BD N1\n\n" \
               "Aguarde alguns instantes enquanto carrego a fila!"

    botmsg = Fc.CleanMessage(msg,BOASVINDAS)


    os.system("Executables\GetSR.exe")

    bot.send_chat_action(chat_id=msg.from_user.id, action='upload_photo')
    global fileContent

    fileContent = open("Files\BD-N1.txt", "r", encoding="utf-8").readlines()[1:]

    MainCaption = open("Files\MainCaption.txt", "r", encoding="utf-8")
    markup = Fc.controlMarkup(0,5,fileContent)
    markup.add(types.InlineKeyboardButton(text="Atualizar",callback_data='atualizar'),types.InlineKeyboardButton(text="Próximo", callback_data='next'))


    bot.delete_message(chat_id=msg.from_user.id, message_id=botmsg.message_id)
    bot.send_photo(msg.from_user.id, photo=open('Files\BD-N1.png', 'rb'),caption=MainCaption, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: 'atualizar' in call.data)
def att_everything(call):
    global Init
    Init=5


    botmsg = Fc.CleanCallBack(call,'Atualizando a fila ...')

    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    os.system("Executables\GetSR.exe")
    bot.send_chat_action(chat_id=call.from_user.id, action='upload_photo')

    global fileContent

    fileContent = open("Files\BD-N1.txt", "r", encoding="utf-8").readlines()[1:]

    markup = Fc.controlMarkup(0, 5, fileContent)
    markup.add(types.InlineKeyboardButton(text="Atualizar", callback_data='atualizar'),
               types.InlineKeyboardButton(text="Próximo", callback_data='next'))

    MainCaption = open("Files\MainCaption.txt", "r", encoding="utf-8")
    bot.delete_message(chat_id=call.from_user.id, message_id=botmsg.message_id)
    bot.send_photo(call.from_user.id, photo=open('Files\BD-N1.png', 'rb'), caption=MainCaption,reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'next' in call.data)
def edit_keyboard(call):
    global Init
    Init= Init+1
    End = Init + 5

    #print("Inicio: " + str(Init + 1), "Fim: " + str(End))


    markup = Fc.controlMarkup(Init, End, fileContent)

    if End >= len(fileContent):
        markup.add(types.InlineKeyboardButton(text="Anterior", callback_data='back'))

    else :
        markup.add(types.InlineKeyboardButton(text="Anterior",callback_data='back'),types.InlineKeyboardButton(text="Próximo", callback_data='next'))

    bot.answer_callback_query(callback_query_id=call.id)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup)

    Init=Init+5



@bot.callback_query_handler(func=lambda call: 'back' in call.data)
def edit_keyboard(call):
    global Init
    End = Init-6
    Init=End - 5

    markup = Fc.controlMarkup(Init, End, fileContent)

    if End <= 6 :
        markup.add(types.InlineKeyboardButton(text="Atualizar",callback_data='atualizar'),types.InlineKeyboardButton(text="Próximo", callback_data='next'))


    else:
        markup.add(types.InlineKeyboardButton(text="Anterior", callback_data='back'),types.InlineKeyboardButton(text="Próximo", callback_data='next'))

    bot.answer_callback_query(callback_query_id=call.id)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup)

    Init = Init+5

@bot.callback_query_handler(func=lambda call: 'Dados_solicitante' in call.data)
def edit_media(call):
    markup = Fc.SrControl(1,execute)
    bot.answer_callback_query(callback_query_id=call.id)
    bot.edit_message_media(media=types.InputMediaPhoto(open("Files/SR_dados_image.png", 'rb'),caption=caption), chat_id=call.message.chat.id,
                           message_id=call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: 'Dados_ticket' in call.data)
def edit_media(call):

    markup = Fc.SrControl(0,execute)
    bot.answer_callback_query(callback_query_id=call.id)
    bot.edit_message_media(media=types.InputMediaPhoto(open("Files/SRimage.png", 'rb'),caption=caption), chat_id=call.message.chat.id,
                           message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'Voltar' in call.data)
def edit_media(call):
    global Init
    Init=5
    markup = types.InlineKeyboardMarkup()
    markup = Fc.controlMarkup(0, Init, fileContent)
    markup.add(types.InlineKeyboardButton(text="Atualizar",callback_data='atualizar'),types.InlineKeyboardButton(text="Próximo", callback_data='next'))

    bot.edit_message_media(media=types.InputMediaPhoto(open("Files/BD-N1.png", 'rb')), chat_id=call.message.chat.id,
                           message_id=call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: 'Atualizar' in call.data)
def att_handler(call):
    bot.edit_message_text(text="Atualizando fila ...", chat_id=call.from_user.id,message_id=call.id)

    os.system("Executables\GetSR.exe")

    bot.send_chat_action(chat_id=call.from_user.id, action='upload_photo')
    global fileContent
    global Init
    fileContent = open("Files\BD-N1.txt", "r", encoding="utf-8").readlines()[1:]


    markup = controlMarkup(0,Init,fileContent)
    markup.add(types.InlineKeyboardButton(text="Próximo", callback_data='next'))

    bot.send_photo(call.from_user.id, photo=open('Files\BD-N1.png', 'rb'), reply_markup=markup)



@bot.callback_query_handler(func=lambda call: 'AlterarAtribuicao' in call.data)
def alter_atribuition(call):
    msgbot=Fc.CleanCallBack(call,"Alterando atribuição ...")

    os.system("Executables\AlterAtribution.exe")

    markup = Fc.SrControl(0,execute)
    bot.delete_message(chat_id=call.message.chat.id, message_id=msgbot.message_id)

    bot.send_photo(photo=open("Files/SRimage.png", 'rb'), caption=caption,
                           chat_id=call.message.chat.id,
                            reply_markup=markup)

#### Conversation


###Cancelar Ticket
USER_DATA = {}
@bot.callback_query_handler(func=lambda call: 'CancelarTicket' in call.data)
def cancel_Ticket(call):
    #global USER_DATA

    # Limpa da memória informações prévias do usuário
    USER_DATA[call.from_user.id] = {}
    global mybotmsg
    # Pergunta qual o diário de trabalho
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    mybotmsg = bot.send_message(chat_id=call.from_user.id,
                              text="Informe o motivo de cancelamento.",reply_markup=types.ForceReply())

    # Insert state
    MyStorage.set_user_state(call.from_user.id, MS.CancelTicket.WAIT_Motive)

@bot.message_handler(func=lambda msg: MyStorage.get_current_state(msg.from_user.id) == MS.CancelTicket.WAIT_Motive)
def save_motive(msg):
    bot.delete_message(chat_id=msg.from_user.id, message_id=mybotmsg.message_id)
    # get user data
    data = USER_DATA[msg.from_user.id]

    # save MOTIVE to user data
    data['motive'] = msg.text

    # update storage
    USER_DATA[msg.from_user.id] = data

    # Confirm the Motive
    markup = Fc.YesNoQuery("GetNote","NotConfirmedTicket")
    bot.send_message(text="Confirma o motivo de cancelamento ?",chat_id=msg.from_user.id,reply_markup=markup,reply_to_message_id=msg.message_id)

    bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id)

    # update storage
    MyStorage.set_user_state(msg.from_user.id, MS.CancelTicket.WAIT_Note)

    print(data)



@bot.callback_query_handler(func=lambda call: 'GetNote' in call.data)
def get_Note(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    global mybotmsg
    mybotmsg = bot.send_message(chat_id=call.from_user.id,
                                text="Agora informe a nota de cancelamento.",reply_markup=types.ForceReply())

    # Insert state
    MyStorage.set_user_state(call.from_user.id, MS.CancelTicket.WAIT_Note)


@bot.message_handler(func=lambda msg: MyStorage.get_current_state(msg.from_user.id) == MS.CancelTicket.WAIT_Note)
def save_motive(msg):
    bot.delete_message(chat_id=msg.from_user.id, message_id=mybotmsg.message_id)
    # get user data
    data = USER_DATA[msg.from_user.id]

    # save JOURNAL to user data
    data['note'] = msg.text

    # update storage
    USER_DATA[msg.from_user.id] = data

    # Confirm the Journal
    markup = Fc.YesNoQuery("ConfirmedCancelTicket", "NotConfirmedTicket")
    bot.send_message(text="Confirma a nota de cancelamento ?", chat_id=msg.from_user.id, reply_markup=markup,
                     reply_to_message_id=msg.message_id)

    bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id)

    # update storage
    MyStorage.set_user_state(msg.from_user.id, MS.CancelTicket.Start)

    f = open("Files\CancelTicket.txt", "w")
    f.write(data['motive'] + "-" + data['note'])
    f.close()


    print(data)




@bot.callback_query_handler(func=lambda call: 'ConfirmedCancelTicket' in call.data)
def yes_Cancel(call):

    msgbot=Fc.CleanCallBack(call,"* Cancelando " + caption + "*")

    os.system("Executables\CancelTicket.exe")

    MainCaption = open("Files\MainCaption.txt", "r", encoding="utf-8")

    bot.delete_message(chat_id=call.message.chat.id, message_id=msgbot.message_id)

    markup = Fc.controlMarkup(0, 5, fileContent)
    markup.add(types.InlineKeyboardButton(text="Atualizar",callback_data='atualizar'),
               types.InlineKeyboardButton(text="Próximo", callback_data='next'))

    bot.send_photo(call.from_user.id, photo=open('Files\BD-N1.png', 'rb'),caption=MainCaption, reply_markup=markup)



###Sugerir Fechamento
CLOSE_USER_DATA = {}
@bot.callback_query_handler(func=lambda call: 'SugerirFechamento' in call.data)
def close_Ticket(call):

    # Limpa da memória informações prévias do usuário
    CLOSE_USER_DATA[call.from_user.id] = {}
    global mybotmsg
    # Pergunta qual o diário de trabalho
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    mybotmsg = bot.send_message(chat_id=call.from_user.id,
                              text="Informe o diário de fechamento.",reply_markup=types.ForceReply())

    # Insert state
    MyStorage.set_user_state(call.from_user.id, MS.CloseTicket.WAIT_Journal)

@bot.message_handler(func=lambda msg: MyStorage.get_current_state(msg.from_user.id) == MS.CloseTicket.WAIT_Journal)
def get_journal(msg):
    bot.delete_message(chat_id=msg.from_user.id, message_id=mybotmsg.message_id)
    # get user data
    close_data = CLOSE_USER_DATA[msg.from_user.id]

    # save MOTIVE to user data
    close_data['journal'] = msg.text

    # update storage
    CLOSE_USER_DATA[msg.from_user.id] = close_data

    # Confirm the Motive
    markup = Fc.YesNoQuery("GetCloseNote","NotConfirmedTicket")
    bot.send_message(text="Confirma o diário de trabalho ?",chat_id=msg.from_user.id,reply_markup=markup,reply_to_message_id=msg.message_id)

    bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id)

    # update storage
    MyStorage.set_user_state(msg.from_user.id, MS.CloseTicket.WAIT_Close_Note)

    print(close_data)

@bot.callback_query_handler(func=lambda call: 'GetCloseNote' in call.data)
def get_Close_Note(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    global mybotmsg
    mybotmsg = bot.send_message(chat_id=call.from_user.id,
                                text="Agora informe a nota de fechamento.",reply_markup=types.ForceReply())

    # Insert state
    MyStorage.set_user_state(call.from_user.id, MS.CloseTicket.WAIT_Close_Note)


@bot.message_handler(func=lambda msg: MyStorage.get_current_state(msg.from_user.id) == MS.CloseTicket.WAIT_Close_Note)
def save_note(msg):
    bot.delete_message(chat_id=msg.from_user.id, message_id=mybotmsg.message_id)
    # get user data
    close_data = CLOSE_USER_DATA[msg.from_user.id]

    # save JOURNAL to user data
    close_data['note'] = msg.text

    # update storage
    CLOSE_USER_DATA[msg.from_user.id] = close_data

    # Confirm the Note
    markup = Fc.YesNoQuery("ConfirmedCloseTicket", "NotConfirmedTicket")
    bot.send_message(text="Confirma a nota de fechamento ?", chat_id=msg.from_user.id, reply_markup=markup,
                     reply_to_message_id=msg.message_id)

    bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id)

    # update storage
    MyStorage.set_user_state(msg.from_user.id, MS.CloseTicket.Start)

    f = open("Files\CloseTicket.txt", "w")
    f.write(close_data['journal'] + "-" + close_data['note'])
    f.close()

    print(close_data)


@bot.callback_query_handler(func=lambda call: 'ConfirmedCloseTicket' in call.data)
def yes_Close(call):


    msgbot = Fc.CleanCallBack(call, "* Fechando " + caption + "*")

    os.system("Executables\CloseTicket.exe")

    MainCaption = open("Files\MainCaption.txt", "r", encoding="utf-8")

    bot.delete_message(chat_id=call.message.chat.id, message_id=msgbot.message_id)
    markup = Fc.controlMarkup(0, 5, fileContent)
    markup.add(types.InlineKeyboardButton(text="Atualizar", callback_data='atualizar'),
    types.InlineKeyboardButton(text="Próximo", callback_data='next'))

    bot.send_photo(call.from_user.id, photo=open('Files\BD-N1.png', 'rb'), caption=MainCaption, reply_markup=markup)

###Usado pelos dois

@bot.callback_query_handler(func=lambda call: 'NotConfirmedTicket' in call.data)
def no_Cancel(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    markup = Fc.SrControl(0,execute)
    bot.send_photo(call.from_user.id, photo=open('Files\SRimage.png', 'rb'), caption=caption, reply_markup=markup)


####End conversation
@bot.callback_query_handler(func=lambda call: 'TrabalharTicket' in call.data)
def alter_atribuition(call):
    msgbot=Fc.CleanCallBack(call,"Trabalhando Ticket ...")

    os.system("Executables\WorkTicket.exe")

    markup = Fc.SrControl(0,execute)
    bot.delete_message(chat_id=call.message.chat.id, message_id=msgbot.message_id)

    bot.send_photo(photo=open("Files/SRimage.png", 'rb'), caption=caption,
                           chat_id=call.message.chat.id,
                            reply_markup=markup)


@bot.callback_query_handler(func=lambda call: "ExecutarRPA" in call.data)
def exec_rpa_menu(call):
    bot.answer_callback_query(callback_query_id=call.id)
    markup = Fc.exec_menu()
    bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  reply_markup=markup)



@bot.callback_query_handler(func=lambda call: "ExtrairUsuario" in call.data)
def extrair_usuario(call):
    bot.answer_callback_query(callback_query_id=call.id)
    markup = Fc.extract_user()
    bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  reply_markup=markup)


@bot.callback_query_handler(func=lambda call: "Extract_COLISEU" in call.data)
def extrair_usuario_coliseu(call):
    bot.answer_callback_query(callback_query_id=call.id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    msg = bot.send_message(chat_id=call.from_user.id, text="Extraindo usuários do Coliseu",
                           parse_mode='markdown')

    os.system("Executables\ExtractUserColiseu.exe")


    bot.delete_message(chat_id=call.message.chat.id, message_id=msg.message_id)

    global mymsg
    mymsg = bot.send_message(chat_id=call.from_user.id, text="Os seguintes itens estão corretos ?",
                           parse_mode='markdown')
    global myexcel
    myexcel = bot.send_document(call.from_user.id, data=open('SendFiles\\' + caption + '.xlsx', 'rb'))

    global myphoto
    myphoto = bot.send_photo(call.from_user.id, photo=open('SendFiles\\' + caption + '.png', 'rb'))

    markup = Fc.YesNoQuery("ConfirmedExtract", "RefusedExtract")
    photo2 = bot.send_photo(call.from_user.id, photo=open('SendFiles\\' + caption + '(2).png', 'rb'),reply_markup=markup)


@bot.callback_query_handler(func=lambda call: "Extract_SPAZIO" in call.data)
def extrair_usuario_spazio(call):
    bot.answer_callback_query(callback_query_id=call.id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    msg = bot.send_message(chat_id=call.from_user.id, text="Extraindo usuários do Spazio",
                           parse_mode='markdown')

    os.system("Executables\ExtractUserSpazio.exe")

    bot.delete_message(chat_id=call.message.chat.id, message_id=msg.message_id)

    global mymsg
    mymsg = bot.send_message(chat_id=call.from_user.id, text="Os seguintes itens estão corretos ?",
                             parse_mode='markdown')
    global myexcel
    myexcel = bot.send_document(call.from_user.id, data=open('SendFiles\\' + caption + '.xlsx', 'rb'))

    markup = Fc.YesNoQuery("ConfirmedExtract", "RefusedExtract")
    photo = bot.send_photo(call.from_user.id, photo=open('SendFiles\\' + caption + '.png', 'rb'), reply_markup=markup)




@bot.callback_query_handler(func=lambda call: "RefusedExtract" in call.data)
def call_exec_true(call):
    bot.answer_callback_query(callback_query_id=call.id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=mymsg.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=myexcel.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=myphoto.message_id)

    markup = Fc.SrControl(0, execute)
    bot.answer_callback_query(callback_query_id=call.id)
    bot.edit_message_media(media=types.InputMediaPhoto(open("Files/SRimage.png", 'rb'), caption=caption),
                           chat_id=call.message.chat.id,
                           message_id=call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: "ConfirmedExtract" in call.data)
def call_exec_true(call):
    bot.answer_callback_query(callback_query_id=call.id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=mymsg.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=myexcel.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=myphoto.message_id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    msg = bot.send_message(chat_id=call.from_user.id, text="*Fazendo upload dos arquivos para o XTTs *",
                           parse_mode='markdown')

    os.system("Executables\\UploadExtractResults.exe")

    bot.delete_message(chat_id=call.message.chat.id, message_id=msg.message_id)

    markup = Fc.SrControl(0, execute)
    bot.send_photo(call.from_user.id, photo=open('Files\SRimage.png', 'rb'), caption=caption, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: "ExtractTrue" in call.data)
def call_exec_true(call):
    f = open("Files\SR-id.txt", "w")
    f.write(call.data.split(" ")[0])
    f.close()

    g = open("Files\SR-id.txt", "r")
    global caption
    caption = g.read()
    g.close()
    global execute
    execute = True

    bot.answer_callback_query(callback_query_id=call.id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    msg = bot.send_message(chat_id=call.from_user.id, text="*Consultando " + call.data.split(" ")[0] + "*", parse_mode='markdown')
    os.system("Executables\Sr_ScreenImage.exe")

    bot.delete_message(chat_id=call.message.chat.id, message_id=msg.message_id)

    markup = Fc.SrControl(0,execute)
    bot.send_photo(call.from_user.id, photo=open('Files\SRimage.png', 'rb'), caption=caption, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def call_exec_false(call):
    global execute
    execute = False
    f = open("Files\SR-id.txt", "w")
    f.write(call.data)
    f.close()

    g = open("Files\SR-id.txt", "r")
    global caption
    caption = g.read()
    g.close()


    bot.answer_callback_query(callback_query_id=call.id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    msg = bot.send_message(chat_id=call.from_user.id, text="*Consultando " + call.data + "*", parse_mode='markdown')
    os.system("Executables\Sr_ScreenImage.exe")

    bot.delete_message(chat_id=call.message.chat.id, message_id=msg.message_id)

    markup = Fc.SrControl(0,execute)
    bot.send_photo(call.from_user.id, photo=open('Files\SRimage.png', 'rb'),caption=caption,reply_markup=markup)




bot.polling()