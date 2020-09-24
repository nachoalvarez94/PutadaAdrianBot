#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


fisica = 0
mental = 0
sabiduria = 0
final = 0
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, CHOOSE_MENTAL, TYPING_CHOICE, CHOOSE_FINAL  = range(4)

reply_keyboard = [['Prueba de Sabiduria', 'Prueba Fisica'],
                  ['Prueba Mental', 'Prueba Final'],
                  ['Finalizadas todas las pruebas']]

reply_keyboard_2 = [['Y ahora que'],
                  ['Buff Paso']]

                  
reply_keyboard_Mental = [['Error en Compilacion', '0'],
                  ['3','Deltoya']]

reply_keyboard_final = [['Que hago', 'Quien me puede ayudar'],
                  ['Buff Paso']]                  
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
markup_response = ReplyKeyboardMarkup(reply_keyboard_2, one_time_keyboard=True)
markup_mental = ReplyKeyboardMarkup(reply_keyboard_Mental, one_time_keyboard=True)
markup_final = ReplyKeyboardMarkup(reply_keyboard_final, one_time_keyboard=True)

def start(update, context):

    bienvenida = "Eyyy,¿que pacha Adrián? Igual te pensabas que esto acababa aquí, lo siento colega pero aun te queda un rato mas de puteo,AVISO: NO INTENTES HACKEARME , he sido programado por uno de los mejores ingenieros de HPE en una tarde, si no introduces los comandos predeterminados no funcionaré :( , dicho esto aqui te dejo las pruebas que tienes que hacer para desbloquear tu regalo. SUERTE CAMPEÓN!!!!"
    update.message.reply_text(bienvenida, reply_markup=markup)

    return CHOOSING


def custom_choice_ayuda(update, context):

    update.message.reply_text(
        '¿Has hecho los 15 burpees?, genial, \n'
        'Tus Maestros del Fisico Son Alberto y Jose, habla con este ultimo para que te proponga un ejercicio, Hasta que no lo hagas y Alberto no te de el visto bueno no consegiras Pasar la prueba\n'
        'Suerte'
        , reply_markup=markup_response)

    return TYPING_CHOICE


def custom_choice_hecho(update, context):

    update.message.reply_text(
        'Bueno vale, tu verás, pasamos a otra prueba entonces', reply_markup=markup)

    return CHOOSING


def custom_choice(update, context):
    update.message.reply_text('Bienvenido a la prueba de mentira , la que para tí será la mas sencilla'
                              'Te veo un poco tenso, hazme 15 burpees', reply_markup=markup_response)

    return TYPING_CHOICE


def custom_choice_sabiduria(update, context):

    if sabiduria == 0:
        update.message.reply_text('Bienvenido a la prueba de Sabiduria\n'
                                'Para superar esta prueba tienes que continuar la siguiente serie : \n'
                                '\n1, AA, C1, CC11,\n'
                                '\n¡Oh vaya! , Parece que Aroa y Cristina como Maestras de la Sabiduria  han robado algunas partes de la serie, acude a ellas y convencelas para que te digan  que partes faltan.'
                                '\nHasta que no te lo den no podrás completar esta prueba :)',reply_markup=markup)
        return CHOOSING
    else:
        update.message.reply_text(
        'La sabiduría consiste en saber que se sabe  y saber que no se sabe lo que no se sabe,\n'
        'No podemos enseñarte mas aqui',reply_markup=markup)
        return CHOOSING       


def custom_choice_fisica(update, context):

    if fisica == 0:
        update.message.reply_text('Bienvenido a la prueba Fisica , la que para tí será la mas sencilla'
                              'Te veo un poco tenso, hazme 15 burpees', reply_markup=markup_response)
        return TYPING_CHOICE                              
    else:
        update.message.reply_text(
            'Tampoco te quieras poner tan fuerte campeón.',reply_markup=markup)
        return CHOOSING 


def custom_choice_mental(update, context):

    if mental == 0:
        update.message.reply_text('Bienvenido a la prueba Mental: \n'
                                'Para esta Prueba tu Maestro es Nacho, No creo que tengas problema pero en caso de dudas puedes acudir a el, aqui te va la prueba: \n\n'
                                'Dado el siguiente codigo Java,¿Cual sería el resultado tras compilarlo/ejecutarlo?\n \n'
                                'public class test {\n'
                                                    '\t public static void add3 (Integer i) { \n'
                                                    '\t \t int val = i.intValue(); \n'
                                                    '\t \t val += 3;\n'
                                                    '\t \t i = new Integer (val); \n'
                                                    '\t} \n'
                                                    'public static void main (String args[]) {\n'
                                                    '\tInteger i = new Integer (0);\n'
                                                    '\t \tadd3 (i);\n'
                                                    '\t System.out.println (i.intValue ( ) );\n'
                                                    '\t \t}\n'
                                                    '} \n',
                                                    reply_markup=markup_mental)
        return CHOOSE_MENTAL
    else:
        update.message.reply_text(
        'SI, ERES MUY LISTO!!!, ¿No me has humillado ya suficiente?, Tira para otra prueba anda',reply_markup=markup)
        return CHOOSING

