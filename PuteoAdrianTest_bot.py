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

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [['Prueba de Sabiduria', 'Prueba Fisica'],
                  ['Prueba Mental','Prueba Final'],
                  ['Finalizadas todas las pruebas']]

reply_keyboard_2 = [['Ayuda'],
                  ['Apañao']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
markup_response = ReplyKeyboardMarkup(reply_keyboard_2, one_time_keyboard=True)

def start(update, context):

    bienvenida = "Eyyy,¿que pacha Adrían? Igual te pensabas que esto acababa aqui, lo siento colega pero aun te queda un rato mas de puteo,AVISO: NO INTENTES HACKEARME , he sido programado por uno de los mejores ingenieros de HPE en una tarde, es misión IMPOSIBLE, dicho esto aqui te dejo las misiones que tienes que hacer para desbloquear tu regalo. SUERTE CAMPEÓN!!!!"
    update.message.reply_text(bienvenida, reply_markup=markup)

    return CHOOSING


def custom_choice_ayuda(update, context):

    update.message.reply_text('Hola, que ase, esto es una prueba para ver si funciona la ayuda',reply_markup=markup)

    return CHOOSING

def custom_choice_hecho(update, context):

    update.message.reply_text('Hola, que ase, esto es una prueba para ver si funciona el panel de HECHO',reply_markup=markup)

    return CHOOSING    


def custom_choice(update, context):
    update.message.reply_text('Bienvenido a la prueba de mentira , la que para tí será la mas sencilla'
                              'Te veo un poco tenso, hazme 15 burpees',reply_markup=markup_response)

    return TYPING_CHOICE

def custom_choice_sabiduria(update, context):
    update.message.reply_text('Bienvenido a la prueba de Sabiduria '
                              'Aqui sergio se pondria las pilas')

    return CHOOSING

def custom_choice_fisica(update, context):

    if fisica == 0:
       update.message.reply_text('Bienvenido a la prueba Fisica , la que para tí será la mas sencilla'
                              'Te veo un poco tenso, hazme 15 burpees',reply_markup=markup_response)
    else : 
        update.message.reply_text('Tampoco te quieras poner tan fuerte campeón.')


    return TYPING_CHOICE

def custom_choice_mental(update, context):
    update.message.reply_text('Bienvenido a la prueba Mental ,'
                              'Aquí se insertará una prueba')

    return CHOOSING

def custom_choice_final(update, context):
    update.message.reply_text('Aqui está el Final BOSS, tienes que haber superado las anteriores para poder realizar esta')

    return CHOOSING


def received_information(update, context):

    update.message.reply_text('Has escrito Finalizado?')


    return CHOOSING


def done(update, context):

    if fisica == 1 and mental ==1  and sabiduria ==1 and final == 1:
        update.message.reply_text('Enhorabuena, has superado las pruebas, para celebrarlo vamos a tomar algo hasta el gran Capitán, te lo has ganado CRACK!!!')
        return ConversationHandler.END
    else : 
        update.message.reply_text('¿Donde vas crack?, todavía te quedan cosas por hacer.')
        return CHOOSING

   # user_data.clear()
    return ConversationHandler.END


def help_command(update, context):
    
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!',reply_markup=markup)
    global fisica 
    fisica = 1
    return CHOOSING

def fisica_done(update, context):
    
    """Send a message when the command /help is issued."""
    update.message.reply_text('Enhorabuena, has terminado la prueba Fisica!',reply_markup=markup)
    global fisica 
    fisica = 1
    return CHOOSING


def mental_done(update, context):
    
    """Send a message when the command /help is issued."""
    update.message.reply_text('Enhorabuena, has terminado la prueba Mental!',reply_markup=markup)
    global mental 
    mental = 1
    return CHOOSING

def sabiduria_done(update, context):
    
    """Send a message when the command /help is issued."""
    update.message.reply_text('Enhorabuena, has terminado la prueba de Sabiduria!',reply_markup=markup)
    global sabiduria 
    sabiduria = 1
    return CHOOSING
def final_done(update, context):
    
    """Send a message when the command /help is issued."""
    update.message.reply_text('Enhorabuena, has terminado la prueba Final!',reply_markup=markup)
    global final 
    final = 1
    return CHOOSING

def easter_egg(update, context): 
    update.message.reply_text('¡¡QUE ME COMAS TOL PEPINO!!',reply_markup=markup)
    return CHOOSING

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1394405549:AAGaWqylz6KTbdEpUYckUKR_dKrhGlO55lk", use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

   
    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CHOOSING: [MessageHandler(Filters.regex('^Prueba de Sabiduria$'),
                                      custom_choice_sabiduria),
                       MessageHandler(Filters.regex('^Prueba Fisica$'),
                                      custom_choice_fisica) ,
                       MessageHandler(Filters.regex('^Prueba Mental$'),
                                      custom_choice_mental) ,
                       MessageHandler(Filters.regex('^Prueba Final$'),
                                      custom_choice_final)                                    
                       ],
            TYPING_CHOICE: [
                       MessageHandler(Filters.regex('^Ayuda$'),
                                      custom_choice_ayuda) ,
                       MessageHandler(Filters.regex('^Apañao$'),
                                      custom_choice_hecho)                                       
                               ],

            TYPING_REPLY: [
                MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Finalizado$')),
                               received_information)],
        },

        fallbacks=[MessageHandler(Filters.regex('^Finalizadas todas las pruebas$'), done)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("vinagre", fisica_done))
    dp.add_handler(CommandHandler("cohelo", mental_done))
    dp.add_handler(CommandHandler("Nacho", sabiduria_done))
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