def custom_choice_final(update, context):
    if fisica == 1 and sabiduria == 1 and mental == 1:
        update.message.reply_text(
            'Felicidades compañero!! has llegado a la prueba final !!!,',reply_markup=markup_final)
        return CHOOSE_FINAL

    else:
        update.message.reply_text(
            'Aqui está el Final BOSS, tienes que haber superado las anteriores para poder realizar esta',reply_markup=markup)
        return CHOOSING


def custom_choice_Error(update, context):
    update.message.reply_text('ERROR: Prueba otra vez, o consultalo con el gurú ;)', reply_markup=markup_mental)

    return CHOOSE_MENTAL



def custom_choice_Troll(update, context):
    update.message.reply_text('¡¡¡QUE ME COMAS TOH LA POLLA!!!!!!' ,reply_markup=markup_mental)

    return CHOOSE_MENTAL

def custom_choice_Acierto(update, context):
    update.message.reply_text('¡¡¡¡ACIERTO!!! Estas hecho un mostrenco, acude a Nacho,  Maestro de la Mente  para que  el visto bueno  y te de la prueba por superada',reply_markup=markup)
    return CHOOSING

def custom_choice_marta(update, context):
    update.message.reply_text('¿A mi que me cuentas?, yo solo soy un mero informador, no se... mira a ver en el buzón , igual Marta te ha dejado algo ahí.',reply_markup=markup_final)
    return CHOOSE_FINAL

def custom_choice_jorge(update, context):
    update.message.reply_text('A ver, es arriesgado, pero creo que jorge te podría ayudar.',reply_markup=markup_final)
    return CHOOSE_FINAL



def received_information(update, context):

    update.message.reply_text('Has escrito Finalizado?')


    return CHOOSING


def done(update, context):

    if fisica == 1 and mental == 1 and sabiduria == 1 and final == 1:
        update.message.reply_text(
            'Enhorabuena, has superado todas las pruebas, Ya tienes tu merecido regalo, te lo has ganado CRACK!!!',)
        return ConversationHandler.END
    else:
        update.message.reply_text(
            '¿Donde vas crack?, todavía te quedan cosas por hacer.',reply_markup=markup)
        return CHOOSING

   # user_data.clear()
    return ConversationHandler.END


def help_command(update, context):

    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!', reply_markup=markup)
    global fisica
    fisica = 1
    return CHOOSING

def fisica_done(update, context):

    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Enhorabuena, has terminado la prueba Fisica!', reply_markup=markup)
    global fisica
    fisica = 1
    return CHOOSING


def mental_done(update, context):

    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Enhorabuena, has terminado la prueba Mental!', reply_markup=markup)
    global mental
    mental = 1
    return CHOOSING

def sabiduria_done(update, context):

    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Enhorabuena, has terminado la prueba de Sabiduria!', reply_markup=markup)
    global sabiduria
    sabiduria = 1
    return CHOOSING
def final_done(update, context):

    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Enhorabuena, has terminado la prueba Final!', reply_markup=markup)
    global final
    final = 1
    return CHOOSING

def easter_egg(update, context):
    update.message.reply_text(
        '¡¡QUE ME COMAS TOL PEPINO!!', reply_markup=markup)
    return CHOOSING

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        "1394405549:AAGaWqylz6KTbdEpUYckUKR_dKrhGlO55lk", use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher


    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CHOOSING: [MessageHandler(Filters.regex('^Prueba de Sabiduria$'),
                                      custom_choice_sabiduria),
                       MessageHandler(Filters.regex('^Prueba Fisica$'),
                                      custom_choice_fisica),
                       MessageHandler(Filters.regex('^Prueba Mental$'),
                                      custom_choice_mental),
                       MessageHandler(Filters.regex('^Prueba Final$'),
                                      custom_choice_final)
                       ],
            TYPING_CHOICE: [
                       MessageHandler(Filters.regex('^Y ahora que$'),
                                      custom_choice_ayuda),
                       MessageHandler(Filters.regex('^Buff Paso$'),
                                      custom_choice_hecho)
                               ],

            CHOOSE_MENTAL: [MessageHandler(Filters.regex('^(3|Error en Compilacion)$'),
                                      custom_choice_Error),
                       MessageHandler(Filters.regex('^0$'),
                                      custom_choice_Acierto),
                       MessageHandler(Filters.regex('^Deltoya$'),
                                      custom_choice_Troll)
            ],
            CHOOSE_FINAL: [MessageHandler(Filters.regex('^(3|Error en Compilacion)$'),
                                      custom_choice_Error),
                       MessageHandler(Filters.regex('^Que hago$'),
                                      custom_choice_marta),                                 
                       MessageHandler(Filters.regex('^Quien me puede ayudar$'),
                                      custom_choice_jorge),
                       MessageHandler(Filters.regex('^Buff Paso$'),
                                      custom_choice_hecho)                                      
            ],
        },

        fallbacks=[MessageHandler(Filters.regex(
            '^Finalizadas todas las pruebas$'), done)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("vinagre", fisica_done))
    dp.add_handler(CommandHandler("Nacho", mental_done))
    dp.add_handler(CommandHandler("cohelo", sabiduria_done))
    dp.add_handler(CommandHandler("Felicidades", final_done))
    dp.add_handler(CommandHandler("asundino", easter_egg))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
